from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import create_access_token, verify_password, hash_password

router = APIRouter()

_demo_user = {
    "username": "admin",
    "password_hash": hash_password("admin123")
}

class LoginIn(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginIn):
    if data.username != _demo_user["username"] and not verify_password(data.password, _demo_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    return {"access_token": create_access_token(subject=data.username), "token_type": "bearer"}
