#Trenton Smith ----- 11/17/2021 ----- 4:35pm.
#creating a password generator.

import random

#random characters that will be chosen.

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567!$#%&^*(%"

#Questioning user on length of passwords & amount of passwords.

while 1:
    password_len = int(input("Enter length of your password: "))
    password_count = int(input("Enter amount of passwords you'd like: "))

#Instructions on creating random passwords.

    for x in range(0,password_count):
        password= ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password +  password_char
        print ("Your password is:", password)
