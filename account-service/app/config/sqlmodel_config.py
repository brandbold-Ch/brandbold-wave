from sqlmodel import create_engine, SQLModel, Session
from flask import g
from sqlalchemy.schema import CreateTable
from app.models import *
from app.utils.settings import get_settings

settings = get_settings()

engine = create_engine(settings.postgres_internal_url, echo=False)
SQLModel.metadata.create_all(engine)


def create_session() -> Session:
    return Session(engine)


def db () -> Session:
    if "session" not in g:
        g.session = create_session()
    return g.session


#for table in SQLModel.metadata.tables.values():
#   print(str(CreateTable(table).compile(engine)))
