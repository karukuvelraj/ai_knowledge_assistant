from sqlalchemy import (
    Boolean, Integer, String, Text, ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True, comment="Username of the user")

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, comment="Email address of the user")

    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False, comment="Hashed password of the user")

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, comment="Indicates whether the user is active")


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, comment="ID of the user who owns the document")

    filename: Mapped[str] = mapped_column(String(255), nullable=False, comment="Filename of the document")

    file_path: Mapped[str] = mapped_column(String(500), nullable=False, comment="File path of the document")    

    status: Mapped[str] = mapped_column(String(50), default="pending", comment="Status of the document processing")