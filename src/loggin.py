import streamlit as st

from language_profile import main_Program


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

    st.header("Login Part")
    st.set_page_config(page_title="Popo App", layout= 'wide')
    st.markdown("## Your Personal Language Exam Preparation Assistant")
    st.markdown("Welcome to Popo Tool! This application is designed to help you prepare for various language proficiency exams. Select your target language, exam type, and preparation time to get started.")
    if st.button('Login with Google'):
        st.success("Logged in successfully!")
        st.session_state.logged_in = True
else:
    main_Program()