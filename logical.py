a=[1,2,4,2,1,3,3,2,4,5,2]
x={}
for i in a:
    y=a.count(i)
    x.update({i:y//2})
print("pair",x) 

