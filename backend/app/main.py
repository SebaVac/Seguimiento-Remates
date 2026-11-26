from fastapi import FastAPI

app = FastAPI(title="Seguimiento Remates")


@app.get("/health")
def health() -> dict[str, str]:
    """Indica que la API está viva."""
    return {"status": "ok"}
