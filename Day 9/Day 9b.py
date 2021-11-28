#/*Dictionary with Nesting*\#
travel_log = [
{
  "country": "Nepal",
  "visits": 12,
  "cities": ["Kathmandu", "Pokhara", "Butwal"]
},
{
  "country": "India",
  "visits": 5,
  "cities": ["Noida", "Delhi"]
},
]
def add_new_country(country_name,times_visited,cities_visited):
  new_country={}
  new_country["country"]=country_name
  new_country["visits"]=times_visited
  new_country["cities"]=cities_visited
  travel_log.append(new_country)



add_new_country("China", 2, ["Beijing", "Sanghai"])
print(travel_log)



