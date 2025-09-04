from google import genai
import streamlit as st

key =  st.secrets["gemini_conf"]["api_key"]

def call_gemini(prompt):

    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    if response.text:
        return response.text
    else:
        return "No response from Gemini API"


text = call_gemini("Escribe un poema sobre la inteligencia artificial en español.")
