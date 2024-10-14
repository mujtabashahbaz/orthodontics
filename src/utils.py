from src.data_models import TreatmentPlanInputs
import openai
from src.config import Config

def generate_treatment_plan_with_settings(inputs: TreatmentPlanInputs, temperature: float, max_tokens: int) -> str:
    prompt = f"""
    You are an experienced orthodontist. Based on the following patient information, clinical findings, and treatment goals, provide a comprehensive treatment plan.

    Patient Information:
    Name: {inputs.patient_name}
    Age: {inputs.age}
    Gender: {inputs.gender}
    Contact: {inputs.contact_info}

    Clinical Findings:
    Malocclusion Type: {inputs.malocclusion_type}
    Crowding: {inputs.crowding}
    Spacing: {inputs.spacing}
    Bite Issues: {inputs.bite_issues}
    TMJ Issues: {inputs.tmj_issues}
    Additional Findings: {inputs.additional_findings}

    Treatment Goals:
    {', '.join(inputs.treatment_goals)}

    Treatment Plan:
    """

    response = openai.Completion.create(
        engine=Config.OPENAI_MODEL,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
        stop=None,
    )
    treatment_plan = response.choices[0].text.strip()
    return treatment_plan
