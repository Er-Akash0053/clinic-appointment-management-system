from fastapi import APIRouter
from fastapi import HTTPException

from database import supabase
from schemas import AppointmentCreate

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)

@router.post("/")
def create_appointment(
    appointment: AppointmentCreate
):

    existing = (
        supabase.table("appointments")
        .select("*")
        .eq(
            "doctor_id",
            appointment.doctor_id
        )
        .eq(
            "appointment_date",
            appointment.appointment_date
        )
        .eq(
            "appointment_time",
            appointment.appointment_time
        )
        .execute()
    )

    if existing.data:

        raise HTTPException(
            status_code=400,
            detail="Slot already booked"
        )

    result = (
        supabase.table("appointments")
        .insert(
            appointment.model_dump()
        )
        .execute()
    )

    return result.data


@router.get("/")
def get_appointments():

    result = (
        supabase.table("appointments")
        .select("*")
        .execute()
    )

    return result.data


@router.delete("/{appointment_id}")
def cancel_appointment(
    appointment_id: str
):

    result = (
        supabase.table("appointments")
        .update(
            {"status": "cancelled"}
        )
        .eq(
            "id",
            appointment_id
        )
        .execute()
    )

    return result.data