import os
import streamlit as st
import pandas as pd
from save_profile import save_profile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
examns_df = os.path.join(BASE_DIR, '..', 'data','exam_types.pkl')


def get_new_profile():
    st.title("Language profile")
    target_language = st.selectbox("Target Language", options= ["French",  "Japanese"]
                            ,key="target_language"
                            ,index=None)
    base_language = st.selectbox("Base Language", options= ["English", "Spanish", "French"]
                            ,key="base_language"
                            ,index=None)
    if target_language is not None and base_language is not None:
        examen_df = pd.read_pickle(examns_df)
        filtered_exams = examen_df[(examen_df['Language'] == target_language)
        ]

        exam_scope = st.selectbox("Select Exam", options= filtered_exams['Examen'].unique()
                                 ,key="exam"
                                 ,index=None)

        if exam_scope is not None:
            level = filtered_exams[(filtered_exams['Examen'] == exam_scope)]['Levels'].unique()

            col, col2 = st.columns(2)
            with col:
                current_level = st.selectbox("Current Level", options= level
                                          ,key="cur_level"
                                          ,index=None)
                if current_level is not None:
                    index_value = filtered_exams[(filtered_exams['Levels'] == current_level)]['Levels'].index[0]
                    goal_levels = filtered_exams[(filtered_exams['Examen'] == exam_scope)&(filtered_exams.index > index_value)]['Levels'].unique()
                    with col2:
                        goal_level = st.selectbox("Goal Level", options= goal_levels
                                                 ,key="goal_level"
                                                 ,index=None)

            if current_level is not None and goal_level is not None:
                prep_time = st.slider("Preparation Time (in months)", min_value=1, max_value=12, value=3, step=1)

    if st.button("Save Profile"):
        email = st.user.email
        #save_profile(email, target_language, base_language, exam_scope, current_level, goal_level, prep_time)




if __name__ == '__main__':
    get_new_profile()
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