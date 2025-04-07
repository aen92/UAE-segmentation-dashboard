import streamlit as st
import pandas as pd

st.set_page_config(page_title="🇦🇪 UAE Extended Customer Segmentation (2024)", layout="wide")

st.title("📊 UAE Customer Segmentation – Extended Insights (2024)")
st.markdown("This dashboard provides a segmentation of the UAE population based on nationality, religion, length of stay, and marital status.")

segmentation_type = st.sidebar.selectbox("Choose segmentation type", [
    "Nationality", "Religion", "Length of Stay", "Marital Status"
])

# NATIONALITY SEGMENTATION
if segmentation_type == "Nationality":
    st.header("Top Expat Nationalities in the UAE (2024 estimates)")
    
    nationality_data = pd.DataFrame({
        "Nationality": [
            "Indian", "Pakistani", "Bangladeshi", "Filipino", "Egyptian",
            "Syrian", "Sudanese", "Jordanian", "British", "Other"
        ],
        "Population Estimate": [
            3400000, 1280000, 1000000, 700000, 900000,
            242000, 200000, 150000, 120000, 2000000
        ]
    }).set_index("Nationality")

    st.bar_chart(nationality_data)

# RELIGION SEGMENTATION
elif segmentation_type == "Religion":
    st.header("Religious Affiliation in the UAE (Estimates)")

    religion_data = pd.DataFrame({
        "Religion": ["Islam (Sunni + Shia)", "Christianity", "Hinduism", "Buddhism", "Others"],
        "Percentage": [76, 13, 7, 2, 2]
    }).set_index("Religion")

    st.bar_chart(religion_data)

# LENGTH OF STAY
elif segmentation_type == "Length of Stay":
    st.header("Length of Stay of Residents (Expat Estimates)")

    length_data = pd.DataFrame({
        "Years in UAE": [
            "Less than 1 year", "1-5 years", "6-10 years", "11-20 years", "20+ years"
        ],
        "Percentage": [12, 38, 22, 18, 10]
    }).set_index("Years in UAE")

    st.bar_chart(length_data)

# MARITAL STATUS
elif segmentation_type == "Marital Status":
    st.header("Marital Status in UAE (Estimates for Age 25+)")
    
    marital_data = pd.DataFrame({
        "Status": ["Married", "Single", "Divorced", "Widowed"],
        "Percentage": [58, 35, 5, 2]
    }).set_index("Status")

    st.bar_chart(marital_data)

# FOOTER
st.markdown("---")
st.caption("Sources: Global Media Insight, Wikipedia, Gulf News, Statista – 2024 publicly available data.")
