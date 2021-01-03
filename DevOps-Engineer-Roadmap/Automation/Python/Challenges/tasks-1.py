https://www.w3resource.com/python-exercises/challenges/1/index.php

1. Write a Python program to check if a given positive integer is a power of two.

def is_Power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0


2. Write a Python program to check if a given positive integer is a power of three.

def is_Power_of_three(n):
    while (n % 3 == 0):
         n /= 3;
    return n == 1;

3.  def is_Power_of_three(n):
    while (n % 3 == 0):
         n /= 3;
    return n == 1;

4.     
