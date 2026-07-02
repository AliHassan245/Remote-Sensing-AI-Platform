from fastapi import APIRouter, HTTPException
from pathlib import Path

from services.image_service import (
    enhance_image,
    denoise_image,
    sharpen_image,
    deblur_image
)

router = APIRouter(
    prefix="/process",
    tags=["Processing"]
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOADS_DIR = BASE_DIR / "uploads"
OUTPUTS_DIR = BASE_DIR / "outputs"

OUTPUTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def get_uploaded_image():

    images = list(UPLOADS_DIR.glob("*"))

    if len(images) == 0:
        raise HTTPException(
            status_code=404,
            detail="No uploaded image found."
        )

    return images[-1]


def create_response(message, output_file):

    return {
        "message": message,
        "filename": output_file.name,
        "image_url": f"/outputs/{output_file.name}"
    }


@router.post("/enhance")
def enhance():

    input_image = get_uploaded_image()

    output_path = OUTPUTS_DIR / f"enhanced_{input_image.name}"

    enhance_image(
        str(input_image),
        str(output_path)
    )

    return create_response(
        "Image Enhanced",
        output_path
    )


@router.post("/denoise")
def denoise():

    input_image = get_uploaded_image()

    output_path = OUTPUTS_DIR / f"denoised_{input_image.name}"

    denoise_image(
        str(input_image),
        str(output_path)
    )

    return create_response(
        "Image Denoised",
        output_path
    )


@router.post("/sharpen")
def sharpen():

    input_image = get_uploaded_image()

    output_path = OUTPUTS_DIR / f"sharpened_{input_image.name}"

    sharpen_image(
        str(input_image),
        str(output_path)
    )

    return create_response(
        "Image Sharpened",
        output_path
    )


@router.post("/deblur")
def deblur():

    input_image = get_uploaded_image()

    output_path = OUTPUTS_DIR / f"deblurred_{input_image.name}"

    deblur_image(
        str(input_image),
        str(output_path)
    )

    return create_response(
        "Image Deblurred",
        output_path
    )