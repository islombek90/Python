from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager




data = DataManager()
cities = data.get_required_fight()
print(cities)
print(len(cities))


flight = FlightSearch()
for city in range(0,len(cities)):
    # print(cities[city]["iataCode"])
    flight.flight_multicity_serach(cities[city]["iataCode"])

    #flight.flight_multicity_serach(cities[city]["city"])
    # print(cities[city]["lowestPrice"])
    data = FlightData()
    data.compare_price(cities[city]["lowestPrice"])

#
