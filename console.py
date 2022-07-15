import pdb
# from models.attraction import Attraction
from models.city import City
from models.country import Country
from models.user import User
from models.visits_country import VisitsCountry

import repositories.user_repository as user_repository
import repositories.country_repositiory as country_repository
import repositories.visits_country_repositiory as visits_country_repository

# visit_repository.delete_all()
country_repository.delete_all()
user_repository.delete_all()

user1 = User('Samwise Gamgee')
user_repository.save(user1)

country1 = Country("Ireland", "Europe")
country_repository.save(country1)

visit1 = VisitsCountry(user1, country1, '5 stars')
visits_country_repository.save(visit1)

pdb.set_trace()
