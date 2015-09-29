import requests
import json
import yaml
import time
#import pandas as pd
# To access debug panel http://<bridge ip address>/debug/clip.html
#
# More about the 'requests' module:
# http://docs.python-requests.org/en/latest/user/quickstart
# /#more-complicated-post-requests

# Get API key and local IP address
credentials = yaml.load(open('credentials.yml'))
api_key = credentials['hue_api_key']
ip_address = credentials['ip']

# Construct the API request URL
url = "http://{0}/api/{1}/lights/".format(ip_address, api_key)
print(url)

# Get a list of all lights from API
resp = requests.get(url)
data_lights = json.loads(resp.text) # requests library's .text shows JSON

# Create dict of lights object from JSON
# Maybe store lights in an array where light attributes can also be stored
light_list = {}
for light in data_lights:
    light_list[light] = data_lights[light]['name']

# Show lights in a list
# Would be worth sorting the list
def showLight():
    print "### Lights on the network ###\n"
    for light in light_list:
        print "    {} - {}".format(light, light_list[light])
    print

# Get light choice
def getLight():
    user_input = raw_input("Enter light number: ")
    # Validate input can be an integer and exists in dict
    if type(int(user_input)) == int and light_list.has_key(user_input) == True:
        selection = str(user_input)
        print "{} is selected.\n".format(light_list[selection])
        return selection # Return the unchanged string
    else:
        print "{} is not valid. Try again.\n".format(user_input)
        return False

# Get brightness value
def getBright():
    user_input = raw_input("Enter brightness value (1 - 254):  ")
    # Validate input as integer
    if type(int(user_input)) == int and int(user_input) > 0 and int(user_input) < 255:
        user_input = int(user_input)
        print
        return user_input
    else:
        print "You must enter a whole number. \n"
        return False

# Change light attributes
def modifyBright(key, brightness):
    # Create API URL and JSON payload
    hue_api_url = "{}{}/state/".format(url, key)
    payload_bri = {'bri': brightness}
    # Make the call
    print "Changing brightness of {} to {}...\n".format(light_list[key], brightness)
    request = requests.put(hue_api_url, data=json.dumps(payload_bri))
    print "API:  {}".format(hue_api_url)
    print "Payload:  {}".format(payload_bri)
    print "Done!"

# Main function
# Does not handle False values yet
def hueMain():
    showLight()
    select_light = getLight()
    brightness = getBright()
    modifyBright(select_light, brightness)

def hueCycle():
    showLight()
    select_light = getLight()
    brightness = getBright()

    # Cycle the brightness
    step = 15
    loops = 100
    direction = 'up'
    min_bright = 40
    sleep_dur = 0.25
    for cycles in range(1,loops):
        time.sleep(sleep_dur)
        if 254 - brightness >= 0 and direction == 'up':
            modifyBright(select_light, brightness)
            brightness += step
        elif direction == 'up':
            direction = 'down'
            brightness = 254
        elif brightness - min_bright >= 0 and direction == 'down':
            modifyBright(select_light, brightness)
            brightness -= step
        else:
            direction = 'up'
            brightness = min_bright
