# Weather CLI

Uses the Openweathermap API to gather information about weather in location and return a brief description.

Location information can either be passed as an argument or entered after running the script.

### API Key
This script requires an API key from Openweathermap.
The key is stored in a python file titled api_key.py which is simply:
'''python
api_key = '<API KEY HERE>'
'''

### Requirements
Uses the requests library to get weather information.
This can be installed using the command 
'''
'pip install requests'
'''