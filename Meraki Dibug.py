# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result) 

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])

# print(person[4])

# result = person[4]['place']

# print(result) 

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])

# print(person[4])

# result = person[4]['place']

# print(result) 


# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }

# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic) 

# dic= {
#    'Name': 'RAM',
#    'Age': 17,
#     }
# dic['student']={
#        'id':22, 
#        'place':'dharamsala'
#    }
# print(dic) 

# car ={
#     "brand":  "ford",
#     "model":  "mustang",
#     "year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.") 


# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()
# print(mydict) 

# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#       print(state) 


dic= {
        
1: 'NAVGURUKUL',
2: 'IN',  
3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
del dic[3]['A']
print(dic)


