# Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) kar 
# de. Input :- 
a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
sorted_dict=dict(sorted(a.items(),
                        key=lambda item:item[1],
                        reverse=False))
                                                
print(sorted_dict)
