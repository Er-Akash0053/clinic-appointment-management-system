# Clinic Appointment Management System

A FastAPI-based healthcare management system that enables patient registration, doctor scheduling, appointment booking, and medical record management using JWT Authentication and Supabase.

## Features

* User Registration and Login
* JWT Authentication
* Doctor Management
* Appointment Scheduling
* Medical Record Management
* Prevent Double Booking
* Supabase Integration

## Tech Stack

* FastAPI
* Python
* Supabase
* PostgreSQL
* JWT Authentication

## API Endpoints

### Authentication

* POST /auth/register
* POST /auth/login

### Doctors

* POST /doctors
* GET /doctors
* DELETE /doctors/{id}

### Appointments

* POST /appointments
* GET /appointments
* DELETE /appointments/{id}

### Medical Records

* POST /records
* GET /records
* DELETE /records/{id}

## Installation

```bash
git clone https://github.com/Er-Akash0053/clinic-appointment-management-system.git

cd clinic-appointment-management-system

pip install -r requirements.txt

uvicorn main:app --reload
```

## Documentation

Open:

http://127.0.0.1:8000/docs
