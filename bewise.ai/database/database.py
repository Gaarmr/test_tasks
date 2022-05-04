from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'db.sqlite'

engin = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engin)

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engin)