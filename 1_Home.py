import streamlit as st

st.set_page_config(
    page_title="RentalHub",
    page_icon="🏠",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.hero {
    text-align:center;
    padding:40px 20px;
}

.hero h1 {
    font-size:48px;
    font-weight:700;
}

.hero p {
    color:gray;
    font-size:20px;
}

.category-card {
    background:#f8fafc;
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #e5e7eb;
    transition:0.3s;
}

.category-card:hover {
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown("""
<div class="hero">
    <h1>🏠 RentalHub</h1>
    <p>Rent Anything, Anywhere</p>
</div>
""", unsafe_allow_html=True)

# ---------- SEARCH ----------
st.text_input(
    "🔍 Search by location, property, vehicle..."
)

st.divider()

# ---------- CATEGORIES ----------
st.subheader("Browse Categories")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="category-card">
        <h1>🏠</h1>
        <h4>Houses & Flats</h4>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="category-card">
        <h1>🛏️</h1>
        <h4>PG & Hostel</h4>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="category-card">
        <h1>🚗</h1>
        <h4>Vehicles</h4>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="category-card">
        <h1>🎉</h1>
        <h4>Event Items</h4>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------- FEATURED LISTINGS ----------
st.subheader("Featured Rentals")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
🏠 2BHK Apartment

📍 Ahmedabad

₹15,000/month
""")
    st.button("View Details", key="house")

with c2:
    st.info("""
🚗 Honda City

📍 Ahmedabad

₹1,200/day
""")
    st.button("View Details", key="car")

with c3:
    st.info("""
🎉 Wedding Tent Setup

📍 Surat

₹5,000/event
""")
    st.button("View Details", key="tent")

st.divider()

st.caption("© 2026 RentalHub | Find the perfect rental for every need")
