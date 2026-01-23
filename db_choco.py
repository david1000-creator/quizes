import sqlite3
from typing import overload

from queries_choco import *
from contextlib import contextmanager


class Database:
    def __init__(self, db_name='quiz.db'):
        self.db_name = db_name

    @contextmanager
    def _get_connection(self):
        """Контекстный менеджер для управления соединением."""
        conn = sqlite3.connect(self.db_name)
        # тип а-ля словарь
        # conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    def create_line(self, table, columns, data):
        voprosiki = len(columns.split(','))*'?, '
        if type(data) == str:
            data = [data]
        zapros = INSERT + table + f' {columns} VALUES ({voprosiki[:-2]})'
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(zapros, data)
            conn.commit()
            return cursor.lastrowid

    def complete_data(self, zapros, data):
        if type(data) == str:
            data = [data]
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(zapros, data)
            conn.commit()
            return cursor.fetchall()

    def complete(self, zapros):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(zapros)
            conn.commit()
            return cursor.fetchall()

def create_db(drop = True):
    db = Database('quiz.db')
    db.complete(PRAGMA)
    if drop:
        db.complete(DROP + 'quiz')
        db.complete(DROP + 'questions')
        db.complete(DROP + 'quiz_content')
        db.complete(CREATE_QUIZ)
        db.complete(CREATE_QUESTION)
        db.complete(CREATE_QUIZ_CONTENT)
    for q in QUIZES:
        res = db.create_line('quiz', ADD_QUIZES, q)
        # print(res)
    for q in QUESTIONS:
        res = db.create_line('questions', ADD_QUESTIONS, q)
        # print(res)
    for q in CONTENT:
        res = db.create_line('quiz_content', ADD_CONTENT, q)
        # print(res)
    return db


if __name__ == '__main__':
    db = Database()
    db.complete(PRAGMA)
    db.complete(DROP + 'quiz')
    db.complete(DROP + 'questions')
    db.complete(DROP + 'quiz_content')
    db.complete(CREATE_QUIZ)
    db.complete(CREATE_QUESTION)
    db.complete(CREATE_QUIZ_CONTENT)
    for q in QUIZES:
        res = db.create_line('quiz', ADD_QUIZES, q)
        # print(res)
    for q in QUESTIONS:
        res = db.create_line('questions', ADD_QUESTIONS, q)
        # print(res)
    for q in CONTENT:
        res = db.create_line('quiz_content', ADD_CONTENT, q)
        # print(res)