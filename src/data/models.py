import datetime
from typing import List, Optional
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, DateTime
from sqlalchemy.orm import Mapped, DeclarativeBase, relationship, backref, mapped_column
from sqlalchemy.sql import func, case
from sqlalchemy.ext.hybrid import hybrid_property

class Base(DeclarativeBase):
    pass

class Role(Base):
    __tablename__ = "role"

    role_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

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
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    custom_instruction: Mapped[str] = mapped_column(nullable=True)
    last_chat: Mapped[str] = mapped_column(nullable=True)
    user_role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id"), nullable=False)

    user_role: Mapped["Role"] = relationship('Role', backref="role_users", foreign_keys=[user_role_id])

    def __repr__(self):
        return (
            f"User(user_id={self.user_id!r}, "
            f"username={self.username!r}, "
            f"role_id={self.role_id!r})"
        )

class UserFeedback(Base):
    __tablename__ = "user_feedback"

    user_feedback_id: Mapped[int] = mapped_column(primary_key=True)
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    feedback: Mapped[str] = mapped_column(nullable=False)
    is_archived: Mapped[bool] = mapped_column(nullable=False, default=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"), nullable=False)

    owner: Mapped["User"] = relationship('User', backref="feedbacks", foreign_keys=[owner_id])

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
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    uploader_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"), nullable=False)

    uploader: Mapped["User"] = relationship('User', backref="documents", foreign_keys=[uploader_id])

    def __repr__(self):
        return (
            f"UploadedDoc(uploaded_doc_id={self.uploaded_doc_id!r}, "
            f"name={self.name!r}, "
            f"checksum={self.checksum!r}, "
            f"user_id={self.user_id})"
        )