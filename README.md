# Seguimiento Remates

App para registrar publicaciones de propiedades y autos en remate.

**Stack:** FastAPI + SQLAlchemy + PostgreSQL 17 (más adelante React + Vite).

## Requisitos

- Docker Desktop
- Python 3.12 o superior

## Puesta en marcha

1. Copiar las variables de entorno:

   ```powershell
   Copy-Item .env.example .env
   ```

2. Levantar PostgreSQL (queda en `localhost:5433`):

   ```powershell
   docker compose up -d
   ```

3. Crear el entorno virtual e instalar dependencias:

   ```powershell
   cd backend
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

4. Levantar la API (desde `backend/`):

   ```powershell
   uvicorn app.main:app --reload
   ```

   Probar en <http://localhost:8000/health> o ver la documentación en <http://localhost:8000/docs>.

5. Ejecutar los tests (desde `backend/`):

   ```powershell
   pytest
   ```

## Estructura

```
.
├── docker-compose.yml   # PostgreSQL 17
├── .env.example         # plantilla de variables de entorno
└── backend/
    ├── requirements.txt
    ├── pytest.ini
    ├── app/main.py      # API FastAPI (GET /health)
    └── tests/
```
