from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud as crud
import schemas as schemas

from database import get_db

router = APIRouter()

secret = "pR9ZbccoRF3VS5w87QYDrWtEaCvO2s4vv2vgX9Ptg=="


@router.post("/authentication/", response_model=schemas.ResponseSchema)
def authentication(user: schemas.UserAuthentication, db: Session = Depends(get_db)) -> schemas.ResponseSchema:
    token = crud.create_token(db=db, email=user.email, password=user.password)

    return schemas.ResponseSchema(
        message=token
    )


@router.post("/authorization/", response_model=schemas.ResponseSchema)
def authorization(token: schemas.Token, db: Session = Depends(get_db)) -> schemas.ResponseSchema:
    if crud.check_token(db=db, token=token.token):
        return schemas.ResponseSchema(
            message="Success"
        )

    return schemas.ResponseSchema(
        message="Error"
    )


@router.post("/registration/", response_model=schemas.ResponseSchema)
def registration(user: schemas.UserAuthentication, db: Session = Depends(get_db)) -> schemas.ResponseSchema:
    if crud.create_user(db=db, email=user.email, password=user.password):
        return schemas.ResponseSchema(
            message="User has been registered"
        )

    return schemas.ResponseSchema(
        message="Email already registered"
    )
