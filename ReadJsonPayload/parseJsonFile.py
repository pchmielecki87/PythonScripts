import json

json = json.loads(open('./Payload1.json').read())
value = json['key']
# print json['value']

# print the keys and values
for key in json:
    value = json[key]
    print("The key and value are ({}) = ({})".format(key, value))