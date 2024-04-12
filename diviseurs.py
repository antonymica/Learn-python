#coding:utf-8

nbr = int(input("Enter the number : "))

for i in range(1, nbr):
    if nbr % i == 0:
        print(i, end="; ")