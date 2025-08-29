from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///clinic.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    
    from models.patient import Patient
    from models.doctor import Doctor
    from models.appointment import Appointment
    Base.metadata.create_all(bind=engine)