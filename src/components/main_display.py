import streamlit as st
import pandas as pd
from src.utils import create_treatment_plan_inputs

def render_main_display(user_inputs: dict):
    st.header("Input Summary")
    
    # Display Patient Information
    st.subheader("Patient Information")
    patient_data = {
        "Name": user_inputs["patient_name"],
        "Age": user_inputs["age"],
        "Gender": user_inputs["gender"],
        "Contact": user_inputs["contact_info"]
    }
    st.table(pd.DataFrame(patient_data, index=[0]))
    
    # Display Clinical Findings
    st.subheader("Clinical Findings")
    clinical_data = {
        "Malocclusion Type": user_inputs["malocclusion_type"],
        "Crowding": user_inputs["crowding"],
        "Spacing": user_inputs["spacing"],
        "Bite Issues": user_inputs["bite_issues"],
        "TMJ Issues": user_inputs["tmj_issues"],
        "Additional Findings": user_inputs["additional_findings"]
    }
    st.table(pd.DataFrame(clinical_data, index=[0]))
    
    # Display Treatment Goals
    st.subheader("Treatment Goals")
    goals = user_inputs["treatment_goals"]
    if goals:
        st.markdown("- " + "\n- ".join(goals))
    else:
        st.write("No treatment goals specified.")
