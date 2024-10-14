import streamlit as st
from src.config import Config
from src.components.sidebar import render_sidebar
from src.components.main_display import render_main_display
from src.openai_integration import generate_treatment_plan
import logging

# Initialize logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    st.set_page_config(page_title="Orthodontic Treatment Planner", layout="wide")
    st.title("Comprehensive Orthodontic Treatment Planner")
    
    # Render Sidebar and get user inputs
    user_inputs = render_sidebar()
    
    # Display Input Summary
    render_main_display(user_inputs)
    
    # Generate Treatment Plan
    if st.button("Generate Treatment Plan"):
        with st.spinner("Generating treatment plan..."):
            try:
                plan = generate_treatment_plan(user_inputs)
                st.subheader("Generated Treatment Plan")
                st.write(plan)
                
                # Option to download the treatment plan
                st.download_button(
                    label="Download Treatment Plan",
                    data=plan,
                    file_name=f"{user_inputs['patient_name']}_treatment_plan.txt",
                    mime="text/plain",
                )
                logging.info(f"Treatment plan generated for {user_inputs['patient_name']}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
                logging.error(f"Error generating treatment plan: {e}")

if __name__ == "__main__":
    main()
