from pydantic import BaseModel


# Defining pydantic model class so that the endpoint can accept data for work
class SummarizeRequest(BaseModel):
    text: str
