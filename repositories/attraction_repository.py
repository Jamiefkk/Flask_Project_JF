from db.run_sql import run_sql

from models.attraction import Attraction
from models.user import User

def save(attraction):
    sql = "INSERT INTO attractions(name, attraction_cat, country_id, city_id) VALUES ( %s, %s, %s, %s ) RETURNING id"
    city = attraction.city.id if attraction.city is not None else None
    values = [attraction.name, attraction.attraction_cat, attraction.country.id, city]
    results = run_sql( sql, values )
    attraction.id = results[0]['id']
    return attraction

def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)

def select(id):
    attraction = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        attraction = Attraction(result['name'], result['attraction_cat'], id = result['id'] )
    return attraction

def select_all():
    attractions = []
    sql = "SELECT * FROM attractions"
    results = run_sql(sql)

    for row in results:
        attraction = Attraction(row['name'],row["attraction_cat"], row['country_id'],row["city_id"], row['id'])
        attractions.append(attraction)
    return attractions

def users(attraction):
    users = []

    sql = "SELECT users.* FROM users INNER JOIN visits_attraction ON visits_attraction.user_id = users.id WHERE attraction_id = %s"
    values = [attraction.id]
    results = run_sql(sql, values)

    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)

    return users

def delete(id):
    sql = "DELETE FROM attractions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def attractions_in_cities(city_id):
    attractions = []

    sql = "SELECT attractions.* FROM attractions WHERE city_id = %s"
    values = [city_id]
    results = run_sql(sql, values)

    for row in results:
        attraction = Attraction(row['name'],row['attraction_cat'], row['id'])
        attractions.append(attraction)

    return attractions

def attractions_in_countries(city_id):
    attractions = []

    sql = "SELECT * FROM attractions WHERE country_id = %s AND city_id IS NULL"
    values = [city_id]
    results = run_sql(sql, values)

    for row in results:
        attraction = Attraction(row['name'],row['attraction_cat'], row['id'])
        attractions.append(attraction)

    return attractions