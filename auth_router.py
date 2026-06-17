from fastapi import APIRouter
from fastapi import HTTPException

from database import supabase

from schemas import UserRegister
from schemas import UserLogin

from auth import hash_password
from auth import verify_password
from auth import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserRegister):

    existing = (
        supabase.table("users")
        .select("*")
        .eq("email", user.email)
        .execute()
    )

    if existing.data:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hash_password(
            user.password
        )
    }

    result = (
        supabase.table("users")
        .insert(new_user)
        .execute()
    )

    return {
        "message": "User Registered",
        "data": result.data
    }


@router.post("/login")
def login(user: UserLogin):

    result = (
        supabase.table("users")
        .select("*")
        .eq("email", user.email)
        .execute()
    )

    if not result.data:

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    db_user = result.data[0]

    if not verify_password(
        user.password,
        db_user["password"]
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    token = create_access_token(
        {
            "sub": db_user["id"],
            "email": db_user["email"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }