from datetime import datetime
from email.policy import default
from sqlalchemy import Column, Boolean, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from db import engine

#Para crear un model la clase "taskItem" debe heredar esta clase
Base = declarative_base()

class tasksItems(Base):
    __tablename__ = 'tasks'
    id = Column(Integer,primary_key=True)
    name = Column(String(60), nullable=False)
    compleate = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())

Base.metadata.create_all(engine)