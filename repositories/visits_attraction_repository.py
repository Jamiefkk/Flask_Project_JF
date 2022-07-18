from models.visits_attraction import VisitsAttraction
from models.attraction import Attraction
from models.user import User

# import repositories.user_repository as user_respository
# import repositories.country_repositiory as country_respository
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