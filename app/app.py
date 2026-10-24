from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="India City Intelligence",
    page_icon="🌏",
    layout="wide",
)

st.title("🌏 India City Intelligence")
st.subheader("Smart City Decision Dashboard")
st.caption("Explore the supplied air-quality dataset by state, city, and pollutant.")

APP_DIR = Path(__file__).resolve().parent
PROJECT_DIR = APP_DIR.parent
DATA_CANDIDATES = [
    PROJECT_DIR / "data" / "aqi_cleaned.csv",
    APP_DIR / "aqi_cleaned.csv",
]

@st.cache_data
def load_data(path_string: str) -> pd.DataFrame:
    df = pd.read_csv(path_string)
    expected = {
        "country", "state", "city", "station", "last_update",
        "latitude", "longitude", "pollutant_id",
        "pollutant_min", "pollutant_max", "pollutant_avg",
    }
    missing = expected - set(df.columns)
    if missing:
        raise ValueError("Dataset is missing required columns: " + ", ".join(sorted(missing)))

    for col in ["latitude", "longitude", "pollutant_min", "pollutant_max", "pollutant_avg"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in ["state", "city", "station", "pollutant_id"]:
        df[col] = df[col].astype("string").str.strip()
    return df

data_path = next((p for p in DATA_CANDIDATES if p.exists()), None)

if data_path is None:
    st.error("Could not find data/aqi_cleaned.csv. Put the cleaned CSV in the project's data folder.")
    st.code("India_City_Intelligence/\n├── data/aqi_cleaned.csv\n└── app/app.py")
    st.stop()

try:
    df = load_data(str(data_path))
except Exception as exc:
    st.error(f"Could not load the dataset: {exc}")
    st.stop()

st.info(f"Dataset loaded from: `{data_path.relative_to(PROJECT_DIR)}`")

with st.sidebar:
    st.header("Filters")
    states = sorted(df["state"].dropna().astype(str).unique().tolist())
    selected_states = st.multiselect("State", states, default=[])
    filtered = df.copy()
    if selected_states:
        filtered = filtered[filtered["state"].isin(selected_states)]

    cities = sorted(filtered["city"].dropna().astype(str).unique().tolist())
    selected_cities = st.multiselect("City", cities, default=[])
    if selected_cities:
        filtered = filtered[filtered["city"].isin(selected_cities)]

    pollutants = sorted(filtered["pollutant_id"].dropna().astype(str).unique().tolist())
    selected_pollutants = st.multiselect(
        "Pollutant",
        pollutants,
        default=[p for p in pollutants if p.upper() in {"PM2.5", "PM10"}],
    )
    if selected_pollutants:
        filtered = filtered[filtered["pollutant_id"].isin(selected_pollutants)]

valid_avg = filtered["pollutant_avg"].dropna()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Records in view", f"{len(filtered):,}")
c2.metric("Cities in view", f"{filtered['city'].nunique():,}")
c3.metric("Stations in view", f"{filtered['station'].nunique():,}")
c4.metric("Missing average readings", f"{filtered['pollutant_avg'].isna().sum():,}")

st.divider()
left, right = st.columns(2)

with left:
    st.markdown("### Average reported value by pollutant")
    pollutant_summary = (
        filtered.dropna(subset=["pollutant_avg"])
        .groupby("pollutant_id", as_index=False)["pollutant_avg"]
        .mean()
        .sort_values("pollutant_avg", ascending=False)
    )
    if pollutant_summary.empty:
        st.warning("No non-missing average measurements match these filters.")
    else:
        st.bar_chart(pollutant_summary.set_index("pollutant_id")["pollutant_avg"])

with right:
    st.markdown("### Top 10 city-pollutant averages")
    city_summary = (
        filtered.dropna(subset=["pollutant_avg", "city"])
        .groupby(["state", "city", "pollutant_id"], as_index=False)["pollutant_avg"]
        .mean()
        .sort_values("pollutant_avg", ascending=False)
        .head(10)
    )
    if city_summary.empty:
        st.warning("No city measurements match these filters.")
    else:
        city_summary["City / pollutant"] = (
            city_summary["city"].astype(str) + " (" +
            city_summary["pollutant_id"].astype(str) + ")"
        )
        st.bar_chart(city_summary.set_index("City / pollutant")["pollutant_avg"])

st.markdown("### Monitoring station map")
map_df = filtered.dropna(subset=["latitude", "longitude"]).copy()
map_df = map_df[
    map_df["latitude"].between(-90, 90) &
    map_df["longitude"].between(-180, 180)
]
if map_df.empty:
    st.warning("No valid coordinates match the selected filters.")
else:
    st.map(map_df[["latitude", "longitude"]].rename(
        columns={"latitude": "lat", "longitude": "lon"}
    ))

st.markdown("### Filtered records")
st.dataframe(filtered, use_container_width=True, hide_index=True)

csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download filtered data as CSV",
    data=csv,
    file_name="india_city_intelligence_filtered.csv",
    mime="text/csv",
)

st.caption(
    "This app analyzes the provided dataset snapshot. Missing values are not zero, "
    "pollutant values should not be compared across different pollutant types as if "
    "they shared the same scale, and this is not a live monitoring or health advisory service."
)
