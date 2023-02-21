# convert dict to json:
import json
x={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
a=input("enter the element you want to purchase")
b=int(input("enter the number of items"))
for i in a:
    if a[i][b]==a[i][b]:
        d=a[i][b]
        e=int(d)
        print("the remaining num of items are:",e-c)
        f={}
        dic={}
        n=e-c
    for key in a:
        for value in a[key]:
            f[value]=a[key][value]
            if value==b:
                f[value]=n
                dic[key]=f
                
with open("meraki9.json","w")as f:
    json.dump(dic,f,indent=4)


