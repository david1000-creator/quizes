from adodbapi.examples.db_table_names import databasename
from flask import Flask, redirect, url_for, request, render_template, session
import os
from db_choco import *
from queries_choco import *


def index():
    quizes = db.complete(SELECT+' quiz')
    print(quizes)
    return render_template('index.html.html', quizes=quizes)


def start_quis(quiz_id):
    session['quiz_id'] = quiz_id
    session['right'] = 0
    session['last_id'] = 0


def end_quiz():
    session.clear()


db = Database()
db.complete(PRAGMA)
folder = os.getcwd()
app = Flask(__name__, static_folder=folder, template_folder=folder)

app.add_url_rule('/', 'index', index)
if __name__ == "__main__":
    app.run()
