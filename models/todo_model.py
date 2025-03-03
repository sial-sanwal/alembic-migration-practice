from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class todo(Base):
    __tablename__='todo'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True)
    discription=Column(String,nullable=True)
    completed=Column(Boolean,default=False)
    task_done=Column(Boolean,default=False)
    
    __tablename__='student'
    id=Column(Integer,primary_key=True,index=True)
    Name=Column(String,index=True)
    Standard=Column(String,nullable=True)
    completed=Column(Boolean,default=False)