from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.attraction import Attraction
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

visit_attractions_blueprint = Blueprint("attractions", __name__)

@visit_attractions_blueprint.route("/attractions")
def attractions():
    attractions = attraction_repository.select_all()
    return render_template("attractions/index.html", attractions = attractions)

@visit_attractions_blueprint.route("/attractions/new", methods = ["GET"])
def new_attraction():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    attractions = attraction_repository.select_all()
    return render_template("attractions/new.html", attractions = attractions, countries = countries, users = users, cities = cities)

@visit_attractions_blueprint.route("/attractions",  methods=['POST'])
def create_attraction():
    attraction_name = request.form['attraction_name']
    country = request.form['country']
    attraction_country = country_repository.select(country)
    city = request.form['city']
    attraction_city = city_repository.select(city)
    attraction_cat = request.form['attraction_cat']
    attraction = Attraction(attraction_name, attraction_cat, attraction_country, attraction_city)
    attraction_repository.save(attraction)
    return redirect('/attractions')

@visit_attractions_blueprint.route("/attractions/<id>")
def show(id):
    attractions = attraction_repository.select(id)
    users = attraction_repository.users(attractions)
    return render_template("attractions/show.html", attractions=attractions, users=users)

@visit_attractions_blueprint.route("/attractions/<id>/delete", methods=["POST"])
def delete(id):
    attraction_repository.delete(id)
    return redirect("/attractions")

@visit_attractions_blueprint.route("/attractions/newentry", methods=['GET'])
def new_attraction_form():
    users = user_repository.select_all()
    attractions = attraction_repository.select_all()
    return render_template("attractions/newentry.html", users = users, attractions = attractions)


@visit_attractions_blueprint.route("/attractions/newentry",  methods=['POST'])
def create_attraction_review():
    user_id = request.form['user_id']
    attraction_id = request.form['attraction_id']
    review = request.form['review']
    user = user_repository.select(user_id)
    attraction = attraction_repository.select(attraction_id)
    visit = VisitsAttraction(user, attraction, review, visited = "Visited")
    breakpoint()
    visits_attraction_repository.save(visit)
    return redirect('/attractions')
