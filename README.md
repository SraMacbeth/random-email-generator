# 📧 Random Email Generator - FastAPI Application

Una herramienta web eficiente y ligera diseñada para generar direcciones de correo electrónico aleatorias de forma instantánea. Este proyecto utiliza un backend robusto en Python para gestionar la lógica de generación y una interfaz moderna para la interacción del usuario.

## 📋 Descripción

Esta aplicación permite a los usuarios crear correos electrónicos personalizados basados en diferentes parámetros. Es ideal para pruebas de software, registros temporales o cualquier escenario que requiera una dirección de correo única y rápida.

## 🚀 Funcionalidades

* **Generación Personalizada:** Ajusta la longitud del correo, el dominio y elige si incluir números o caracteres especiales.
* **Backend de Alto Rendimiento:** Construido con **FastAPI**, asegurando respuestas rápidas y un manejo eficiente de las peticiones.
* **Interfaz Dinámica:** Uso de plantillas **Jinja2** y JavaScript asíncrono (`fetch`) para actualizar el resultado sin recargar la página.
* **Copiado con un Clic:** Función integrada para copiar el correo generado directamente al portapapeles.
* **Validación de Parámetros:** Lógica del lado del servidor para asegurar que la longitud y el formato cumplan con los estándares mínimos.

## 🛠️ Tecnologías Utilizadas

* **Python 3.x:** Lenguaje principal del backend.
* **FastAPI:** Framework web moderno y rápido para construir APIs.
* **Jinja2:** Motor de plantillas para renderizar el frontend desde el servidor.
* **Uvicorn:** Servidor ASGI para la ejecución de la aplicación.
* **HTML5 / CSS3 / JavaScript:** Para una interfaz de usuario limpia y funcional.

## 💻 Instalación y Configuración Local

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/SraMacbeth/random-email-generator.git
    cd random-email-generator
    ```

2.  **Crea un entorno virtual (opcional pero recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación:**
    ```bash
    uvicorn main:app --reload
    ```

5.  Abre tu navegador en `http://127.0.0.1:8000`.

## ⚙️ Estructura del Proyecto

* `main.py`: Contiene los endpoints de la API y la lógica de generación aleatoria.
* `templates/`: Directorio que alberga el archivo `index.html` procesado por Jinja2.
* `requirements.txt`: Listado de librerías necesarias para el funcionamiento del proyecto.

---
**Desarrollado por Emilia Poletti** - *Enfoque en Desarrollo Backend y APIs*
