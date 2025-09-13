# Write a programme that create a secret info encription.

import time
import random
import string
import _2_Greeting

def ops():
    deg = ["8g9fioeerfy34t-HaCkf9ibfv-yr23h=usgq0e", "aoishdHAcKcf90iuh0y2=2mj9-*&$093h(&#h9f-3*&#", "^gfsg*fyi3*&h4tiuha7*&4hHACKfh*&#jo3544rr55"]
    while True:
        i = random.randrange(0, 3)
        print(deg[i])

def ranalpha(letter):
    for i in range(6):
        if i == 3:
             swap(letter)
             print(end = "")
        fix = str(random.choice(string.ascii_letters + string.digits + '@#$%&[{()}]?'))
        print(fix, end = "")        
    return ("")

def swap(letter):
    for i, k in enumerate(letter) :
        if i%2 == 0:
            print(k.upper(), end = "")
        else:
            print(k, end = "")
    return ("")

def reverse(letter):
    letter = letter[::-1]
    return letter

def delalpha(letter):
    letter = letter[3:-3]
    return letter

# ______________________main programme_____________________

inp = input('''Enter "password" or "quit" : ''')
if inp == "quit":
    print(f"{_2_Greeting.greet()}Hacker")

    ans = input('''\nWould you like to take "Coffee" or "Tea" : ''') # To encrypt code type 'coffee'/ To decode type Tea

    match ans.lower():
        
        case "coffee":
            code = input('''\nPlease explain which type of coffee do you like : ''') # Type secret code here
            print("\n\n")
            
            for letter in code.split(" "):
                if len(letter) <= 2:
                    ranalpha(reverse(letter))
                    print(end = " ")            

                else:
                    letter = f"{letter.strip(letter[0])}{letter[0]}" 
                    ranalpha(reverse(letter))
                    print(end = " ")

            print("\n\n\n\nLove it\n")

        case "tea":

            code = input('''\nPlease explain which type of Tea do you like : ''') # Paste secret code here to decode
            print("\n\n")

            for i, letter in enumerate(code.split(" ")):
                letter = delalpha(letter)
                if len(letter) <= 2:
                    letter = reverse(letter)
                    if i == 0:
                        print(letter.capitalize(), end = " ")
                    else:
                        print(letter.lower(), end = " ")

                else:
                    letter = reverse(letter)
                    letter = f"{letter[len(letter) - 1]}{letter.strip(letter[len(letter) - 1])}"
                    if i == 0:
                        print(letter.capitalize(), end = " ")
                    else:
                        print(letter.lower(), end = " ")
            
            print("\n\n\n\nSorry\n")
        case _ :
            print("""\n\n\nPress Win + 'y' and 'x''x'\n\n\n""")

else:
    raise ValueError(ops())

input()