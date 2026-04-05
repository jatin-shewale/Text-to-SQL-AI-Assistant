import streamlit as st
from PIL import Image

from src.pipeline import run_pipeline
from src.ui.layout import setup_page
from src.ui.sidebar import render_sidebar
from src.ui.chat import init_chat, display_chat, handle_input


st.set_page_config(page_title="Text-to-SQL AI", layout="wide")


try:
    logo = Image.open("screenshots/logo.png")
except:
    logo = None


if logo:
    st.sidebar.image(logo, width=150)


if logo:
    st.image(logo, width=120)

st.title("🤖 Text-to-SQL AI Assistant")


setup_page()
render_sidebar()
init_chat()


display_chat()
st.markdown("---")
handle_input(run_pipeline)

