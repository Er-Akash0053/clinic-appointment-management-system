from fastapi import APIRouter

from database import supabase
from schemas import MedicalRecordCreate

router = APIRouter(
    prefix="/records",
    tags=["Medical Records"]
)

@router.post("/")
def create_record(
    record: MedicalRecordCreate
):

    result = (
        supabase.table("medical_records")
        .insert(
            record.model_dump()
        )
        .execute()
    )

    return result.data


@router.get("/")
def get_records():

    result = (
        supabase.table("medical_records")
        .select("*")
        .execute()
    )

    return result.data


@router.delete("/{record_id}")
def delete_record(record_id: str):

    result = (
        supabase.table("medical_records")
        .delete()
        .eq("id", record_id)
        .execute()
    )

    return result.data