import streamlit as st
from src.utils import gather_treatment_goals, create_treatment_plan_inputs

def render_sidebar() -> dict:
    st.sidebar.header("Patient Information")
    
    # Patient Information Inputs
    patient_name = st.sidebar.text_input("Patient Name", "")
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=15)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
    contact_info = st.sidebar.text_input("Contact Information", "")
    
    st.sidebar.header("Clinical Findings")
    
    # Clinical Findings Inputs
    malocclusion_type = st.sidebar.selectbox(
        "Type of Malocclusion",
        ["Class I", "Class II Division 1", "Class II Division 2", "Class III"]
    )
    crowding = st.sidebar.text_input("Crowding Details", "")
    spacing = st.sidebar.text_input("Spacing Details", "")
    bite_issues = st.sidebar.text_area("Bite Issues (e.g., overbite, underbite)", "")
    tmj_issues = st.sidebar.text_area("TMJ Issues", "")
    additional_findings = st.sidebar.text_area("Additional Clinical Findings", "")
    
    st.sidebar.header("Treatment Goals")
    
    # Treatment Goals Inputs
    goal_alignment = st.sidebar.checkbox("Improve dental alignment")
    goal_occlusion = st.sidebar.checkbox("Correct occlusion")
    goal_aesthetics = st.sidebar.checkbox("Enhance aesthetics")
    goal_function = st.sidebar.checkbox("Improve functional aspects")
    goal_other = st.sidebar.text_input("Other Goals", "")
    
    # Optional Settings
    st.sidebar.header("Settings")
    temperature = st.sidebar.slider("OpenAI Temperature", 0.0, 1.0, 0.7)
    max_tokens = st.sidebar.slider("Max Tokens", 100, 2000, 1000, step=100)
    
    # Gather treatment goals
    treatment_goals = gather_treatment_goals(
        goal_alignment, goal_occlusion, goal_aesthetics, goal_function, goal_other
    )
    
    # Compile all inputs into a dictionary
    user_inputs = {
        "patient_name": patient_name,
        "age": age,
        "gender": gender,
        "contact_info": contact_info,
        "malocclusion_type": malocclusion_type,
        "crowding": crowding,
        "spacing": spacing,
        "bite_issues": bite_issues,
        "tmj_issues": tmj_issues,
        "additional_findings": additional_findings,
        "treatment_goals": treatment_goals,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    
    return user_inputs
