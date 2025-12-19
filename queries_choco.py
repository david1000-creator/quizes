CREATE_QUIZ = """ CREATE TABLE IF NOT EXISTS quiz (
id INTEGER PRIMARY KEY,
name TEXT 
)"""

CREATE_QUESTION = """CREATE TABLE IF NOT EXISTS questions (
id INTEGER PRIMARY KEY,
text TEXT,
right_ans TEXT,
wrong TEXT
)"""

CREATE_QUIZ_CONTENT = """CREATE TABLE IF NOT EXISTS quiz_content (
id INTEGER PRIMARY KEY,
quiz_id INTEGER,
quest_id INTEGER,
FOREIGN KEY (quiz_id) REFERENCES quiz (id),
    FOREIGN KEY (quest_id) REFERENCES questions (id)
)"""

QUIZES = [
    ('chocopie'),
    ('not_chocopie')
]
SELECT = 'SELECT * FROM'
INSERT = """INSERT INTO """

ADD_QUIZES = '(name)'
ADD_QUESTIONS = """(text, right_ans, wrong)"""
ADD_CONTENT = """(quiz_id, quest_id)"""


QUESTIONS = [
    ('how much does a 30kg pig weight', '30kg', '40kg ~ 50kg ~ idk'),
    ('what is 4x50', '200', '50505050 ~ idk ~ 800 ~ 450'),
    ('what is the biggest plane in the world for the whole history', 'an-225', 'A380 ~ B747 ~ B777'),
    ('if i was born 10 years ago how old am i', '10', '20 ~ 2015 ~ 4BILLIONS'),
    ('who is the creator of undertale', 'tobyfox and temmie', 'what is undertale ~ i only recognize deltarune ~ SANS'),
    ('what does endryoniy pelmen mean', 'RAGE', 'tasty dumpling ~ frends named endrey ~ are you sure its english')
]

DROP = 'DROP TABLE IF EXISTS '
CONTENT = [
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
]
PRAGMA = "PRAGMA foreign_keys=on"