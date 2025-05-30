import streamlit as st
import json
from agents.classifier_agent import classify_and_route

st.set_page_config(page_title="AI Classifier & Router", layout="centered")
st.title("📬 AI Classifier & Router")

# Initialize session state to track submission
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "result" not in st.session_state:
    st.session_state.result = None

# Form UI (only show if not yet submitted)
if not st.session_state.submitted:
    st.write("Upload a JSON file or enter an Email manually below:")

    uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])
    email_text = st.text_area("Or paste Email content here", height=200)

    if st.button("Classify & Route"):
        if uploaded_file:
            try:
                input_json = json.load(uploaded_file)
                result = classify_and_route(input_json)
                st.session_state.result = result
                st.session_state.submitted = True
            except Exception as e:
                print("error",e)
                st.error(f"Invalid JSON file: {e}")
        elif email_text.strip():
            result = classify_and_route(email_text)
            st.session_state.result = result
            st.session_state.submitted = True
        else:
            st.warning("Please upload a JSON file or enter Email text.")

# # Show result if submitted
# if st.session_state.submitted:
#     st.success("✅ Input successfully classified and routed.")
#     st.markdown("### 📦 Classification & Routing Result")
#     st.json(st.session_state.result)

#     if st.button("🔄 Reset"):
#         st.session_state.submitted = False
#         st.session_state.result = None
