import streamlit as st
import pandas as pd

def init_chat():
    if "chat" not in st.session_state:
        st.session_state.chat = []

def display_chat():
    for msg in st.session_state.chat:
        if msg["role"] == "user":
            st.markdown(f"<div class='chat-box user'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-box bot'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

            if "sql" in msg:
                st.markdown("**SQL**")
                st.markdown(f"<div class='sql-box'>{msg['sql']}</div>", unsafe_allow_html=True)

            if "result" in msg:
                try:
                    df = pd.DataFrame(eval(msg["result"]))
                    st.dataframe(df)
                except:
                    st.write(msg["result"])

def handle_input(run_pipeline):
    user_input = st.chat_input("Ask something...")

    if user_input:
        st.session_state.chat.append({"role": "user", "content": user_input})

        try:
            sql, result = run_pipeline(user_input)

            st.session_state.chat.append({
                "role": "bot",
                "content": "Result 👇",
                "sql": sql,
                "result": result
            })

        except Exception as e:
            st.session_state.chat.append({
                "role": "bot",
                "content": f"Error: {e}"
            })

        st.rerun()