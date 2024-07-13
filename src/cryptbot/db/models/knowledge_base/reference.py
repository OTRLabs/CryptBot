# src/cryptflows/db/models/knowledge_base/reference.py
from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...database import KnowledgeBaseBase

class Reference(KnowledgeBaseBase):
    __tablename__ = "reference"
    title: Mapped[str] = mapped_column(String(length=255), nullable=False)
    url: Mapped[str] = mapped_column(String(length=2083), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)