# this file includes random and counter examples
from random import *
from collections import Counter


lst=["GS","BJK","FB","TS","YMS"]
print(Counter(choices(lst, k=34)))
print(Counter(choices(lst, k=10000)))
print(Counter(choices(lst,[3,5,3,2,4], k=10000)))
shuffle(lst)
print(lst)
print(choices(lst,k=3))
print(sample(lst,k=3))
print(sorted(sample(range(1,44),k=4)))