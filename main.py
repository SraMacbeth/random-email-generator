import string
import random
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Setup Jinja2 to look for templates in the 'templates' folder
templates = Jinja2Templates(directory="templates")

def generate_random_email(
    length: int = 10,
    domain: str = "randommail.io",
    include_numbers: bool = True,
    include_special_chars: bool = False
):
    characters = string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += "!#%&*" # Common safe characters for emails
    
    if length < 5:
        length = 5

    user = ''.join(random.choices(characters, k=length))
    return f"{user}@{domain}"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/generate")
def get_email(
    length: int = 10,
    domain: str = "randommail.io",
    include_numbers: bool = True,
    include_special_chars: bool = False
):
    email = generate_random_email(length, domain, include_numbers, include_special_chars)
    return {"email": email}