import streamlit as st
import hydralit_components as hc

def contact_us():
    st.subheader(":mailbox: Speak to us!")
    with st.form(key='form1'):
        firstname = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Insert message here")
        submitted = st.form_submit_button("Send email")
        if submitted:
            st.success("Hello {}, your email has been sent ".format(firstname))
