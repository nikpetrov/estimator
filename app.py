import streamlit as st

st.set_page_config(page_title="Extension Cost Estimator", page_icon="🏠")

st.title("🏠 Extension Cost Estimator (Ireland)")

st.markdown("Enter details about your planned 40 sqm extension:")

location = st.selectbox("📍 Location (County)", ["Dublin", "Cork", "Galway", "Limerick"])
roof_type = st.selectbox("🏗️ Roof Type", ["Flat", "Pitched"])
finish_quality = st.selectbox("🎨 Finish Quality", ["Standard", "Premium", "Luxury"])
labour_cost = st.number_input("👷 Estimated Labour Cost (€)", min_value=10000, max_value=50000, value=20000, step=1000)
duration_weeks = st.slider("🕐 Duration (Weeks)", 4, 12, 6)

if st.button("💬 Estimate Cost"):
    st.subheader("📊 Your Input Summary")
    st.write(f"- Location: **{location}**")
    st.write(f"- Roof Type: **{roof_type}**")
    st.write(f"- Finish Quality: **{finish_quality}**")
    st.write(f"- Labour Cost: **€{labour_cost}**")
    st.write(f"- Estimated Duration: **{duration_weeks} weeks**")

    st.warning("🔧 Cost estimation model not yet connected. This is just the UI setup.")
