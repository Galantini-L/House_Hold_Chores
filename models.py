from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime
from db import engine
from sqlalchemy.orm import sessionmaker

#Para crear un model la clase "taskitem" debe heredar esta clase
Base = declarative_base()

class tasksItems(Base):
    __tablename__ = 'tasks'
    id = Column(Integer(),primary_key=True)
    name = Column(String(60), nullable=False)
    compleate = Column(Boolean,default=False)
    created_at = Column(DateTime, default=datetime.now())
    
Base.metadata.create_all(engine)