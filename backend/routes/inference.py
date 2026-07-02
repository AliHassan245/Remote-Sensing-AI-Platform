from fastapi import APIRouter, HTTPException
from pathlib import Path

from models.vqa import QuestionRequest
from services.vlm_service import ask_image

router = APIRouter(
    prefix="/inference",
    tags=["Inference"]
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOADS_DIR = BASE_DIR / "uploads"


def get_uploaded_image():

    images = list(UPLOADS_DIR.glob("*"))

    if len(images) == 0:
        raise HTTPException(
            status_code=404,
            detail="No uploaded image found."
        )

    return images[-1]


@router.post("/ask")
def ask(request: QuestionRequest):

    input_image = get_uploaded_image()

    answer = ask_image(
        str(input_image),
        request.question
    )

    return {
        "filename": input_image.name,
        "question": request.question,
        "answer": answer
    }