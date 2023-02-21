
# Dump():- Dump() method python objects ko json file mai store karane ke liye use hota hai. 
# Dump() method json files par hi kaam karta hai aur python objects ko ek argument ki tarah store karta hai.

# Example:-python object(dictionary) ko hum json file mai dump.


import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}

out_file = open("myfile.json", "w")
  
json.dump(dict1, out_file, indent = 6)
  
out_file.close()
