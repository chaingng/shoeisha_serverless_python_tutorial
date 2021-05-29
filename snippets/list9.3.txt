from flask_script import Command
from flask_blog.models.entries import Entry
from flask_blog.models.sessions import Session

class InitDB(Command):
    "create database"

    def run(self):
        if not Entry.exists():
            Entry.create_table(read_capacity_units=5, write_capacity_units=2)
        if not Session.exists():
            Session.create_table(read_capacity_units=5, write_capacity_units=2)
