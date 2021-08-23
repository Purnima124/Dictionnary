# student1={"Name":"Rishab","Age":27}
# # print(student1)
# # upded
# student1["Age"]=28
# print(student1)

# Nested list
# a={1:{"cours":"python","fees":"15000"},
#    2:{"cours":"javascript","fees":"10000"}}
# print(a)

# Delete

# a={1:{"cours":"python","fees":"15000"},
#    2:{"cours":"javascript","fees":"10000"}}
# del a[1]["cours"]
# print(a)

# element
# a={1:{"cours":"python","fees":"15000"},
#    2:{"cours":"javascript","fees":"10000"}}
# print(len(a[2]))

# a={1:{"cours":"python","fees":"15000"},
#    2:{"cours":"javascript","fees":"10000"}}
# print(len(a))

# a={1:{"cours":"python","fees":"15000"},
#    2:{"cours":"javascript","fees":"10000"}}
# print(a[1]['cours'])
# print(a[1]['fees'])
# print(a[2]['cours'])
# print(a[2]['fees'])

# 2:{"cours":"javascript","fees":"10000"}}
# a[1]['cours']='machine Learning'
# a [1]["fees"]=200000
# a[2]['cours']="english"
# a[2]["fees"]="5000"
# print(a)

        # Add
# a={1:{"cours":"python","fees":"15000"},
# 2:{"cours":"javascript","fees":"10000"}}
# a[3]={"cours":"React Js","fees":"30000"}
# print(a)
       # update
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# b={'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# c={}
# for d in (a,b):
#         c.update(d)
# print(d)

k=[]
m=[]