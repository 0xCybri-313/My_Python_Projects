#very nice session keep doing it.
print("Practice of if/else and Loop\nEnter year in which you born: ")
year = int(input())
if year <= 2000:
    age = 2023 - year
    print("your Age is" , age ,"and your are eligiable for this team")
    for i in range(year, 2023+1):
        print(i)
else:
    req = year - 2000
    reqyear = 2023 + req
    print("Your are not eligiabal for this team yet your have to wait until year of", reqyear, "you need", req, "more year for this team.")
    for i in range(2023, reqyear):
        print(i ,end=",")
