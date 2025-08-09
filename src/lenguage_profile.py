import streamlit as st
from requests import options


sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
def main_Program():
    st.title("lenguage profile")
    target_language = st.selectbox("Target Language", options= ["French",  "Japanese"]
                            ,key="target_language"
                            ,index=None)
    base_language = st.selectbox("Base Language", options= ["English", "Spanish", "French"]
                            ,key="base_language"
                            ,index=None)
    if target_language is not None and base_language is not None:
        exam_scope = st.selectbox("Select Examn", options= ["TEF Canada", "TCF Canada", "JLPT"]
                                ,key="exam"
                                ,index=None)



if __name__ == '__main__':
    main_Program()
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://www.example.com/path/to/your/image.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )