from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    experience: int


class DoctorUpdate(BaseModel):
    name: str
    specialization: str
    experience: int
    available: bool


class AppointmentCreate(BaseModel):
    patient_id: str
    doctor_id: str
    appointment_date: str
    appointment_time: str


class AppointmentUpdate(BaseModel):
    status: str


class MedicalRecordCreate(BaseModel):
    patient_id: str
    doctor_id: str
    diagnosis: str
    prescription: str
    notes: str


class MedicalRecordUpdate(BaseModel):
    diagnosis: str
    prescription: str
    notes: str