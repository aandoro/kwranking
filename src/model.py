from src.db import Base,session
from sqlalchemy import Column, Integer, String

class Keyword(Base):
    __tablename__ = 'keyword'

    id = Column(Integer, primary_key =True)
    keyword = Column(String, unique=True, nullable = False)
    posicion = Column(Integer, nullable = True)

    def __init__(self, keyword, posicion = None):
        self.keyword = keyword
        self.posicion = posicion

    def save(self):
        try:
            session.add(self)
            session.commit()
        except Exception as e:
            session.rollback();

    def update(self,posicion):
        return session.query(Keyword).get(self.id)

    def delete(self):
        try:
            session.delete(self)
            session.commit()
        except Exception as e:
            session.rollback();

    @staticmethod
    def get_all():
        return session.query(Keyword).all()

    def __repr__(self):
        return f'Keyword ({self.keyword}, {self.posicion})'

    def __str__(self):
        return self.keyword