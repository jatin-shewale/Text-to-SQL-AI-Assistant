import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.header("⚙️ Options")

        st.markdown("### Sample Queries")
        st.write("• Who scored highest?")
        st.write("• Show grade A students")

        if st.button("Clear Chat"):
            st.session_state.chat = []