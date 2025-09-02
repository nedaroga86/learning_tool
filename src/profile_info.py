import pandas as pd
import streamlit as st

def show_profile_info():

    tab1, tab2 = st.tabs(["Profile Overview", "Details"])
    with tab1:
        st.success("Image")
        st.write("**Target Language:**", st.session_state.profile["target_language"])
        st.write("**Base Language:**", st.session_state.profile["base_language"])
        st.success("Text Part")
        st.write("**Exam Scope:**", st.session_state.profile["exam_scope"])
        st.write("**Current Level:**", st.session_state.profile["current_level"])
        st.write("**Goal Level:**", st.session_state.profile["goal_level"])
        st.write("**Prep Time (months):**", st.session_state.profile["prep_time"])
    with tab2:
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "70 °F", "1.2 °F")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "86%", "4%")

        data_df = pd.DataFrame(
            {
                "Progress": [30, 40, 35, 80],
            }
        )

        st.data_editor(
            data_df,
            column_config={
                "Progress": st.column_config.ProgressColumn(
                    "Progress",
                    help="The sales volume in USD",
                    format="%.1f %%",
                    min_value=0,
                    max_value=100,
                ),
            },
            hide_index=True,
        )

show_profile_info()