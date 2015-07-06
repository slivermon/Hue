import urllib.request

# For easy debug, skip data entry and use stored values for api and IP
skip_entry = True

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
api_request_base_url = 'http://' + str(ip_address) + '/api/' + api_key + '/lights/'
print(api_request_base_url)

# Encode api_request_base_url
# encoded_api_request_base_url = urllib.parse(api_request_base_url)

# Ugly response of lights on network
print('These are the lights on the local network:')
light_network_state = urllib.request.urlopen(api_request_base_url)
print(light_network_state)



