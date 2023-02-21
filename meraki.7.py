# 7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29

import json
x="""{
    "Name": "Abhishek",
    "Designation": "CEO of navgurukul",
    "Gender":"male",
    "Age": "29"
    }"""
y=json.loads(x)
z=json.dumps(y,indent=4)
print(z)


