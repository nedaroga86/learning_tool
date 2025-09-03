import time
import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.language_profile import get_new_profile
from src.save_profile import get_user_profile
from src.buttons import loggin_button


st.set_page_config(page_title="Popo App", layout= 'wide')

if not st.user.is_logged_in:
    st.header("Login Part")
    st.markdown("## Your Personal Language Exam Preparation Assistant")
    st.markdown("Welcome to Popo Tool! This application is designed to help you prepare for various language proficiency exams. Select your target language, exam type, and preparation time to get started.")
    if loggin_button('Login with Google'):
        st.login("google")
else:
    # st.header("Test Part")
    # st.write(st.user.is_logged_in)
    # st.write(st.user.email)
    # pem = st.secrets["gcp_service_account"]["private_key"]
    # lines = pem.splitlines()
    # st.write(lines[0], "...", lines[-1], f"({len(lines)} líneas)")
    # time.sleep(15)
    st.session_state.profile = get_user_profile(st.user.email)
    if st.session_state.profile == None:
        get_new_profile()
    else:
        pages = [
            st.Page("main_window.py", title="Home"),
            st.Page("profile_info.py", title="Profile"),

        ]
        pg = st.navigation(pages, position="top")
        pg.run()
    if st.button('Logout'):
        st.logout()

