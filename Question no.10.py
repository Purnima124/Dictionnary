a={
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
t=0
for i in a:
   i=a[i]
   count=len(i)
   t=t+count
print("Total count",t)