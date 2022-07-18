from models.visits_country import VisitsCountry
from models.country import Country
from models.user import User

# import repositories.user_repository as user_respository
# import repositories.country_repositiory as country_respository
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