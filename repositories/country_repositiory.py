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