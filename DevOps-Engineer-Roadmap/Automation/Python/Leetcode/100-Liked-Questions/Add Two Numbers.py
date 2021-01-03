You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


#as a list

def find_sum(l1,l2):
    ll=int("".join([str(x) for x in l1]))
    ln=int("".join([str(x) for x in l2]))
    l3=ll+ln
    new=[]
    for x in str(l3):
        new.append(int(x))
    print(new)
