from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    token = Column(String, index=True)
