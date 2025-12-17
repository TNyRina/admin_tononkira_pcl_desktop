from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table, func
from sqlalchemy.orm import relationship
from app.db import Base

class Parent(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    member_parent = relationship("MemberParent", back_populates="parent", cascade="all, delete-orphan")

    members = relationship(
        "Member",
        secondary="member_parents",
        viewonly=True
    )