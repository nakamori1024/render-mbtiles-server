from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "name": "Render MBTiles Server",
        "version": "0.1.0",
        "endpoints": {
            "/docs": "Swagger UI",
            "/health": "Check the health of the server",
        },
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
