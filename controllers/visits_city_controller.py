from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
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

visit_cities_blueprint = Blueprint("/cities", __name__)

@visit_cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("/cities/index.html", cities = cities, countries = countries)

@visit_cities_blueprint.route("/cities/new", methods = ["GET"])
def new_city():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    return render_template("cities/new.html", countries = countries, users = users)

@visit_cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    city_name = request.form['city_name']
    country = request.form['country']
    city_country = country_repository.select(country)
    city = City(city_name, city_country)
    city_repository.save(city)
    return redirect('/cities')

@visit_cities_blueprint.route("/cities/<id>")
def show(id):
    cities = city_repository.select(id)
    attractions = attraction_repository.select(id)
    users = attraction_repository.users(cities)
    return render_template("cities/show.html", cities=cities, users=users)