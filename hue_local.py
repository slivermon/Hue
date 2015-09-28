import requests
import json
import yaml
#import pandas as pd
# To access debug panel http://<bridge ip address>/debug/clip.html
# More about the 'requests' module:  http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests

# Get API key and local IP address
credentials = yaml.load(open('credentials.yml'))
api_key = credentials['hue_api_key']
ip_address = credentials['ip']

# Construct the API request URL
url = "http://{0}/api/{1}/lights".format(ip_address, api_key)
print(url)

# Get a list of all lights
resp = requests.get(url)
data_lights = json.loads(resp.text) # requests library's .text shows JSON

# Create menu objects from JSON
light_list = {}
for light in data_lights.keys():
    light_list.append(data_lights[light]['name'])



# Light change menu; would be great to pull the list from the API next time
print('Which light do you want to use?')
print('   1 - Floor Light')
print('   2 - Ivy Light')
print('   3 - Table Light')
print('   4 - Iris')
print('   5 - Bloom')
select_light = input('Enter number of light: ')

# Change light attribute
brightness = input('Enter new brightness value (1 - 254): ')
brightness = int(brightness) # Must be an integer or it will error

# Create URL and payload
change_brightness_url = url + select_light  + '/state/'
brightness_payload = {'bri': brightness}

# For debug
print()
print('API URL: ' + change_brightness_url)
print('Payload: ' + str(brightness_payload))
print()

# Make the call!
print('Changing brightness...')
request = requests.put(change_brightness_url, data=json.dumps(brightness_payload)) # Store response in 'request' variable; data=json.dumps() is for json payloads, params=variable is for query strings
print(request)
