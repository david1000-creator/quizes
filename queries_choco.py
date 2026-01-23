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

COUNT_QS = '''SELECT COUNT(*)
FROM quiz_content
WHERE quiz_id = ?'''

NEXT_QUESTION_ID = """
SELECT quiz_content.id, 
       questions.text, questions.right_ans, questions.wrong
    FROM questions, quiz_content
    WHERE quiz_content.quest_id == questions.id
    AND quiz_content.id > ? AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id"""

CHECK_RIGHTS = '''SELECT quiz_content.id, questions.text, questions.right_ans
    FROM questions, quiz_content
    WHERE quiz_content.id = ? AND (questions.right_ans LIKE ?)'''

GET_FIRST = '''SELECT quest_id
    FROM quiz_content
    WHERE quiz_id = ?
    ORDER BY quest_id
    LIMIT 1'''

ADD_QUIZES = '(name)'
ADD_QUESTIONS = """(text, right_ans, wrong)"""
ADD_CONTENT = """(quiz_id, quest_id)"""


QUESTIONS = [
    ('how much does a 30kg pig weight', '30kg', '40kg ~ 50kg ~ idkg'),
    ('what is 4x50', '200', '50505050 ~ idk ~ 800 ~ 450'),
    ('what is the biggest plane in the world for the whole history', 'an-225', 'A380 ~ B747 ~ B777'),
    ('if i was born 10 years ago how old am i', '10', '20 ~ 2015 ~ 4BILLIONS'),
    ('who is the creator of undertale', 'tobyfox and temmie', 'what is undertale ~ i only recognize deltarune ~ SANS'),
    ('what does endryoniy pelmen mean', 'RAGE', 'tasty dumpling ~ friend named endrey ~ are you sure its english')
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