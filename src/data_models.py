from pydantic import BaseModel
from typing import List, Optional

class TreatmentPlanInputs(BaseModel):
    patient_name: str
    age: int
    gender: str
    contact_info: str
    malocclusion_type: str
    crowding: Optional[str] = ""
    spacing: Optional[str] = ""
    bite_issues: Optional[str] = ""
    tmj_issues: Optional[str] = ""
    additional_findings: Optional[str] = ""
    treatment_goals: List[str]
