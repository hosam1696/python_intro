# import geopy
#
# geolocation = geopy.geocoders.Nominatim()
cities, years = [], []
for line in open('games.txt', 'r'):
    words = line.split()
    city = ' '.join(words[:-1]).ljust(10)
    year = words[-1].strip('()')
    cities.append(city)
    years.append(year)
    # print(geolocation.geocode(line.split()[0]))

print( list(zip(cities,years)), sep='\n')

results = []

for city, year in zip(cities,years):
    if int(year) > 1945:
        results.append(city + ': ' + year)

print(results)

cities_by_year = {year: city.strip() for city,year in zip(cities,years)}

print(cities_by_year)