# -*- coding: utf-8 -*-
from flask import render_template, current_app
from app import app

@app.route('/')
def index():
    return render_template('layouts.html', data=current_app.config)