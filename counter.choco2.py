from flask import Flask, session


def index():
    session['count'] = 0
    return '<a href="/ctr">Next</a>'


def counter():
    session['count'] += 1
    return f'<h1>{session["count"]}</h1>'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'verystrongkey'
app.add_url_rule('/', 'index', index)
app.add_url_rule('/ctr', 'counter', counter)
if __name__ == "__main__":
    app.run()