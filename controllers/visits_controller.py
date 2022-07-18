from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.visits_city import VisitsCity
from models.visits_country import VisitsCountry
from models.visits_attraction import VisitsAttraction
import repositories.user_repository as user_repository
import repositories.country_repositiory as country_repository
import repositories.visits_country_repositiory as visits_country_repository
import repositories.visits_city_repository as visits_city_respository
import repositories.visits_attraction_repository as visits_attraction_repository
import repositories.city_repository as city_repository
import repositories.attraction_repository as attraction_repository

locations_blueprint = Blueprint("countries", __name__)

@locations_blueprint.route("/countries")
def locations():
    locations = visits_country_repository.select_all() # NEW
    return render_template("locations/index.html", locations = locations)

@locations_blueprint.route("/locations/<id>")
def show(id):
    location = location_repository.select(id)
    users = location_repository.users(location)
    return render_template("locations/show.html", location=location, users=users)