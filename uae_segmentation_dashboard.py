import streamlit as st
import pandas as pd

st.set_page_config(page_title="UAE Customer Segmentation", layout="wide")

st.title("🇦🇪 UAE Customer Segmentation Dashboard")
st.markdown("This dashboard provides a detailed segmentation of the UAE population using demographic, geographic, psychographic, and behavioral criteria.")

st.sidebar.header("📊 Filters")
segmentation_type = st.sidebar.selectbox("Select Segmentation Type", [
    "Demographic", "Geographic", "Psychographic", "Behavioral", "Technographic", "Cultural"
])

# Define segmentation data
segmentation_data = {
    "Demographic": {
        "Age Groups": {
            "0-14 years": "15.1%",
            "15-24 years": "9.1%",
            "25-54 years": "68.6%",
            "55-64 years": "5.2%",
            "65+ years": "1.9%",
        },
        "Gender": {
            "Male": "69%",
            "Female": "31%",
        },
        "Nationality": {
            "Expatriates": "88.1%",
            "Emiratis": "11.9%",
        },
        "Education Levels": {
            "University+": "High",
            "Secondary": "Moderate",
            "Primary/Below": "Low",
        }
    },

    "Geographic": {
        "By Emirate": {
            "Dubai": "3.81M",
            "Abu Dhabi": "3.79M",
            "Sharjah": "~2.0M",
            "Others": "~2.0M combined"
        },
        "Urban vs Rural": {
            "Urban": "88%",
            "Rural": "12%",
        }
    },

    "Psychographic": {
        "Lifestyle Preferences": [
            "Luxury seekers", "Health-conscious", "Tech-savvy", "Traditionalists"
        ],
        "Values & Attitudes": [
            "Eco-conscious", "Cultural/religious alignment", "Status-driven"
        ]
    },

    "Behavioral": {
        "Shopping Habits": [
            "Online-first", "In-store lovers", "Hybrid shoppers"
        ],
        "Brand Loyalty": [
            "Loyalists", "Price-sensitive", "Variety seekers"
        ],
        "Usage Rate": [
            "Heavy", "Moderate", "Light users"
        ],
        "Benefits Sought": [
            "Quality", "Convenience", "Value for money"
        ]
    },

    "Technographic": {
        "Technology Adoption": [
            "Early adopters", "Mainstream", "Late adopters"
        ],
        "Device Usage": [
            "Mobile-first", "Multi-device", "Desktop-centric"
        ]
    },

    "Cultural": {
        "Ethnic Backgrounds": [
            "South Asian", "Arab expats", "Western expats", "East Asian"
        ],
        "Religion": [
            "Muslim (majority)", "Others (Christianity, Hinduism, etc.)"
        ]
    }
}

# Render the selected segmentation
st.subheader(f"📍 {segmentation_type} Segmentation")

data = segmentation_data.get(segmentation_type)

if isinstance(data, dict):
    for category, values in data.items():
        st.markdown(f"### {category}")
        if isinstance(values, dict):
            df = pd.DataFrame(list(values.items()), columns=["Segment", "Details"])
            st.table(df)
        elif isinstance(values, list):
            for item in values:
                st.markdown(f"- {item}")
else:
    st.warning("No data available for this segmentation type.")

st.markdown("---")
st.caption("Data compiled from Global Media Insight, Wikipedia, and other public sources as of 2024.")
