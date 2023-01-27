from todo.database.base import Base, engine
from sqlalchemy import Column, String, Integer, Boolean


class ToDo(Base):
    # Создание таблицы
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complite = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
