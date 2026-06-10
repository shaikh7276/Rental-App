import streamlit as st
import pandas as pd
import os
st.set_page_config(
    page_title="RentalHub",
    page_icon="🏠",
    layout="wide"
)
hide = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

st.markdown(hide, unsafe_allow_html=True)
st.set_page_config(page_title="Rental App")

st.markdown("""
<h1 style='text-align:center'>
🏠 RentalHub
</h1>

<h4 style='text-align:center;color:gray'>
Find your perfect rental property
</h4>
""", unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)

with col1:
    st.metric("Properties","120")

with col2:
    st.metric("Bookings","58")

with col3:
    st.metric("Users","210")
    st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/25/25694.png",
    width=80
)

st.sidebar.title("RentalHub")
search = st.text_input(
    "🔍 Search by location"
)

# Create CSV files if they don't exist
if not os.path.exists("properties.csv"):
    pd.DataFrame(
        columns=["Title", "Location", "Rent", "Description"]
    ).to_csv("properties.csv", index=False)

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Property", "View Properties"]
)

if menu == "Add Property":

    st.header("Add Property")

    title = st.text_input("Property Title")
    location = st.text_input("Location")
    rent = st.number_input("Monthly Rent", min_value=0)
    description = st.text_area("Description")

    if st.button("Save Property"):

        new_property = pd.DataFrame({
            "Title": [title],
            "Location": [location],
            "Rent": [rent],
            "Description": [description]
        })

        df = pd.read_csv("properties.csv")
        df = pd.concat([df, new_property], ignore_index=True)
        df.to_csv("properties.csv", index=False)

        st.success("Property Added Successfully!")

elif menu == "View Properties":

    st.header("Available Properties")

    df = pd.read_csv("properties.csv")

    if len(df) > 0:
        st.dataframe(df)
    else:
        st.info("No properties available.")
