# Dictonary data structure
# --------------------------
''' 
List, Tuple, Set, --> Represent individual objects as entity represent indivodual objects as a 
key-value pairs --> Dictionary
Duplicate Keys are not allowed but duplicate vaues are allowed

Heteregenous* objects are allowed. *Different types of data
Insertion order is preserved
Dynamic(Increase or decrease the dictonary) and Mutable
Indexing and Sclicing are not applicable 
'''

"""
Important Funcations on Dictionary
----------------------------------
len()
clear()
dict.get(key)  ---> returns None

dict.get(key,default value) --> when no key it returns default value
pop(key) --> when specific key is not available it will raise key error
popitem() --> it removes random entry
keys() --> to get only key
values() --> to get only values
items() --> (key, value) -- it's tuple
copy() --> clone dict
update() -> dict.update({1:'mre',3:'test'}) like this
"""

"""
Dictionary Comprehension
------------------------
{expression for item in iterable_object if condition}
Below is example
"""
# d = {x:x*x for x in range(1,6)}
# print(d)

word = 'Bhaskar'
d = {}
for i in word:
    d[i] = d.get(i, 0)+1
print(d)

for k, v in d.items():
    print(k, 'Occured', v, 'times')
