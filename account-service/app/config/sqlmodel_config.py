"""
SQLModel configuration module.
Initializes the database engine, session, and provides session management utilities for the application.
"""
from sqlmodel import create_engine, SQLModel, Session
from flask import g
from sqlalchemy.schema import CreateTable
from app.models import *
from app.utils.settings import get_settings


settings = get_settings()
engine = create_engine(settings.postgres_local_url, echo=False)
SQLModel.metadata.create_all(engine)


def create_session() -> Session:
    """
    Create a new SQLModel session using the configured engine.
    Returns:
        Session: A new SQLModel session.
    """
    return Session(engine)


def db () -> Session:
    """
    Get or create a session for the current Flask request context.
    Returns:
        Session: The session associated with the current request.
    """
    if "session" not in g:
        g.session = create_session()
    return g.session


#for table in SQLModel.metadata.tables.values():
#   print(str(CreateTable(table).compile(engine)))
