import requests
import json
# import time
# To access debug panel http://<bridge ip address>/debug/clip.html

# For easy debug, skip data entry and use stored values for api and IP
skip_entry = False

print('Welcome to the Hue API Experimenter.')

if skip_entry == False:
    # Manually enter the api key and IP address
    api_key = input('Please enter the API key:')
    ip_address = input('Please enter the IP address of the bridge on the local network.')
else:
    # Remove this later, not secure to store API key here
    api_key = ''
    ip_address = ''

# Construct the API request URL
base_url = 'http://' + str(ip_address) + '/api/' + api_key + '/lights/'
print(base_url)

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
change_brightness_url = base_url + select_light  + '/state/'
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


