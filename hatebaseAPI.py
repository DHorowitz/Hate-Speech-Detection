from json import loads
import json
from hatebase import HatebaseAPI

hatebase = HatebaseAPI({"key": '1cfe0ef015998aea71f2ad32bf9f601f'})
filters = {'language': 'eng', 'type': 't'}
output = "json"
query_type = "vocabulary"
response = hatebase.performRequest(filters, output, query_type)

# convert to Python object
response = loads(response)

with open('hatefile', 'w') as w:
    w.write(json.dumps(response["data"]))
