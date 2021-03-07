import requests
import json

send_url = "http://api.ipstack.com/check?access_key=7bf70b206feb1b82eca4a6195331e493"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']

print(city)