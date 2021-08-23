# dic1=[1,10,2,20,20,1,2]
# h=[]
# n={}
# for i in (dic1):
#     h.append(i)
#     s=h.count(i)
#     n.update({i:s})
# print(n)

# dic1=[10,12,13,14]
# dict2=[2,4,5,6]
# n={}
# for i in range(len(dic1)):
#     # for x in range(len(dict2)):
#         n[dic1[i]]=dict2[i]
# print(n)


   # Question n0.3
# dic1=[10,12,13,14]
# dict2=[2,4,5,6,]
# n={}
# for i in range(len(dic1)):
#     for x in range(len(dict2)):
#         n[dic1[i]]=dict2[i]
#     print(n)


# n={}
# k=["komal",12,"dhanu",13,"pournima",14,"kajal",15]
# keys=[]
# values=[]
# for i,j in enumerate(k):
#     if i%2==0:
#         keys.append(j)
#     else:
#         values.append(j)
# print(dict(zip(keys,values)))

# from typing import Dict


# k=["komal",12,"tina",14,"shri",13]
# dict={}
# i=0
# while i <len(k):
#     dict[k[i]]=(k[i+1])
#     i=i+2
# print(dict)

k=[1,4,6,7,10,15,19]
i=0
b=[]
while i<len(k):
   a=k[i]
   if a not in b:
      b.append(a)
   i=i+1
print(b)














