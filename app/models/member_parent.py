from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base


class MemberParent(Base):   
    __tablename__ = 'member_parents'

    member_id = Column(Integer, ForeignKey('members.id'), primary_key=True)
    parent_id = Column(Integer, ForeignKey('parents.id'), primary_key=True)

    role = Column(String, nullable=True)  


    member = relationship("Member", back_populates="member_parent")
    parent = relationship("Parent", back_populates="member_parent")


    