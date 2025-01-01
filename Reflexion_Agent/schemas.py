from typing import List

from pydantic import BaseModel, Field

class Reflection(BaseModel):
    missing:str = Field(description="Critique on what is missing in the answer")
    superfluous:str = Field(description="Critique on what is superfluous in the answer")



class AnswerQuestion(BaseModel):
    """Answer the question."""

    answer:str = Field(description="250 detailed answer to the question.")
    reflection:Reflection = Field(description="Your reflection on the initial answer.")
    # search_queries: List[str] = Field(description="1-3 search queries for researching improvements to address the critique of your current answer.")