from flask import Flask, request, render_template, redirect, flash, sessions
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text #apparently this one has to stay in app
from models import db, connect_db, Pet

app = Flask(__name__) #make flask app
app.app_context().push() #newly needed

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'#using postgres and here's the db // has to be before below chunk
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #keeps overhead down
app.config['SQLALCHEMY_ECHO'] = True #shows the underlying SQL query
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def list_pets():
    """Shows list of all pets in db"""
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route('/', methods=["POST"])
def create_pet():
    name = request.form["name"]
    species = request.form["species"]
    hunger = request.form["hunger"]
    hunger = int(hunger) if hunger else None

    new_pet = Pet(name=name, species=species, hunger=hunger)
    db.session.add(new_pet)
    db.session.commit()

    return redirect(f'/{new_pet.id}')

@app.route('/<int:pet_id>')
def show_pet(pet_id):
    """Show details about a single pet"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('details.html', pet=pet)

@app.route('/species/<species_id>')
def show_pets_by_species(species_id):
    pets = Pet.get_by_species(species_id)
    return render_template("species.html", pets=pets, species=species_id)