# Deploy FastAPI on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render.

Follow the steps below:

## Manual Steps

1. You may [create your own repository from this template](https://github.com/nakamori1024/render-fastapi-template/generate) if you'd like to customize the code.
2. Create a new Web Service on [Render](https://dashboard.render.com/web/new).
3. Specify the URL to your new repository.
4. Specify the following as the Build Command.

    ```shell
    pip install uv && uv sync --frozen
    ```
5. Specify the following as the Start Command.

    ```shell
    uv run uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

## Acknowledgments

This template is inspired by and builds upon the original FastAPI deployment examples for Render. Special thanks to:

- [Harish](https://harishgarg.com) for the [original FastAPI quickstart inspiration](https://twitter.com/harishkgarg/status/1435084018677010434) and foundational code
- The Render community for sharing deployment best practices
- The FastAPI and uv communities for creating excellent tools

This template extends the original concept with modern Python tooling (`uv`), comprehensive development guidelines, and production-ready configurations.
