from db import Base
from sqlalchemy import Column,Integer,String,DateTime,Text
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,index=True)
    password=Column(String)
    api_key=Column(String)
    name=Column(String)

class Address(Base):
    __tablename__="addresses"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,index=True)
    address=Column(String,index=True)
    city=Column(String,index=True)
    state=Column(String,index=True)
    zip_code=Column(String,index=True)