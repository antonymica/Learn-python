#coding:utf-8

n = 50
i = 0
while i < n:
	i+=1
	multiple = i * 13
	if multiple % 7 == 0:
		index = i
		print("{} x 13 = {}".format(index, multiple))
