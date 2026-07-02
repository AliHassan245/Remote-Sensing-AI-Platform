from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from PIL import Image
import shutil
import uuid
import os

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOADS_DIR = BASE_DIR / "uploads"

UPLOADS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


@router.post("/upload")
async def upload_image(
    file: UploadFile = File(...)
):

    try:

        # Delete previous uploads
        for old_file in UPLOADS_DIR.iterdir():
            if old_file.is_file():
                old_file.unlink()

        # Save uploaded file temporarily
        extension = Path(file.filename).suffix.lower()

        temp_filename = f"{uuid.uuid4()}{extension}"

        temp_path = UPLOADS_DIR / temp_filename

        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        # Convert every image to JPG
        final_filename = f"{uuid.uuid4()}.jpg"

        final_path = UPLOADS_DIR / final_filename

        image = Image.open(temp_path)

        image = image.convert("RGB")

        image.save(
            final_path,
            "JPEG",
            quality=95
        )

        # Remove temporary file
        os.remove(temp_path)

        return {
            "message": "Upload Successful",
            "filename": final_filename,
            "image_url": f"/uploads/{final_filename}"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )