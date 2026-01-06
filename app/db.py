from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import DATABASE_URL

# Création du moteur de base de données
engine = create_engine(DATABASE_URL, echo=False)

# Création de la session locale
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base déclarative pour les modèles
Base = declarative_base()
 