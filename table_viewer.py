import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment

def print_table(title, headers, data):
    print(f"\n{title}")
    print("-" * 80)
    
    header_row = " | ".join(f"{h:15}" for h in headers)
    print(f"| {header_row} |")
    print("-" * 80)
    
    for row in data:
        data_row = " | ".join(f"{str(value):15}" for value in row)
        print(f"| {data_row} |")
    
    print("-" * 80)
    print(f"Rows: {len(data)}")

def view_patients_table():
    db = SessionLocal()
    patients = db.query(Patient).all()
    
    headers = ["ID", "First Name", "Last Name", "Phone", "Email", "Created At"]
    data = []
    
    for p in patients:
        data.append([
            p.id,
            p.first_name,
            p.last_name,
            p.phone_number,
            p.email,
            p.created_at.strftime("%Y-%m-%d %H:%M") if p.created_at else "N/A"
        ])
    
    print_table("PATIENTS TABLE", headers, data)
    db.close()

def view_doctors_table():
    db = SessionLocal()
    doctors = db.query(Doctor).all()
    
    headers = ["ID", "First Name", "Last Name", "Specialty", "License", "Created At"]
    data = []
    
    for d in doctors:
        data.append([
            d.id,
            d.first_name,
            d.last_name,
            d.specialty,
            d.license_number,
            d.created_at.strftime("%Y-%m-%d %H:%M") if d.created_at else "N/A"
        ])
    
    print_table("DOCTORS TABLE", headers, data)
    db.close()

def view_appointments_table():
    db = SessionLocal()
    appointments = db.query(Appointment).all()
    
    headers = ["ID", "Patient ID", "Doctor ID", "Appointment Date", "Status", "Created At"]
    data = []
    
    for a in appointments:
        data.append([
            a.id,
            a.patient_id,
            a.doctor_id,
            a.appointment_date.strftime("%Y-%m-%d %H:%M") if a.appointment_date else "N/A",
            a.status,
            a.created_at.strftime("%Y-%m-%d %H:%M") if a.created_at else "N/A"
        ])
    
    print_table("APPOINTMENTS TABLE", headers, data)
    db.close()

if __name__ == "__main__":
    view_patients_table()
    view_doctors_table()
    view_appointments_table()
