from app import app
from database.models import *


@app.route('/')
def index():
    return "hello, capstone!"