from db.run_sql import run_sql

from models.attraction import Attraction
from models.country import Country
from models.user import User

def save(user):
    sql = "INSERT INTO users( name ) VALUES ( %s ) RETURNING id"
    values = [user.name]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    return users


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    user = run_sql(sql, values)
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def locations_countries(user):
    locations = []

    sql = "SELECT countries.* FROM countries INNER JOIN visits_country ON visits_country.country_id = countries.id WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        location = Country(row['name'], row['category'], row['id'])
        locations.append(location)

    return locations