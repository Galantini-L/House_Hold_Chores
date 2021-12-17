from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import sessionmaker
from db import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
session = Session()

