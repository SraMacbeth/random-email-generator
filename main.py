# Importa el módulo 'string' que contiene colecciones de caracteres útiles como letras, dígitos y puntuación
import string

# Importa el módulo 'random' para generar valores aleatorios
import random

# Importa FastAPI (el framework) y Request (para manejar datos de la petición HTTP)
from fastapi import FastAPI, Request

# Importa HTMLResponse para poder devolver páginas HTML como respuesta
from fastapi.responses import HTMLResponse

# Importa Jinja2Templates para renderizar plantillas HTML dinámicas
from fastapi.templating import Jinja2Templates

# Crea la instancia principal de la aplicación FastAPI
app = FastAPI()

# Le indica a Jinja2 dónde buscar los archivos de plantilla HTML
templates = Jinja2Templates(directory="templates")


def generate_random_email(
    length: int = 10,               # Longitud del nombre de usuario (por defecto 10)
    domain: str = "randommail.io",  # Dominio del correo (por defecto "randommail.io")
    include_numbers: bool = True,   # Si se incluyen números en el usuario
    include_special_chars: bool = False  # Si se incluyen caracteres especiales
):
    # Comienza con solo letras minúsculas como caracteres válidos
    characters = string.ascii_lowercase

    # Si se pidió incluir números, los agrega al conjunto de caracteres
    if include_numbers:
        characters += string.digits

    # Si se pidió incluir caracteres especiales, agrega algunos seguros para emails
    if include_special_chars:
        characters += "!#%&*"

    # Evita que el usuario sea demasiado corto (mínimo 5 caracteres)
    if length < 5:
        length = 5

    # Genera el nombre de usuario eligiendo 'length' caracteres al azar del conjunto
    user = ''.join(random.choices(characters, k=length))

    # Devuelve el email completo en formato usuario@dominio
    return f"{user}@{domain}"


# Define la ruta raíz "/" que responde con una página HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Renderiza y devuelve la plantilla 'index.html', pasándole el objeto request
    # (Jinja2 lo requiere para construir URLs y contexto interno)
    return templates.TemplateResponse("index.html", {"request": request})


# Define la ruta "/generate" que devuelve un email aleatorio en formato JSON
@app.get("/generate")
def get_email(
    length: int = 10,               # Parámetro de query: longitud del usuario
    domain: str = "randommail.io",  # Parámetro de query: dominio del correo
    include_numbers: bool = True,   # Parámetro de query: incluir números
    include_special_chars: bool = False  # Parámetro de query: incluir especiales
):
    # Llama a la función generadora con los parámetros recibidos en la URL
    email = generate_random_email(length, domain, include_numbers, include_special_chars)

    # Devuelve el email generado como un objeto JSON: {"email": "abc123@randommail.io"}
    return {"email": email}