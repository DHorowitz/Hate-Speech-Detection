import json
from json import loads

with open('hateupdate') as r, \
     open('hatewords', 'w') as w:
    dict = json.loads(r.read())
    for tweet in dict:
        w.write(json.dumps(tweet["vocabulary"]))
        #w.write(json.dumps(tweet["meaning"]))
        w.write("\n")
    
