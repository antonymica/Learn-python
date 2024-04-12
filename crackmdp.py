import random
import pygame

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
chars_list = list(chars)

password = pygame.password("Enter a password : ")

guess_password = ""

while (guess_password != password):
    guess_password = random.choice(chars_list, k=len(password))

    print("<===================="+ str(guess_password) +"===================>")

    if (guess_password == list(password)):
        print("Your password is : "+ "".join(guess_password))
        break