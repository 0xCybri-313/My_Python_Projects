import random

def ops():
    deg = ["8g9fioeerfy34t-HaCkf9ibfv-yr23h=usgq0e", "aoishdHAcKcf90iuh0y2=2mj9-*&$093h(&#h9f-3*&#", "^gfsg*fyi3*&h4tiuha7*&4hHACKfh*&#jo3544rr55"]
    while True:
        i = random.randrange(0, 3)
        print(deg[i])

inp = input('''Enter "password" or "quit" : ''')
if inp == "quit":
    print("Wellcome Hacker")
else:
    raise ValueError(ops())

