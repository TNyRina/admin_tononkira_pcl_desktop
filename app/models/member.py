from sqlalchemy import Column, Date, DateTime, Integer, String, func
from sqlalchemy.orm import relationship
from app.db import Base

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True, nullable=False)
    lastname = Column(String, index=True, nullable=False)
    sexe = Column(String, nullable=False)
    data_of_birth = Column(Date, nullable=False)
    image_url = Column(String, nullable=True)
    address = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    member_parent = relationship("MemberParent", back_populates="member")

    parents = relationship(
        "Parent",
        secondary="member_parents",
        viewonly=True
    )