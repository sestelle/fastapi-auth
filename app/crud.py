from sqlalchemy.orm import Session
from sqlalchemy import and_

import models as models
import utils as utils


def create_user(db: Session, email: str, password: str) -> bool:
    if db.query(models.User.email).filter(models.User.email == email).first():
        return False

    db_user = models.User(email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return True


def check_token(db: Session, token: str) -> bool:
    if db.query(models.Token.token).filter(token == models.Token.token).first():
        return True

    return False


def create_token(db: Session, email: str, password: str) -> str:
    db_user = db.query(models.User.id).filter(and_(models.User.email == email,
                                                   models.User.password == password)).first()

    if db_user:
        token = utils.generate_token(email=email)

        db_token = models.Token(token=token, user_id=db_user.id)
        db.add(db_token)
        db.commit()
        db.refresh(db_token)

        return token

    return "Error"

