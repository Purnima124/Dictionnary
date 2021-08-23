from collections import Counter
my_dict={
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
b=[]
k=Counter(my_dict)
high=k.most_common(3)
for i in high:
    b.append(i[1])
print(b)



# print("Dictionary with 3 highest values:")
# print("keys:values")
    # highest=max(my_dict.values())
# print(highest)
# print(i[0],":",i[1]," ")
