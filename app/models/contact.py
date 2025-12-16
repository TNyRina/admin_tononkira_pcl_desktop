from sqlalchemy import Column, Integer, String
from app.db import Base


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    contact = Column(String, index=True, nullable=False)
    owner = Column(Integer, nullable=False)