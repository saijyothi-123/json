# sort the result by using keys:
import json
x={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
print(json.dumps(x, indent=4, sort_keys=True))

# o/p
# {
#     "1": 3,
#     "2": 4,
#     "4": 5,
#     "6": 7
# }