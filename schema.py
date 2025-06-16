from pydantic import BaseModel

class PasswordResponse(BaseModel):
    """модель ответа с паролем"""
    password: str