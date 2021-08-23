# Ek program likhiye jisse ki agar di hui key pehle se
#  dictionary me exist karti ho toh “exists “ print
#  kare 
#  aur agar nahi karti ho to "not exists" print karega
# num=int(input("enter the number")) 

dict={"name":"Raju","marks":56}
key=input("enter the key")
if key in dict:
    print("exists")
else:
    print("not exists")    
