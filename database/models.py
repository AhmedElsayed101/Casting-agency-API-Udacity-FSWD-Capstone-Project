from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hello(db.Model):
    pass


