from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):

    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable= False)
    start_time = db.Column(db.Date, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'start_time': self.start_time
        }



class Actor(db.Model):

    __tablename__ = 'actors'
    
    id = db.Column(db.Integer, primary_key=True)
    # auth0_id = db.Column(db.String(80), nullable = False)
    name = db.Column(db.String(80), nullable= False)
    age = db.Column(db.Integer, nullable= False)
    gender = db.Column(db.String(20), nullable= False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'gender': self.gender
        }


