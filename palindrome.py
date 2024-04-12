#coding:utf-8

# Palindrome

def palindrome(mot):
    long = len(mot)
    i = 0
    while i < long-1:
        long -=1
        if mot[i] == mot[long]:
            vrai = True
        else:
            vrai = False
        i += 1

    return vrai


chaine = input("Entrer le mot: ")

if palindrome(chaine):
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")