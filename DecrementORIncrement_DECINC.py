"""
Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4 otherwise decrement its value by 1.

Input:
First line will contain a number N.

Output:
Output a single line, the new value of the number.

Constraints
0≤N≤1000

Sample Input:
5

Sample Output:
4
"""

n = int(input())
if n%4==0:
    n+=1
    print(n)
else:
    n-=1
    print(n)