# Deploy MBTiles Server on Render

Use this repo as a template to deploy an MBTiles server on Render.

Follow the steps below:

## Manual Steps

1. You may [create your own repository from this template](https://github.com/nakamori1024/render-mbtiles-server/generate).

2. Place your MBTiles files in the appropriate directories:
   - Vector tiles: Place `.mbtiles` files in the `vector/` directory
   - Raster tiles: Place `.mbtiles` files in the `raster/` directory

3. Create a new Web Service on [Render](https://dashboard.render.com/web/new).

4. Specify the URL to your new repository.

5. Specify the following as the Build Command.
    ```shell
    pip install uv && uv sync --frozen
    ```

6. Specify the following as the Start Command.
    ```shell
    uv run uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

7. Click Deploy Web Service.

## Local Development

For developers who want to run the server locally:

1. Clone this repository:
   ```shell
   git clone git@github.com:nakamori1024/render-mbtiles-server.git
   cd render-mbtiles-server
   ```

2. Set up Python virtual environment:
   ```shell
   uv venv
   source .venv/bin/activate
   ```

3. Install dependencies using uv:
   ```shell
   uv sync
   ```

4. Start the development server:
   ```shell
   uv run uvicorn main:app --reload  
   ```

## Sample Data

This repository includes sample MBTiles files for demonstration purposes:

### Vector Data
- **Medical Areas**: Based on National Land Numerical Information (Ministry of Land, Infrastructure, Transport and Tourism of Japan)
  - Source: [国土数値情報ダウンロードサイト 医療圏データ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A38-2020.html)
  - License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
  - Note: Data has been processed and converted to MBTiles format

### Raster Data
- **Natural Earth II**: Natural Earth raster data
  - Source: [Natural Earth II with Shaded Relief and Water](https://www.naturalearthdata.com/downloads/50m-raster-data/50m-natural-earth-2/)
  - License: Public Domain

## Acknowledgments

This template is inspired by and builds upon the original FastAPI deployment examples for Render. Special thanks to:

- [Harish](https://harishgarg.com) for the [original FastAPI quickstart inspiration](https://twitter.com/harishkgarg/status/1435084018677010434) and foundational code
- The Render community for sharing deployment best practices
- The FastAPI and uv communities for creating excellent tools

This template extends the original concept with modern Python tooling (`uv`), comprehensive development guidelines, and production-ready configurations.
