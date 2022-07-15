import pdb
from models.attraction import Attraction
from models.city import City
from models.country import Country
from models.user import User
from models.visits_city import VisitsCity
from models.visits_country import VisitsCountry

import repositories.user_repository as user_repository
import repositories.country_repositiory as country_repository
import repositories.visits_country_repositiory as visits_country_repository
import repositories.visits_city_repository as visits_city_respository
import repositories.city_repository as city_repository
import repositories.attraction_repository as attraction_repository

visits_city_respository.delete_all()
visits_country_repository.delete_all()
user_repository.delete_all()
city_repository.delete_all()
attraction_repository.delete_all()
country_repository.delete_all()

user1 = User('Samwise Gamgee')
user_repository.save(user1)

country1 = Country("Ireland", "Europe")
country_repository.save(country1)

city1 = City("Kilkenny", country1)
city_repository.save(city1)

attraction1 = Attraction("Kilkenny Castle", "Castle", city1.country, city1)
attraction_repository.save(attraction1)

visit1 = VisitsCountry(user1, country1, '5 stars')
visits_country_repository.save(visit1)

visit2 = VisitsCity(user1, city1, '6 stars')
visits_city_respository.save(visit2)

pdb.set_trace()
