import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json


data = {
    "Inputs": {
        "input1": {
            "ColumnNames": ["make", "fuel-type", "num-of-doors", "drive-wheels", "price"],
            "Values": [["audi", "gas", "two", "fwd", "1900000"], ["value", "value", "value", "value", "0"], ]
        },
    },
    "GlobalParameters": {

            }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/150a17d6571440eaa02251fdf425d380/services/49a5b5075fee4d339df586f46c06202d/execute?api-version=2.0&details=true'
api_key = 'SrmGG/dK6O+zeZvoJLb0i81Wv0AkyYd+9n7nOuTUjEG6YGewl0hMTaPT3mUoQwMad/Ie6/rLlJF5aR0y5BWIhw=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result)

except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))

