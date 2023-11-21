from pydantic import BaseModel

class MessageRequestSchema(BaseModel):
    user : str
    locale : str
    type : str
    text : str

class CreateRequestSchema(BaseModel):
    user:str