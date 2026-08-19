from fastapi import (
    APIRouter, Depends, UploadFile, HTTPException,
    UploadFile, status, File
)
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.database import get_db
from app.db.models import Document, User
from app.schemas.documents import DocumentResponse
from app.services.document_service import save_uploaded_file


router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only PDF files are allowed.")

    file_path = save_uploaded_file(file)

    document = Document(user_id=current_user.id, filename=file.filename, file_path=file_path, status="uploaded")
    db.add(document)
    db.commit()
    db.refresh(document)

    return document

