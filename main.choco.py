from flask import Flask, redirect, url_for, request, render_template, session
import os
from db_choco import *
from queries_choco import *
from random import shuffle



def index():
    if request.method == 'GET':
        quizes = db.complete(SELECT + ' quiz')
        return render_template('index.html.html', quizes=quizes)
    elif request.method == 'POST':
        quiz_id = request.form.get('quizes')
        start_quis(quiz_id)
        return redirect(url_for('test'))


def test():
    if request.method == 'POST':
        save_answer()
    next_question = db.complete_data(NEXT_QUESTION_ID, (session['last_id'], session['quiz_id']))
    if next_question is None or len(next_question) == 0:
        return redirect(url_for('result'))
    else:
        return question_form(next_question[0])


def result():
    if request.method == 'POST':
        end_quiz()
        return redirect(url_for('index'))
    else:
        amount = db.complete_data(COUNT_QS, (session['quiz_id']))[0][0]
        return render_template('result.html.html', right_ans = session['right'], total = amount)



def start_quis(quiz_id):
    session['quiz_id'] = quiz_id
    session['right'] = 0
    session['last_id'] = db.complete_data(GET_FIRST, (quiz_id))[0][0]-1


def end_quiz():
    session.clear()


def question_form(question):
    q_id = question[0]
    text = question[1]
    right = question[2]
    wrong = question[3].split(' ~ ')
    wrong.append(right)
    shuffle(wrong)
    return render_template('test.html.html', q_id=q_id, text=text, answers=wrong)

def save_answer():
    answer = request.form.get('answer_text')
    q_id = request.form.get('q_id')
    right_answer = db.complete_data(CHECK_RIGHTS, (q_id, answer))
    if right_answer is not None and len(right_answer) > 0:
        session['right'] += 1
    session['last_id'] = int(q_id)

db = create_db()
folder = os.getcwd()
app = Flask(__name__, static_folder=folder, template_folder=folder)
app.config['SECRET_KEY'] = 'verystrongkey'

app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test, methods=['GET', 'POST'])
app.add_url_rule('/result', 'result', result, methods=['GET', 'POST'])
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)
