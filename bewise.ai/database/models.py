from sqlalchemy import Column, Integer, Text, DateTime
from .database import Base


class Questions(Base):
    __tablename__ = 'questions'
    
    question_id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(DateTime)

    def __repr__(self) -> str:
        return f'{self.question_id} {self.question} {self.answer} {self.created_at}'