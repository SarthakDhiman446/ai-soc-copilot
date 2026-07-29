from typing import List

from pydantic import BaseModel


class AIReport(BaseModel):
    executive_summary: str
    attack_type: str
    severity: str
    mitre: List[str]
    impact: str
    recommendations: List[str]
    containment_steps: List[str]