https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

1. Write a Python program to calculate the sum of a list of numbers.
lst=list(map(int, input("enter number:").split()))
print(sum(lst))

or
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])

2. Write a Python program to converting an Integer to a string in any base.
   def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(2835,16))

3. 
