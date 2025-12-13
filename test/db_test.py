from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base
from app.models import Category, Song

# Base en mémoire
engine = create_engine("sqlite:///:memory:", echo=True)
TestingSessionLocal = sessionmaker(bind=engine)

# Créer les tables pour les tests
Base.metadata.create_all(bind=engine)
