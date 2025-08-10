import time

import streamlit as st

from language_profile import main_Program
st.set_page_config(page_title="Popo App", layout= 'wide')

if not st.user.is_logged_in:
    st.header("Login Part")
    st.markdown("## Your Personal Language Exam Preparation Assistant")
    st.markdown("Welcome to Popo Tool! This application is designed to help you prepare for various language proficiency exams. Select your target language, exam type, and preparation time to get started.")
    if st.button('Google'):
        st.login("google")
else:
    st.text(st.user.email)
    main_Program()
    if st.button('Logout'):
        st.logout()

