# -*- coding: utf-8 -*-
from flask_script import Server, Manager
from app import app
from instance.config import BaseConfig

manager = Manager(app)
app.config.from_object(BaseConfig)

manager.add_command("runserver", Server())

if __name__ == "__main__":
    manager.run()
