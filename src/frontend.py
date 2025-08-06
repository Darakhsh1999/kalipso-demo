import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/assess"
HEALTH_URL = "http://localhost:8000/health"

st.set_page_config(page_title="Kalipso Policy Analyst Demo", layout="centered")
st.title("Kalipso Policy Analyst Demo")

# Backend health check
try:
    health_response = requests.get(HEALTH_URL, timeout=3)
    health_json = health_response.json()
    if health_json.get("status") != "ok":
        st.warning(f"Backend health check failed: {health_json}")
except Exception as e:
    st.error(f"Could not connect to backend at {HEALTH_URL}: {e}")

# Upload section
uploaded_file = st.file_uploader("Upload a single PDF file", type=["pdf"], accept_multiple_files=False)

# Submit button
submit_disabled = uploaded_file is None
if st.button("Submit", disabled=submit_disabled):
    if uploaded_file is not None:
        with st.spinner("Uploading and processing PDF..."):
            files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
            try:
                response = requests.post(BACKEND_URL, files=files)
                if response.status_code == 200:
                    st.success("Received response from backend!")
                    st.text_area(
                        "Raw JSON Output", 
                        value=response.text, 
                        height=400, 
                        max_chars=None, 
                        key="output_area"
                    )
                else:
                    st.error(f"Backend error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
    else:
        st.warning("Please upload a PDF file before submitting.")
else:
    st.info("Upload a PDF file to enable submission.")
