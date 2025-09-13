import random
import string

def reverse(letter):
    return letter[::-1]

def alpha():
    for i in range(3):
        fix = ranalpha.split(" ")[random.randrange(0, 81)]
        print(fix, end = "")


sc = ("Please explain which type of coffee do you like")
ranalpha = '''A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z ! @ # $ % ^ & * ( ) _ { } | ? / ; [ ] 1 2 3 4 5 6 7 8 9 0'''

for letter in sc.split(" "):
    if len(letter) < 3:
        print(reverse(letter), end = " ")
    else:
        letter = f"{letter.strip(letter[0])}{letter[0]}"
        letter = reverse(letter)
        alpha()
        print(letter, end = "")
        alpha()
        print(end=" ")
