from pathlib import Path

from fastapi import UploadFile


UPLOAD_DIR = Path("uploads")

def save_uploaded_file(file: UploadFile) -> str:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        while chunk := file.file.read(1024 * 1024):  # Read in 1MB chunks
            buffer.write(chunk)

    return str(file_path)