from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from auth import decode_token

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    )
):

    token = credentials.credentials

    payload = decode_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload