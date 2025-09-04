import streamlit as st

from src.gemini_assistant import call_gemini


def main_Window():
    st.title("Main Window")
    st.write("This is the main window of the application.")
    # Add more UI components and logic as needed
    menu_options = ["Main","Profile", 'Logout']


    ai_container = st.container(border=True, height=400)
    with ai_container:
        col1, col2 = st.columns([2,4])
        with col1:
            image = st.container(border=True)
        with col2:
            if 'gemini' not in st.session_state:
                st.session_state.gemini = "Gemini's response will appear here."
            else:
                st.session_state.gemini = st.container(border=True)

    text = st.text_area("Prompt", height=200, max_chars=1000, key="input_text", help="ready to hear from you")
    if st.button("Submit"):
        st.session_state.gemini =  call_gemini(text)
        st.rerun()

main_Window()