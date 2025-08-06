from pydantic import BaseModel, Field

class ComplianceAssessment(BaseModel):
    compliance_status: int = Field(..., description="0: met, 1: partially met, 2: not met", ge=0, le=2)
    evidence: str = Field("", description="Cited segment from the policy supporting the compliance status claim.")
    missing_elements: str = Field("", description="Reference to missing requirement for partially/not met; empty if met.")
    amendments: str = Field("", description="Suggestions to meet the requirement for partially/not met; empty if met.")
