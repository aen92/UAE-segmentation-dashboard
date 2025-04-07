import streamlit as st
import pandas as pd

st.set_page_config(page_title="🇦🇪 UAE Customer Segmentation 2024", layout="wide")

st.title("📊 UAE Customer Segmentation Dashboard (2024)")
st.markdown("Latest demographic, geographic, income, and behavioral insights on the UAE population, based on 2024 data.")

segmentation_type = st.sidebar.selectbox("Select segmentation type", [
    "Demographic", "Geographic", "Income", "Technographic", "Behavioral"
])

# DEMOGRAPHIC SEGMENTATION
if segmentation_type == "Demographic":
    st.header("Demographic Segmentation")
    
    age_data = {
        "0-14": 15.1,
        "15-24": 9.1,
        "25-54": 68.6,
        "55-64": 5.2,
        "65+": 2.0
    }
    df_age = pd.DataFrame(age_data.items(), columns=["Age Group", "Percentage"])
    st.subheader("Age Distribution")
    st.bar_chart(df_age.set_index("Age Group"))

    st.subheader("Gender Distribution")
    gender_data = pd.DataFrame({
        "Gender": ["Male", "Female"],
        "Percentage": [69, 31]
    }).set_index("Gender")
    st.bar_chart(gender_data)

    st.subheader("Nationality Breakdown")
    nationality_data = pd.DataFrame({
        "Group": ["Expatriates", "Emiratis"],
        "Percentage": [88.1, 11.9]
    }).set_index("Group")
    st.bar_chart(nationality_data)

# GEOGRAPHIC SEGMENTATION
elif segmentation_type == "Geographic":
    st.header("Geographic Segmentation")
    
    pop_by_emirate = {
        "Dubai": 3810000,
        "Abu Dhabi": 3790000,
        "Sharjah": 1830000,
        "Ajman": 504000,
        "Ras Al Khaimah": 416000,
        "Fujairah": 256000,
        "Umm Al Quwain": 49100,
        "Al Ain": 766000,
        "Other": 160000
    }

    df_geo = pd.DataFrame(pop_by_emirate.items(), columns=["Emirate/City", "Population"]).set_index("Emirate/City")
    st.subheader("Population by Emirate")
    st.bar_chart(df_geo)

    st.subheader("Urban vs Rural")
    st.write("**Urban** population: 88%")
    st.write("**Rural** population: 12%")

# INCOME SEGMENTATION
elif segmentation_type == "Income":
    st.header("Income Segmentation (Estimates)")
    income_data = pd.DataFrame({
        "Income Level": ["High", "Middle", "Low"],
        "Est. Monthly Income (AED)": [40000, 10000, 2500],
        "Population Share (%)": [5, 50, 45]
    })
    st.dataframe(income_data)

# TECHNO SEGMENTATION
elif segmentation_type == "Technographic":
    st.header("Technographic Segmentation")

    st.subheader("Device Usage (2024 est.)")
    tech_data = pd.DataFrame({
        "Device Type": ["Mobile-first", "Multi-device", "Desktop-centric"],
        "Percentage": [75, 20, 5]
    }).set_index("Device Type")
    st.bar_chart(tech_data)

    st.subheader("Internet Penetration")
    st.write("As of 2024, UAE internet penetration is over **99%** (source: TRA UAE).")

# BEHAVIORAL SEGMENTATION
elif segmentation_type == "Behavioral":
    st.header("Behavioral Segmentation")

    st.subheader("Shopping Preference (2024 est.)")
    shopping_data = pd.DataFrame({
        "Mode": ["Online-first", "In-store", "Hybrid"],
        "Percentage": [60, 25, 15]
    }).set_index("Mode")
    st.bar_chart(shopping_data)

    st.subheader("Brand Loyalty")
    loyalty_data = pd.DataFrame({
        "Group": ["Loyal Buyers", "Price-sensitive", "Explorers"],
        "Percentage": [40, 35, 25]
    }).set_index("Group")
    st.bar_chart(loyalty_data)

# FOOTER
st.markdown("---")
st.caption("Source: Global Media Insight, TRA UAE, Wikipedia, and public 2024 population data.")
