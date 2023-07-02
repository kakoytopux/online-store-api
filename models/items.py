from sqlalchemy import String, Text, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from middlewares.db import db

class Base(DeclarativeBase):
  pass

class Items(Base):
  __tablename__ = 'items'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  img_url: Mapped[str] = mapped_column(Text, nullable=False)
  name: Mapped[str] = mapped_column(String(40), nullable=False)
  desc: Mapped[str] = mapped_column(Text, nullable=False)
  tags: Mapped[str] = mapped_column(String(255), nullable=False)
  likes: Mapped[str] = mapped_column(JSON, default={})

Base.metadata.create_all(bind=db.get_conn())