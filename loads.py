# convert from json to python:
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
print(type(x))
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(type(y))