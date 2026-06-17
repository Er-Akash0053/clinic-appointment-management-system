from fastapi import APIRouter
from database import supabase
from schemas import DoctorCreate

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)

@router.post("/")
def create_doctor(doctor: DoctorCreate):

    result = (
        supabase.table("doctors")
        .insert(doctor.model_dump())
        .execute()
    )

    return result.data


@router.get("/")
def get_doctors():

    result = (
        supabase.table("doctors")
        .select("*")
        .execute()
    )

    return result.data


@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: str):

    result = (
        supabase.table("doctors")
        .delete()
        .eq("id", doctor_id)
        .execute()
    )

    return result.data