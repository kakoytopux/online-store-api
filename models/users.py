from sqlalchemy import String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from middlewares.db import db

class Base(DeclarativeBase):
  pass

class Users(Base):
  __tablename__ = 'users'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String(30), nullable=False)
  email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
  password: Mapped[str] = mapped_column(Text, nullable=False)
  rank: Mapped[str] = mapped_column(String(255), default='user')

Base.metadata.create_all(bind=db.get_conn())