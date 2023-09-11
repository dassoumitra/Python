#Author - Soumitra Das                               Date - 05/01/2023
#(o) illustrate  deep copy.
import copy
a = [1,2,[3,4,5],6,[7,8,9,10],11]
print(a)
b = copy.deepcopy(a)
print(b)
