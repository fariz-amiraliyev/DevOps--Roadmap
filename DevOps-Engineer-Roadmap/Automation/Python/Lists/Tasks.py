
https://www.w3resource.com/python-exercises/list/#EDITOR

1. Write a Python program to sum all the items in a list. Go to the editor
Click me to see the sample solution

2. Write a Python program to multiplies all the items in a list. Go to the editor
Click me to see the sample solution

3. Write a Python program to get the largest number from a list. Go to the editor
Click me to see the sample solution

4. Write a Python program to get the smallest number from a list. Go to the editor
Click me to see the sample solution

5. Write a Python program to count the number of strings where the string length is 2 or more and the
first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
Click me to see the sample solution

6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple
from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
Click me to see the sample solution

7. Write a Python program to remove duplicates from a list. Go to the editor
Click me to see the sample solution

8. Write a Python program to check a list is empty or not. Go to the editor
Click me to see the sample solution

9. Write a Python program to clone or copy a list. Go to the editor
Click me to see the sample solution

10. Write a Python program to find the list of words that are longer than n from a given list of words. Go to the editor
Click me to see the sample solution

11. Write a Python function that takes two lists and returns True if they have at least one common member. Go to the editor
Click me to see the sample solution

1.84. Write a Python program to round the numbers of a given list, print the minimum and
maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order
separated by space. Go to the editor
Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
Minimum value: 4
Maximum value: 22
Result:
20 25 45 55 60 70 80 90 110

nums = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20,5.19,5.18, 17.50]
print("Original list:", nums)
numbers=list(map(round,nums))
print("Minimum value: ",min(numbers))
print("Maximum value: ",max(numbers))
numbers=list(set(numbers))
numbers=(sorted(map(lambda n:n*5,numbers)))
print("Result:")
for numb in numbers:
    print(numb,end=' ')

2. Write a Python program to round every number of a given list of numbers and print
the total sum multiplied by the length of the list.

nums = [22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]
print("Original list: ", nums)
print("Result:")
lenght=len(nums)
print(sum(list(map(round,nums))* lenght))


3. 82. Write a Python program to generate the combinations of n distinct objects
   taken from the elements of a given list. Go to the editor;
   def combination(n, n_list):
    if n<=0:
        yield []
        return
    for i in range(len(n_list)):
        c_num = n_list[i:i+1]
        for a_num in combination(n-1, n_list[i+1:]):
            yield c_num + a_num
n_list = [1,2,3,4,5,6,7,8,9]
print("Original list:")
print(n_list)
n = 2
result = combination(n, n_list)
print("\nCombinations of",n,"distinct objects:")
for e in result:
     print(e)

12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

or

for x in s:
    if s.index(x) in [2,3]:
        s.remove(x)
print(s)

13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
   arr=[[["*" for col in range(3)] for col in range(3)] for row in range(5)]

 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
num = [7,8, 120, 25, 44, 20, 27]
nums=sorted([x for x in num if x%2==0])

15.18. Write a Python program to generate all permutations of a list in Python.
import itertools
print(list(itertools.permutations([1,2,3])))

16. 19. Write a Python program to get the difference between the two lists.
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)

17. 71. Write a Python program to check whether all dictionaries in a list are empty or not.
my_list = [{},{},{}]
my_list1 = [{1,2},{},{}]
print(all(not d for d in my_list))
print(all(not d for d in my_list1))
