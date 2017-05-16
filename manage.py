# -*- coding: utf-8 -*-
from flask_script import Server, Manager
from app import app
from app.config.development import DevelopmentConfig

manager = Manager(app)
app.config.from_object(DevelopmentConfig)

manager.add_command("runserver", Server())

if __name__ == "__main__":
    manager.run()
