import sys
import os
import click
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from datetime import datetime

def get_db():
    return SessionLocal()

def print_menu(title, options):
    click.secho(f"\n--- {title} ---", fg='green', bold=True)
    for i, option in enumerate(options, 1):
        click.echo(f"{i}. {option}")
    return input("Enter choice: ")

def handle_crud(entity_type, entity_name):
    db = get_db()
    try:
        if entity_type == "view":
            items = db.query(eval(entity_name)).all()
            click.secho(f"\n--- All {entity_name}s ---", fg='blue')
            for item in items:
                click.echo(f"ID: {item.id}, Name: {item.first_name} {item.last_name}")
        elif entity_type == "add":
            if entity_name == "Patient":
                item = Patient(
                    first_name=input("First Name: "),
                    last_name=input("Last Name: "),
                    phone_number=input("Phone: "),
                    email=input("Email: ")
                )
            elif entity_name == "Doctor":
                item = Doctor(
                    first_name=input("First Name: "),
                    last_name=input("Last Name: "),
                    specialty=input("Specialty: "),
                    license_number=input("License: ")
                )
            db.add(item)
            db.commit()
            click.secho(f"{entity_name} added successfully!", fg='green')
        elif entity_type == "delete":
            item_id = int(input(f"Enter {entity_name} ID to delete: "))
            item = db.query(eval(entity_name)).filter(eval(f"{entity_name}.id == {item_id}")).first()
            if item:
                db.delete(item)
                db.commit()
                click.secho(f"{entity_name} deleted successfully!", fg='yellow')
            else:
                click.secho("Not found!", fg='red')
    except Exception as e:
        click.secho(f"Error: {e}", fg='red')
        db.rollback()
    finally:
        db.close()

def patient_management():
    while True:
        choice = print_menu("Patient Management", 
            ["View All", "Add New", "Delete", "Back"])
        if choice == "1": handle_crud("view", "Patient")
        elif choice == "2": handle_crud("add", "Patient")
        elif choice == "3": handle_crud("delete", "Patient")
        elif choice == "4": break
        else: click.secho("Invalid choice", fg='red')

def doctor_management():
    while True:
        choice = print_menu("Doctor Management", 
            ["View All", "Add New", "Delete", "Back"])
        if choice == "1": handle_crud("view", "Doctor")
        elif choice == "2": handle_crud("add", "Doctor")
        elif choice == "3": handle_crud("delete", "Doctor")
        elif choice == "4": break
        else: click.secho("Invalid choice", fg='red')

def appointment_management():
    db = get_db()
    try:
        choice = print_menu("Appointment Management", 
            ["View All", "Create New", "Back"])
        if choice == "1":
            appointments = db.query(Appointment).all()
            click.secho("\n--- All Appointments ---", fg='blue')
            for appt in appointments:
                click.echo(f"ID: {appt.id}, Patient: {appt.patient_id}, Doctor: {appt.doctor_id}, When: {appt.appointment_date}")
        elif choice == "2":
            appointment = Appointment(
                patient_id=int(input("Patient ID: ")),
                doctor_id=int(input("Doctor ID: ")),
                appointment_date=datetime.strptime(input("Date (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M"),
                status="Scheduled"
            )
            db.add(appointment)
            db.commit()
            click.secho("Appointment created!", fg='green')
        elif choice == "3": return
        else: click.secho("Invalid choice", fg='red')
    except Exception as e:
        click.secho(f"Error: {e}", fg='red')
        db.rollback()
    finally:
        db.close()

def main():
    click.secho("Welcome to my Clinic Management System!", fg='cyan', bold=True)
    while True:
        choice = print_menu("Main Menu", 
            ["Patient Management", "Doctor Management", "Appointment Management", "Exit"])
        if choice == "1": patient_management()
        elif choice == "2": doctor_management()
        elif choice == "3": appointment_management()
        elif choice == "4": 
            click.secho("Chao!", fg='magenta')
            break
        else: click.secho("Invalid choice", fg='red')

if __name__ == "__main__":
    main()
