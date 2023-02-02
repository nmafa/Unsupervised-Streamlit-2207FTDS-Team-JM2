import streamlit as st

def style(file_name):
    with open(file_name) as f:
        st.markdown(f"<style >{f.read()}</style>", unsafe_allow_html=True)