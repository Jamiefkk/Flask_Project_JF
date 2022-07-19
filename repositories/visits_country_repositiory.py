from models.visits_country import VisitsCountry
from models.country import Country
from models.user import User

import repositories.user_repository as user_respository
import repositories.city_repository as city_repository
import repositories.country_repositiory as country_respository
from db.run_sql import run_sql

def save(visit):
    sql = "INSERT INTO visits_country ( user_id, country_id, review, visited) VALUES ( %s, %s, %s, %s) RETURNING id"
    values = [visit.user.id, visit.country.id, visit.review, visit.visited]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit

def delete_all():
    sql = "DELETE FROM visits_country"
    run_sql(sql)

def select_all_from_country(country):
    visits = []

    sql = "SELECT * FROM visits_country WHERE country_id = %s AND review IS NOT NULL"
    values = [country]
    results = run_sql(sql, values)

    for row in results:
        user = user_respository.select(row['user_id'])
        country = country_respository.select(row['country_id'])
        visit = VisitsCountry(user, country, row['review'], row['id'])
        visits.append(visit)
    return visits