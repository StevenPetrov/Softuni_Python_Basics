import phonenumbers
import folium


from myNumber import number

from phonenumbers import geocoder, carrier

from opencage.geocoder import OpenCageGeocode

Key = '0c240bc70a8e4355ab894e41b798ba2c'

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, 'en')
print(yourLocation)

service_provider = phonenumbers.parse(number)

print(carrier.name_for_number(service_provider, 'en'))

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup=yourLocation).add_to((myMap))
myMap.save('myLocation.html')