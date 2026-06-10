import streamlit as st
import pandas as pd
import os

st.title("➕ Add New Listing")

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create CSV if it doesn't exist
if not os.path.exists("data/listings.csv"):
    pd.DataFrame(
        columns=[
            "Title",
            "Category",
            "Location",
            "Price",
            "Description"
        ]
    ).to_csv("data/listings.csv", index=False)

# Form
with st.form("listing_form"):

    title = st.text_input("Title")

    category = st.selectbox(
        "Category",
        [
            "Houses & Flats",
            "PG & Hostel",
            "Vehicles",
            "Event Items"
        ]
    )

    location = st.text_input("Location")

    price = st.number_input(
        "Rental Price (₹)",
        min_value=0
    )

    description = st.text_area(
        "Description"
    )

    submit = st.form_submit_button(
        "Add Listing"
    )

if submit:

    new_listing = pd.DataFrame({
        "Title": [title],
        "Category": [category],
        "Location": [location],
        "Price": [price],
        "Description": [description]
    })

    df = pd.read_csv("data/listings.csv")

    df = pd.concat(
        [df, new_listing],
        ignore_index=True
    )

    df.to_csv(
        "data/listings.csv",
        index=False
    )

    st.success("✅ Listing Added Successfully!")

    st.balloons()

# Preview Existing Listings
st.divider()

st.subheader("Current Listings")

df = pd.read_csv("data/listings.csv")

if len(df) > 0:
    st.dataframe(df, use_container_width=True)
else:
    st.info("No listings added yet.")
