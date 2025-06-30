# SQLAlchemy models
from sqlalchemy import *
from database import Base

class Employee(Base):
    __tablename__ ="employees"

    id=Column(Integer, primary_key=True,index=True)
    name=Column(String,index=True)
    dept=Column(String,index=True)
    email=Column(String,unique=True,index=True)