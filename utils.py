import os
from fastapi import HTTPException


def sanitize_filename(file_name: str) -> str:
    basename = os.path.basename(file_name)
    if basename != file_name:
        raise HTTPException(status_code=400, detail="Invalid characters in filename")
    return basename
