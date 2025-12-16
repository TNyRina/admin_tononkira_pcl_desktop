from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.db import Base
from app.repositories.category_repository import CategoryRepository
from .category import song_category

class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    release = Column(String, index=True)
    author = Column(String, index=True)
    composer = Column(String, index=True) 
    description = Column(String, index=True) 
    verse = Column(String, index=True) 
    refrain = Column(String, index=True) 

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relation Many-to-Many avec Categories
    categories = relationship(
        "Category",
        secondary=song_category,
        back_populates="songs"
    )
    
    