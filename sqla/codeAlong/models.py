from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()  #use alchemy for db


def connect_db(app):
    db.app = app  #for db use the flask app
    db.init_app(app)

#models go below
#db.Model - class model individual pet - table plural, pets


class Pet(db.Model):
    """Pets"""
    __tablename__ = 'pets'

    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).all()
    
    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger > 20).all()


    id = db.Column(db.Integer,  #not int, that's python
                   primary_key=True,
                   autoincrement=True)  #autinc = serial
    
    name = db.Column(db.String(50),
                     nullable=False,  #can be nulled; default true
                     unique=True)
    
    species = db.Column(db.String(30), nullable=True)
    
    hunger = db.Column(db.Integer,
                       nullable=False,
                       default=20)


    def __repr__(self):
        p = self
        return f"<Pet id{p.id} name={p.name} species={p.species} hunger={p.hunger}>"

    def greet(self):
        return f"I'm {self.name} the {self.species}"
    
    def feed(self, amt=20):
        """Update hunger based off of amt"""
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)