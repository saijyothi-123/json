# convert python to json:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print(type(x))
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))
