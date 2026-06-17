from fastapi import FastAPI

from auth_router import router as auth_router
from doctor_router import router as doctor_router
from appointment_router import router as appointment_router
from medical_record_router import router as medical_record_router

app = FastAPI(
    title="Clinic Appointment Management System",
    version="1.0.0",
    description="Clinic Appointment Management API using FastAPI, JWT and Supabase"
)

app.include_router(auth_router)
app.include_router(doctor_router)
app.include_router(appointment_router)
app.include_router(medical_record_router)


@app.get("/")
def home():
    return {
        "message": "Clinic Appointment Management System Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }