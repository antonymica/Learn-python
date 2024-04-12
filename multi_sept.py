#coding:utf-8

n = 20
i=0
while i < n:
	i += 1
	print(i*7 ,end=" ")
	if (i*7 % 3) == 0:
		print("*", end=" ")

