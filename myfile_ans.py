# ["neelam","programer","24","2400",],
# ["komal","trainer","24","20000"],
# ["anuradha","HR","25","40000"],
# ["Abhishek","manager","29","63000"]


import json
a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","salary"]
d1={}
d2={}
d3={}
d4={}
i=0
while i<len(e):
    d1[e[i]]=a[i]
    d2[e[i]]=b[i]
    d3[e[i]]=c[i]
    d4[e[i]]=d[i]
    i=i+1
x = dict(emp1= d1, emp2 = d2, emp3= d3,emp4=d4)
# print(d1)
# print(x)
openfile=open("myfile1.txt","w")
json.dump(x,openfile,indent=4)
openfile.close()
    