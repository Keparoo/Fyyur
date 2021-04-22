from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()

def setup_db(app):
  app.config.from_object('config')
  db = SQLAlchemy(app)
  migrate = Migrate(app, db)
  return db

class Venue(db.Model):
  __tablename__ = 'venues'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  city = db.Column(db.String(120), nullable=False)
  state = db.Column(db.String(120), nullable=False)
  address = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(120), nullable=False)
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))

  # TODO: implement any missing fields, as a database migration using Flask-Migrate
  # genres = db.Column(db.String(120), nullable=False)
  genres = db.Column(db.ARRAY(db.String))
  website = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.Text)
  shows = db.relationship('Show', backref='venue', lazy=True)


class Artist(db.Model):
  __tablename__ = 'artists'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  city = db.Column(db.String(120), nullable=False)
  state = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(120), nullable=False)
  genres = db.Column(db.ARRAY(db.String))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))

  # TODO: implement any missing fields, as a database migration using Flask-Migrate
  website = db.Column(db.String(120))
  seeking_venue = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.Text)
  shows = db.relationship('Show', backref='artist', lazy=True)

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
  __tablename__ = 'shows'

  id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime, nullable=False) 
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)