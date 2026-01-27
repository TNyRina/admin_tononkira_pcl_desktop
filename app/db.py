from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import Engine
import sqlite3
from .config import DATABASE_URL

# Création du moteur de base de données
engine = create_engine(DATABASE_URL, echo=False)

# Création de la session locale
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base déclarative pour les modèles
Base = declarative_base()

@event.listens_for(Engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


from app.models.category import song_category

song_category.create(bind=engine, checkfirst=True)