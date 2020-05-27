from flask import render_template
from app import app
from database.models import *


@app.route('/api')
def api():
    return "render_template('index.html')"