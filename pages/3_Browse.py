import streamlit as st
import pandas as pd
import os

st.title("🔍 Browse Rentals")

# Check file exists
if not os.path.exists("data/listings.csv"):
    st.warning("No listings available.")
    st.stop()

df = pd.read_csv("data/listings.csv")

if df.empty:
    st.info("No listings found.")
    st.stop()

# ---------- FILTERS ----------

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox(
        "Category",
        ["All"] + list(df["Category"].unique())
    )

with col2:
    location = st.text_input("Location")

# Apply Filters

filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

if location:
    filtered_df = filtered_df[
        filtered_df["Location"]
        .str.contains(location, case=False)
    ]

st.write(f"Found {len(filtered_df)} listings")

st.divider()

# ---------- CARD DESIGN ----------

st.markdown("""
<style>

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    border:1px solid #e5e7eb;
    margin-bottom:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.05);
}

.price{
    color:#4f46e5;
    font-size:22px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------- DISPLAY LISTINGS ----------

for index, row in filtered_df.iterrows():

    st.markdown(f"""
    <div class="card">
        <h3>{row['Title']}</h3>

        <p>
        📂 {row['Category']} <br>
        📍 {row['Location']}
        </p>

        <div class="price">
        ₹{row['Price']}
        </div>

        <p>{row['Description']}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "View Details",
        key=f"view_{index}"
    ):
        st.success(
            f"You selected {row['Title']}"
        )

    st.write("")

