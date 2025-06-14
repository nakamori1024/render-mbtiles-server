from fastapi import FastAPI, Response
from pymbtiles import MBtiles

app = FastAPI(title="Render MBTiles Server", version="0.1.0")


@app.get("/")
async def root():
    return {
        "endpoints": {
            "/docs": "Swagger UI",
            "/health": "Check the health of the server",
            "/vector/{tile_name}/{z}/{x}/{y}.pbf": "Get vector tiles from an MBTiles file",
        },
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/vector/{file_name}/{z}/{x}/{y}.pbf")
def vector_tile(file_name: str, z: int, x: int, y: int):
    """
    Serve vector tiles from an MBTiles file.
    """
    # xyz -> tms
    y = 2**z - y - 1

    with MBtiles(f"vector/{file_name}.mbtiles") as mbtiles:
        tile_data = mbtiles.read_tile(z, x, y)

    if tile_data is None:
        return Response(status_code=404)

    return Response(
        content=tile_data,
        media_type="application/vnd.mapbox-vector-tile",
        headers={"content-encoding": "gzip"},
    )

@app.get("/raster/{file_name}/{z}/{x}/{y}.png")
def raster_tile(file_name: str, z: int, x: int, y: int):
    """
    Serve raster tiles from an MBTiles file.
    """
    # xyz -> tms
    y = 2**z - y - 1

    with MBtiles(f"raster/{file_name}.mbtiles") as mbtiles:
        tile_data = mbtiles.read_tile(z, x, y)

    if tile_data is None:
        return Response(status_code=404)

    return Response(
        content=tile_data,
        media_type="image/png",
    )

