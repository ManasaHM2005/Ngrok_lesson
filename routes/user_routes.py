from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from repositories.user_repo import UserRepository
from schemas.user_schemas import UserCreate

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return user_repo.create_user(user)

@router.get("/users/{user_id}", response_model=UserCreate)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user = user_repo.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/", response_model=list[UserCreate])
def get_users(db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return user_repo.get_users()

