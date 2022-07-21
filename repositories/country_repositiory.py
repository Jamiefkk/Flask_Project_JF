from db.run_sql import run_sql

from models.country import Country
from models.user import User
import repositories.visits_country_repositiory as visits_country_repository
import repositories.country_repositiory as country_repository
import repositories.user_repository as user_repository
from models.visits_country import VisitsCountry
from repositories.user_repository import User

def save(country):
    sql = "INSERT INTO countries(name, category) VALUES ( %s, %s ) RETURNING id"
    values = [country.name, country.category]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    new_country = country_repository.select(country.id)
    user = user_repository.select(1)
    visit = VisitsCountry(user, new_country, None, "Not visited")
    visits_country_repository.save(visit)
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

