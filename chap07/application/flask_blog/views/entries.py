from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog.models.entries import Entry
from datetime import datetime


@app.route('/')
def show_entries():
    entries = Entry.scan()
    entries = sorted(entries, key=lambda x: x.id, reverse=True)
    return render_template('entries/index.html', entries=entries)


@app.route('/entries', methods=['POST'])
def add_entry():
    entry = Entry(
        id=int(datetime.now().timestamp()),
        title=request.form['title'],
        text=request.form['text']
    )
    entry.save()
    return redirect(url_for('show_entries'))


@app.route('/entries/new', methods=['GET'])
def new_entry():
    return render_template('entries/new.html')


@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    entry = Entry.get(id)
    return render_template('entries/show.html', entry=entry)


@app.route('/entries/<int:id>/edit', methods=['GET'])
def edit_entry(id):
    entry = Entry.get(id)
    return render_template('entries/edit.html', entry=entry)


@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
    entry = Entry.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    entry.save()
    return redirect(url_for('show_entries'))


@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    entry = Entry.get(id)
    entry.delete()
    return redirect(url_for('show_entries'))