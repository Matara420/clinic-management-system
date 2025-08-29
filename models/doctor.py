from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Doctor(Base):
    __tablename__ = 'doctors'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    license_number = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    
    appointments = relationship("Appointment", back_populates="doctor")
    
    def __repr__(self):
        return f"<Doctor {self.first_name} {self.last_name} ({self.specialty})>"