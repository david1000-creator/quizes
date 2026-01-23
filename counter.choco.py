from flask import Flask, session


class Counter:
    def __init__(self):
        self.ctr = 0

def index():
    count.ctr = 0
    return'<a href="/ctr">Next</a>'

def counter():
    count.ctr += 1
    return f'<h1>{count.ctr}</h1>'
count=Counter()
app = Flask(__name__)

app.add_url_rule('/', 'index', index)
app.add_url_rule('/ctr', 'counter', counter)
if __name__ == "__main__":
    app.run()