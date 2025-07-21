import streamlit as st
import pandas as pd
def load_data():
    df = pd.read_csv("hdi_highest_regions_dfs.csv")
    return df
df = load_data()
required_columns = ['Continent', 'Country', 'Region', 'Year:2025']
if not all(col in df.columns for col in required_columns):
    st.error("Data does not contain required columns: Continent, Country, Region, Year:2025")
    st.stop()
st.title("HDI Recommender ('Best Place to live') 🌍")
continent = st.selectbox("Select Continent", sorted(df['Continent'].dropna().unique()))
filtered_countries = df[df['Continent'] == continent]['Country'].dropna().unique()
country = st.selectbox("Select Country", sorted(filtered_countries))
if country:
    country_data = df[df['Country'] == country].copy()
    country_data['HDI Value'] = (country_data['Year:2025'] * 100).round(0).astype(int)
    top_regions = (
        country_data
        .sort_values(by='HDI Value', ascending=False)
        .head(3)
        [['Region', 'HDI Value']]
        .reset_index(drop=True)
    )
    st.subheader(f"Top 3 Best Regions To Settle in {country}")
    st.dataframe(top_regions, use_container_width=True)