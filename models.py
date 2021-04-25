from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()

# Define database model
class Venue(db.Model):
  __tablename__ = 'venues'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  city = db.Column(db.String(120), nullable=False)
  state = db.Column(db.String(120), nullable=False)
  address = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  genres = db.Column(db.ARRAY(db.String), nullable=False)
  website = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.Text)
  shows = db.relationship('Show', backref='venue', lazy=True, cascade='all, delete')

  def __repr__(self):
    return f'<Venue: {self.id} {self.name}>'

class Artist(db.Model):
  __tablename__ = 'artists'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  city = db.Column(db.String(120), nullable=False)
  state = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(120))
  genres = db.Column(db.ARRAY(db.String), nullable=False)
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  website = db.Column(db.String(120))
  seeking_venue = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.Text)
  shows = db.relationship('Show', backref='artist', lazy=True, cascade='all, delete')

  def __repr__(self):
    return f'<Artist: {self.id} {self.name}>'

class Show(db.Model):
  __tablename__ = 'shows'

  id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime, nullable=False) 
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

  def __repr__(self):
    return f'<Show: {self.id}>'