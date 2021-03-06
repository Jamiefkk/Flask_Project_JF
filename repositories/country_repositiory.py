from db.run_sql import run_sql

from models.country import Country
from models.user import User

def save(country):
    sql = "INSERT INTO countries(name, category) VALUES ( %s, %s ) RETURNING id"
    values = [country.name, country.category]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    locations = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        location = Country(row['name'], row['category'], row['id'])
        locations.append(location)
    return locations

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result:
        row = result[0]
        country = Country(row['name'], row['category'], row['id'])
    return country

