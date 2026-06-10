import streamlit as st
import pandas as pd
import os
st.set_page_config(
    page_title="RentalHub",
    page_icon="🏠",
    layout="wide"
)
st.set_page_config(page_title="Rental App")

st.title("🏠 Rental App")

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
