from pydantic import BaseModel, Field
from typing import Optional, List

class AnalysisReport(BaseModel):
    sector: str
    report_md: str
    timestamp: str

class ErrorResponse(BaseModel):
    detail: str
