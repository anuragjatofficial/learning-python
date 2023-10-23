# pthon JSON 
# ----------

import json

# json module is used to 
# parse json file to data


person = '{"name":"Anurag","languages":["English","French"]}' # json string

person_dict = json.loads(person)

print(person)


with open('Day-6/test.json') as f:
    data = json.load(f) # returns a dictinory 

print(data)