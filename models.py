from enum import unique
from operator import index
from sqlalchemy import  Column, Integer, String, ForeignKey,true
from db import Base
from sqlalchemy.orm import relationship


class user_register(Base):
   
    __tablename__ = "user_register_table"
    id           = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name         = Column(String(255), index=True, nullable=False)
    email        = Column(String(100), index=True, nullable=False,unique=True)
    mobile_no    = Column(String(100), index=True, nullable=False,unique=True)
    user_profile = relationship("user_profile", back_populates="owner")

class user_profile(Base):
    __tablename__=" user_profile_table"
    id           = Column(Integer, primary_key=True, index=True)
    sex          =Column(String(255),index=true,nullable=False)
    dob          =Column(String(255),index=true,nullable=False)
    owner_id     = Column(Integer, ForeignKey("user_register_table.id"))
    owner        = relationship("user_register", back_populates="user_profile")