from db.run_sql import run_sql

from models.attraction import Attraction
from models.user import User

def save(attraction):
    sql = "INSERT INTO attractions(name, attraction_cat, country_id, city_id) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [attraction.name, attraction.attraction_cat, attraction.country.id, attraction.city.id]
    results = run_sql( sql, values )
    attraction.id = results[0]['id']
    return attraction

def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)