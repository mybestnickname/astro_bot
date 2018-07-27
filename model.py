from sqlalchemy import Column, String, Integer, Date
from base_def import Base
import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, index=True, unique=True)
    last_quiz_res = Column(Integer, default='0/0')
    last_quiz_date = Column(Date, default=datetime.datetime.now().date())

    def __init__(self, telegram_id, last_quiz_res):
        self.telegram_id = telegram_id
        self.last_quiz_res = last_quiz_res


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_str = Column(String, index=True, unique=True)
    answ_1 = Column(String)
    answ_2 = Column(String)
    answ_3 = Column(String)
    # 4 варик ответа - всегда верный
    answ_4 = Column(String)
    quest_counter = Column(Integer, default=0)
    true_answ_counter = Column(Integer, default=0)

    def __init__(self, question_str, answ_1, answ_2, answ_3, answ_4):
        self.question_str = question_str
        self.answ_1 = answ_1
        self.answ_2 = answ_2
        self.answ_3 = answ_3
        self.answ_4 = answ_4
