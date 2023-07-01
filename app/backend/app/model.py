from sqlalchemy import Column, TIMESTAMP, Integer, String,Text
from sqlalchemy.ext.declarative import declarative_base
from main import engine
Base = declarative_base(bind=engine)
class User(Base):
    __tablename__ = "users"
    __table_args__ = {"autoload": True}
    id = Column(Integer, primary_key = True, nullable=False)
    name = Column(Text, nullable=False)
    password = Column(Text,nullable=False)
