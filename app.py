import streamlit as st
import sqlite3
from datetime import datetime

# --- Streamlit UI ---
st.set_page_config(page_title="Extension Cost Estimator", page_icon="🏠")
st.title("🏠 Construction Cost Estimator (Ireland)")
st.markdown("Enter details about your planned extension:")

location = st.selectbox("📍 Location (County)", ["Dublin", "Cork", "Galway", "Limerick"])
roof_type = st.selectbox("🏗️ Roof Type", ["Flat", "Pitched"])
finish_quality = st.selectbox("🎨 Finish Quality", ["Standard", "Premium", "Luxury"])
labour_cost = st.number_input("👷 Estimated Labour Cost (€)", min_value=10000, max_value=50000, value=20000, step=1000)
duration_weeks = st.slider("🕐 Duration (Weeks)", 4, 12, 6)

# --- Function to save to SQLite ---
def save_to_db(data):
    try:
        conn = sqlite3.connect("extension_inputs.db")
        c = conn.cursor()
        # Create table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                location TEXT,
                roof_type TEXT,
                finish_quality TEXT,
                labour_cost REAL,
                duration_weeks INTEGER
            )
        ''')
        # Insert the values
        c.execute('''
            INSERT INTO submissions (timestamp, location, roof_type, finish_quality, labour_cost, duration_weeks)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
    finally:
        conn.close()

# --- Save input on submit ---
if st.button("💬 Estimate Cost"):
    timestamp = datetime.now().isoformat()
    values = (timestamp, location, roof_type, finish_quality, labour_cost, duration_weeks)
    save_to_db(values)
    st.success("✅ Submission saved to database.")

st.caption("📂 Data is stored locally in `extension_inputs.db` in the app folder.")
