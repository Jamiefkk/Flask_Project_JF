from models.visits_attraction import VisitsAttraction
from models.attraction import Attraction
from models.user import User

import repositories.user_repository as user_respository
import repositories.attraction_repository as attraction_respository
from db.run_sql import run_sql

def save(visit):
    sql = "INSERT INTO visits_attraction ( user_id, attraction_id, review, visited) VALUES ( %s, %s, %s, %s) RETURNING id"
    values = [visit.user.id, visit.attraction.id, visit.review, visit.visited]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit

def delete_all():
    sql = "DELETE FROM visits_attraction"
    run_sql(sql)

def select_all():
    visits = []

    sql = "SELECT * FROM visits_attraction"
    results = run_sql(sql)

    for row in results:
        user = user_respository.select(row['user_id'])
        attraction = attraction_respository.select(row['attraction_id'])
        visit = VisitsAttraction(user, attraction, row['review'], row['id'])
        visits.append(visit)
    return visits

def select_all_from_attractions(attraction):
    visits = []

    sql = "SELECT * FROM visits_attraction WHERE attraction_id = %s AND review IS NOT NULL"
    values = [attraction]
    results = run_sql(sql, values)

    for row in results:
        user = user_respository.select(row['user_id'])
        attraction = attraction_respository.select(row['attraction_id'])
        visit = VisitsAttraction(user, attraction, row['review'], row['id'])
        visits.append(visit)
    return visits