from unicodedata import category
import country_list
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.visits_city import VisitsCity
from models.visits_country import VisitsCountry
from models.visits_attraction import VisitsAttraction
from models.country import Country
import repositories.user_repository as user_repository
import repositories.country_repositiory as country_repository
import repositories.visits_country_repositiory as visits_country_repository
import repositories.visits_city_repository as visits_city_respository
import repositories.visits_attraction_repository as visits_attraction_repository
import repositories.city_repository as city_repository
import repositories.attraction_repository as attraction_repository
from country_list import countries_for_language
country_list = dict(countries_for_language('en'))
print(country_list)

visit_countries_blueprint = Blueprint("countries", __name__)

@visit_countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)
    
@visit_countries_blueprint.route("/countries/new", methods = ["GET"])
def new_country():
    users = user_repository.select_all()
    countries = country_list
    return render_template("countries/new.html", countries = countries, users = users)

@visit_countries_blueprint.route("/countries",  methods=['POST'])
def create_country():
    country_name = request.form['country_name']
    continent = request.form['continent']
    country = Country(country_name, continent)
    country_repository.save(country)
    return redirect('/countries')

@visit_countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repository.select(id)
    cities = city_repository.cities_in_countries(id)
    attractions = attraction_repository.attractions_in_countries(id)
    visits = visits_country_repository.select_all_from_country(id)
    return render_template("countries/show.html", country=country, cities=cities, attractions=attractions, visits = visits)

@visit_countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete(id):
    country_repository.delete(id)
    return redirect("/countries")

@visit_countries_blueprint.route("/countries/newentry", methods=['GET'])
def new_city_review():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    return render_template("countries/newentry.html", users = users, countries = countries)


@visit_countries_blueprint.route("/countries/newentry",  methods=['POST'])
def create_city_review():
    user_id = request.form['user_id']
    country_id = request.form['country_id']
    review = request.form['review']
    user = user_repository.select(user_id)
    country = city_repository.select(country_id)

    visit = VisitsCountry(user, country, review, visited = "Visited")
    visits_country_repository.save(visit)
    return redirect('/countries')
