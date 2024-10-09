# Write a program that reads two integer numbers X and Y. Print all numbers between X and Y which dividing it by 5 the rest is equal to 2 or equal to 3.

n1 = input(int(""))
n2 = input(int(""))

if n1 > n2:
    n1, n2 = n2, n1
    
for i in range (n1+1,n2):
    if i % 5 == 2 or i % 5 == 3:
        print (i)