from typing import List, Optional
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Mapped, DeclarativeBase, relationship, backref, mapped_column

class Base(DeclarativeBase):
    pass

class Role(Base):
    __tablename__ = "role"

    role_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    users: Mapped[List["User"]] = relationship(back_populates="role", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return (
            f"Role(role_id={self.role_id!r}, "
            f"name={self.name!r})"
        )

class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    custom_instruction: Mapped[str] = mapped_column(nullable=True)
    last_chat: Mapped[str] = mapped_column(nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id"), nullable=False)

    role: Mapped["Role"] = relationship(back_populates="users")
    user_feedbacks: Mapped[List["UserFeedback"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    uploaded_docs: Mapped[List["UploadedDoc"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"User(user_id={self.user_id!r}, "
            f"username={self.username!r}, "
            f"role_id={self.role_id!r})"
        )

class UserFeedback(Base):
    __tablename__ = "user_feedback"

    user_feedback_id: Mapped[int] = mapped_column(primary_key=True)
    feedback: Mapped[str] = mapped_column(nullable=False)
    is_archived: Mapped[bool] = mapped_column(nullable=False, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="user_feedbacks")

    def __repr__(self):
        return (
            f"UserFeedback(user_feedback_id={self.user_feedback_id!r}, "
            f"feedback={self.feedback!r}, "
            f"is_archived={self.is_archived!r}, "
            f"user_id={self.user_id!r})"
        )

class UploadedDoc(Base):
    __tablename__ = "uploaded_doc"

    uploaded_doc_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="uploaded_docs")

    def __repr__(self):
        return (
            f"UploadedDoc(uploaded_doc_id={self.uploaded_doc_id!r}, "
            f"name={self.name!r}, "
            f"checksum={self.checksum!r}, "
            f"user_id={self.user_id})"
        )