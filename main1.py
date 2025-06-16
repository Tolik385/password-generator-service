from fastapi import FastAPI
from utils import PasswordGenerator

app = FastAPI()
generator = PasswordGenerator()

@app.get("/generate")
async def generate_password(length: int = 12):
    """генерация пароля зад длины"""
    return {"password": generator.generate(length)}