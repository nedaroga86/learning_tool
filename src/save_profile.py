import os

import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_file =  os.path.join(BASE_DIR, '..', '.streamlit','service_account.json')


scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

creds = st.secrets["gcp_service_account"]
client = gspread.service_account_from_dict(creds)

# Abre el spreadsheet por ID
db = client.open_by_key("1pNgSoEpnTEG17j06niCj7_fCUN69DZ-Dl3t4DPk9l5w").sheet1

# Guarda perfil
def save_profile(email, target_language, base_language, exam_scope, current_level, goal_level, prep_time):
    db.append_row([email, target_language, base_language, exam_scope,
                      current_level, goal_level, prep_time])

def get_user_profile(email):
    records = db.get_all_records()  # lee toda la hoja
    for row in records:
        if row["email"] == email:
            return row
    return None

