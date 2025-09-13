print("Calulation of 2 Numbers/n Enter a number :   ")
#Enter 2 numbers
num1 = int(input())
num2 = int(input())
print("Enter Opterator : (/,*,+,-)")
#Enter Opertrator
opt = input()
#Use if/else to select operator
if opt == "/":
    ans = int(num1 / num2)
    print(ans)
elif opt == "*":
    ans = int(num1 * num2)
    print(ans)
elif opt == "+":
    ans = int(num1 + num2)
    print(ans)
elif opt == "-":
    ans = int(num1 - num2)
    print(ans)
else:
    print("Optertion is Invalid")