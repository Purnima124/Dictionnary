# User se 10 students ke naam aur marks lekar unhe ek dictionary me 
# store karaye. Output :- 
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56}

dict={}
# num=int(input("enter the number"))

for i in range(10):
    student_name=input("enter the student_name:")
    marks=input("enter the marks:")
    dict.update({student_name:marks})
print(dict)












