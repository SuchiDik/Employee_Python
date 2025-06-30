# Pydantic schemas

from pydantic import BaseModel,EmailStr
class EmployeeBase(BaseModel):
    name:str
    dept:str
    email:EmailStr


class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id:int

    class Config:
        orm_mode = True