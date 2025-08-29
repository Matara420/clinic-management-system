import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from datetime import datetime, timedelta

def create_sample_data():
    db = SessionLocal()
    
    try:
        # Clear existing data first
        db.query(Appointment).delete()
        db.query(Patient).delete()
        db.query(Doctor).delete()
        db.commit()
        
        patients = [
            Patient(
                first_name="John", 
                last_name="Doe", 
                phone_number="555-0101", 
                email="john.doe@email.com"
            ),
            Patient(
                first_name="Jane", 
                last_name="Smith", 
                phone_number="555-0102", 
                email="jane.smith@email.com"
            ),
            Patient(
                first_name="Michael", 
                last_name="Brown", 
                phone_number="555-0103", 
                email="michael.b@email.com"
            )
        ]
        
        doctors = [
            Doctor(
                first_name="Sarah", 
                last_name="Wilson", 
                specialty="Cardiology", 
                license_number="DR-001"
            ),
            Doctor(
                first_name="David", 
                last_name="Chen", 
                specialty="Pediatrics", 
                license_number="DR-002"
            ),
            Doctor(
                first_name="Emily", 
                last_name="Rodriguez", 
                specialty="Dermatology", 
                license_number="DR-003"
            )
        ]
        
        db.add_all(patients)
        db.add_all(doctors)
        db.commit()
        
        appointments = [
            Appointment(
                patient_id=1,
                doctor_id=1,
                appointment_date=datetime.now() + timedelta(days=2),
                status="Scheduled"
            ),
            Appointment(
                patient_id=2,
                doctor_id=2,
                appointment_date=datetime.now() + timedelta(days=3),
                status="Confirmed"
            ),
            Appointment(
                patient_id=3,
                doctor_id=3,
                appointment_date=datetime.now() + timedelta(days=1),
                status="Scheduled"
            )
        ]
        
        db.add_all(appointments)
        db.commit()
        
        print("Sample data added successfully!")
        
    except Exception as e:
        print(f"Error creating sample data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_data()
    print("Database seeded with sample data!")