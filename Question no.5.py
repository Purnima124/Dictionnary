# Do lists lekar ek dictionary banaiye jisme pehli list ke elements 
# keys ho aur dusri list ke elements unn keys ki values ho. Example :- 
# Input :-
 
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]  
dict={}
for i in range(len(list1)):
    dict[list1[i]]=list2[i]
print(dict)
