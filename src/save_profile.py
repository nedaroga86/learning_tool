import os
import time
import gspread
import streamlit as st


BASE_DIR = os.path.dirname(os.path.abspath(__file__))



scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]



# Abre el spreadsheet por ID


# Guarda perfil
def save_profile(email, target_language, base_language, exam_scope, current_level, goal_level, prep_time):
    creds = st.secrets["gcp_service_account"]
    client = gspread.service_account_from_dict(creds)
    db = client.open_by_key("1pNgSoEpnTEG17j06niCj7_fCUN69DZ-Dl3t4DPk9l5w").sheet1
    db.append_row([email, target_language, base_language, exam_scope,
                      current_level, goal_level, prep_time])

def get_user_profile(email):
    creds = st.secrets["gcp_service_account"]
    st.write(st.secrets["gcp_service_account"]["private_key"])
    client = gspread.service_account_from_dict(creds)
    db = client.open_by_key("1pNgSoEpnTEG17j06niCj7_fCUN69DZ-Dl3t4DPk9l5w").sheet1
    records = db.get_all_records()  # lee toda la hoja
    for row in records:
        if row["email"] == email:
            return row
    return None

