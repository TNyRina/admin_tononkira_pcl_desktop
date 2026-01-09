from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db import Base

# Table d'association
song_category = Table(
    'song_category',
    Base.metadata,
    Column('song_id', Integer, ForeignKey('songs.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True)
)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relation Many-to-Many avec Songs
    songs = relationship(
        "Song",
        secondary=song_category,
        back_populates="categories",
        passive_deletes=True
    )
