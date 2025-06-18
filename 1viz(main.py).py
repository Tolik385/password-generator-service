from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from password_generator import PasswordGenerator

app = FastAPI()

"""настройка статических файлов и шаблонов"""
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

generator = PasswordGenerator()

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/generate")
async def generate_password(length: int = 12, use_symbols: bool = True, use_digits: bool = True):
    password = generator.generate(length)
    strength = generator.estimate_strength(password)
    return {
        "password": password,
        "strength": strength
    }