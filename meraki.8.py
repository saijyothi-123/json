


import json

x={ 
     "emp1":
     { "name":"nilam",
       "Designation":"programmer",
       "Age":"34",
       "salary":"24000",
         }

    "emp2":
      { "name":"komal",
        "Designation":"Trainee",
        "Age":"24",
        "salary":"20000" ,
        }

 
    "emp3":
       { "name":"anuradha",
         "Designation":"HR",
         "Age":"25",
         "salary":"40000",
         }


    "emp4":
       { "name":"Abhishek",
         "Designation":"Manager",
         "Age":"29",
       }
            
     
  }

y=json.dumps(x,indent=4)
print(y)