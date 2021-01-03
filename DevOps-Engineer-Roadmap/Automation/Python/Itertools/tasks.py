1. Write a Python program to create an iterator from several iterables in a sequence and display the type and elements of the new iterator.

from itertools import chain
def chain_f(l1,l2,l3):
    return (l1,l2,l3)

f=chain_f([1,2,3],["a","v","f"],[3,5,7])
f
print(f)
([1, 2, 3], ['a', 'v', 'f'], [3, 5, 7])
f
type(f)
tuple

2. Write a Python program to generate the running product of the elements of an given iterable.

from itertools import accumulate
import operator
def running_product(it):
    return accumulate(it,operator.mul)

#List
result = running_product([1,2,3,4,5,6,7])
print("Running product of a list:")
for i in result:
    print(i)

3. Write a Python program to generate the running maximum, minimum value of the elements of an iterable.

from itertools import accumulate
def running_max_product(iters):
    return accumulate(iters, max)
#List
result = running_max_product([1,3,2,7,9,8,10,11,12,14,11,12,7])
print("Running maximum value of a list:")
for i in result:
    print(i)
#Tuple
result = running_max_product((1,3,3,7,9,8,10,9,8,14,11,15,7))
print("Running maximum value of a Tuple:")
for i in result:
    print(i)
def running_min_product(iters):
    return accumulate(iters, min)
#List
result = running_min_product([3,2,7,9,8,10,11,12,1,14,11,12,7])
print("Running minimum value of a list:")
for i in result:
    print(i)
#Tuple
result = running_min_product((1,3,3,7,9,8,10,9,8,0,11,15,7))
print("Running minimum value of a Tuple:")
for i in result:
    print(i)

4. >>> [x for x in itertools.permutations('123')]
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> [x for x in itertools.permutations('123',2)]
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>

5. 
