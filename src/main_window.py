import streamlit as st

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
            text = st.container(border=True)

    text = st.text_area("Prompt", height=200, max_chars=1000, key="input_text", help="Escriba o pegue el texto que desea procesar aquí.")

main_Window()