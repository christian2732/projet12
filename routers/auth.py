from fastapi import APIRouter
from app.auth.jwt_handler import create_access_token

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    # ⚠️ Auth simplifiée (à remplacer plus tard par base de données)
    if username == "admin" and password == "secret":
        token = create_access_token({"user": username})
        return {"access_token": token}
    return {"error": "Invalid credentials"}
