from flask import Flask, render_template, request
import requests
from api_secrets import MAPQUEST_API_KEY

API_BASE_URL = "https://www.mapquestapi.com/geocoding/v1"

key = MAPQUEST_API_KEY

app = Flask(__name__)


@app.route("/")
def show_address_form():
    return render_template("address_form.html")


def get_coords(address):
    res = requests.get(f"{API_BASE_URL}/address",
                       params={'key': key, 'location': address})

    data = res.json()
    lat = data["results"][0]['locations'][0]['latLng']['lat']
    lng = data["results"][0]['locations'][0]['latLng']['lng']
    coords = {'lat': lat, 'lng': lng}
    return coords


@app.route("/geocode")
def get_location():
    address = request.args["address"]  # if it's a get request it's in the args
    coords = get_coords(address)
    return render_template("address_form.html", coords=coords)
