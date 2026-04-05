import streamlit as st
from src.ui.styles import load_css

def setup_page():
    st.set_page_config(
        page_title="Text-to-SQL AI",
        layout="wide"
    )

    st.markdown(load_css(), unsafe_allow_html=True)

    st.title("🤖 Text-to-SQL AI")
    st.caption("Ask → SQL → Result")