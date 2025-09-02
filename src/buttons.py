import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def loggin_button(key, color="#eea399", typeB="sidebar"):
    with stylable_container(
            key="green_button",
            css_styles=f"""
                button {{
                    background-color: {color};
                    color: black;
                    border-radius:4px;
                }}
                """,
    ):  new = st.button(key,  use_container_width=False, key=key)
    return new
