from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, Boolean, String
from setup import Base

CHAR_LENGTH = 50

class TodoTable(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(String(CHAR_LENGTH), nullable=False)
    completed = Column(Boolean, nullable=False)

class CreateTodo(BaseModel):
    title: str = Field(default='', max_length=CHAR_LENGTH)
    completed: bool = Field(default=False)
