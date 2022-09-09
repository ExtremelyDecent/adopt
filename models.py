from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://www.shutterstock.com/image-vector/pet-paw-vector-icon-on-white-1906527277"

class Pet(db.Model):
    """Adopatable pet class"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

    def image_url (self):
        """returns image for pet with default"""

        return self.photo_url or DEFAULT_IMAGE
    
def connect_db(app)
    """Connects to database for flask app"""

    db.app = app
    db.init_app(app)