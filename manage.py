# -*- coding: utf-8 -*-
__author__ = 'Azzssss'

from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)

manager.add_command("runserver", Server(host="0.0.0.0",port=5000,use_debugger = True))

@manager.command
def save_todo():
    todo = Todo(content="my first todo")
    todo.save()

if __name__ == "__main__":
    manager.run()

