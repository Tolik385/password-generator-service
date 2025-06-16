from fastapi import FastAPI
from utils import PasswordGenerator

app = FastAPI()
generator = PasswordGenerator()

@app.get("/")
def read_root():
    """Основной маршрут для проверки работы сервера"""
    return {"Hello": "World"}

@app.get("/generate")
async def generate_password(length: int = 12):
    """
    Генерация пароля заданной длины
    
    Args:
        length: Длина пароля (по умолчанию 12)
        
    Returns:
        {"password": "сгенерированный_пароль"}
    """
    return {"password": generator.generate(length)}
