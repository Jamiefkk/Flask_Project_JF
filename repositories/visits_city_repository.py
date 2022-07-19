from models.visits_city import VisitsCity
from models.city import City
from models.user import User
import repositories.city_repository as city_repository
import repositories.user_repository as user_repository
from db.run_sql import run_sql

def save(visit):
    sql = "INSERT INTO visits_city ( user_id, city_id, review, visited) VALUES ( %s, %s, %s, %s) RETURNING id"
    values = [visit.user.id, visit.city.id, visit.review, visit.visited]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit

def delete_all():
    sql = "DELETE FROM visits_city"
    run_sql(sql)

def select_all_from_city(city):
    visits = []

    sql = "SELECT * FROM visits_city WHERE city_id = %s AND review IS NOT NULL"
    values = [city]
    results = run_sql(sql, values)

    for row in results:
        user = user_repository.select(row['user_id'])
        city = city_repository.select(row['city_id'])
        visit = VisitsCity(user, city, row['review'], row['id'])
        visits.append(visit)
    return visits