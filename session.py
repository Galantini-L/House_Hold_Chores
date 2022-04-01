from sqlalchemy.orm.session import sessionmaker
from db import engine

Session = sessionmaker(engine)
session = Session()

