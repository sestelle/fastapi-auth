import jwt

from datetime import datetime

import config as config


def generate_token(email: str) -> str:
    now = datetime.now()

    token = jwt.encode(
        payload={"email": email, "date": now.strftime("%d/%m/%Y %H:%M:%S")},
        key=config.SECRET,
        algorithm="HS256"
    )

    return token
