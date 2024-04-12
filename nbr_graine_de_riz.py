#coding:utf-8

i = nbrGrain = 0
while i < 64:
	i += 1
	nbrGrain += i

nbrGrainInt = int(nbrGrain)
nbrGrainFloat = float(nbrGrain) 

print("Grain de riz : {} \t {} ".format(nbrGrainInt, nbrGrainFloat))