from pydantic import BaseModel

class Student(BaseModel):
    name: str
    std: int | None = None
    age: int | None= None
    
