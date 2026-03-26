from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./veterinary.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Animal(Base):
    __tablename__ = "animals"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    species = Column(String)  # "dog", "cat", etc.
    owner_name = Column(String)
    owner_phone = Column(String)

class VitalSign(Base):
    __tablename__ = "vitals"
    
    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer)
    temperature = Column(Float)  # °C
    heart_rate = Column(Integer) # bpm
    symptoms = Column(String)    # "vomiting, lethargy"
    timestamp = Column(DateTime, default=datetime.utcnow)

# Crea il database
Base.metadata.create_all(bind=engine)
