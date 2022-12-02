from flask import Flask

app = Flask(__name__)
app.config.from_object('flask_blog.config')

@app.route('/')
def show_entries():
    return "Hello World!"