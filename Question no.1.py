# Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary
#  me aa jaaye jaise ki niche Expected result me diya gaya hain or jisski 
#  bhi keys same hai unki values add ho jai. Example :- Input :- Output

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for key in dic1:
    if key in dic2:
        dic2[key]=dic1[key]+dic2[key]
        dic2.update(dic3)
    else:
        dic2[key]=dic1[key]
print(dic2)
    

 # city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population)) 
