import pdb
from models.attraction import Attraction
from models.city import City
from models.country import Country
from models.user import User
from models.visits_city import VisitsCity
from models.visits_country import VisitsCountry
from models.visits_attraction import VisitsAttraction

import repositories.user_repository as user_repository
import repositories.country_repositiory as country_repository
import repositories.visits_country_repositiory as visits_country_repository
import repositories.visits_city_repository as visits_city_respository
import repositories.visits_attraction_repository as visits_attraction_repository
import repositories.city_repository as city_repository
import repositories.attraction_repository as attraction_repository

# visits_attraction_repository.delete_all()
# visits_city_respository.delete_all()
# visits_country_repository.delete_all()
# user_repository.delete_all()
# attraction_repository.delete_all()
# city_repository.delete_all()
# country_repository.delete_all()

# user1 = User('Samwise Gamgee')
# user_repository.save(user1)

# user2 = User('Bob Cratchit')
# user_repository.save(user2)

# country1 = Country("Ireland", "Europe")
# country_repository.save(country1)

# city1 = City("Kilkenny", country1)
# city_repository.save(city1)

# attraction1 = Attraction("Kilkenny Castle", "Castle", city1.country, city1)
# attraction_repository.save(attraction1)

# attraction2 = Attraction("The Burren", "Cliff", country1, None)
# attraction_repository.save(attraction2)

# visit1 = VisitsCountry(user1, country1, '5 stars', "Visited")
# visits_country_repository.save(visit1)

# visit2 = VisitsCity(user1, city1, '6 stars', "Visited")
# visits_city_respository.save(visit2)

# visit3 = VisitsAttraction(user1, attraction1, '7 stars', "Visited")
# visits_attraction_repository.save(visit3)

# visit4 = VisitsAttraction(user2, attraction1, None, "Want to visit")
# visits_attraction_repository.save(visit4)

# visit5 = VisitsCity(user2, city1, None, "Want to visit")
# visits_city_respository.save(visit5)

# trip = user_repository.locations_countries(user1)
# print(trip)

print(city_repository.select(1))

pdb.set_trace()
