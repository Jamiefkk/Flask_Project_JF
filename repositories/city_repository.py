from db.run_sql import run_sql

from models.city import City
from models.user import User
import repositories.country_repositiory as country_repository

def save(city):
    sql = "INSERT INTO cities(name, country_id) VALUES ( %s, %s ) RETURNING id"
    values = [city.name, city.country.id]
    results = run_sql( sql, values )
    city.id = results[0]['id']
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result:
        row = result[0]
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['id'])
    return city