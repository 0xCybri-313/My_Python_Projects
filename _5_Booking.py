def greet():        # Creat a function using Time module
    import time
    timestamp = int(time.strftime("%H"))
    if timestamp >= 4 and timestamp <= 11:
        print("\nGood Morning Mr./Mrs.", end=" ")
    elif timestamp >= 12 and timestamp <=18:
        print("\nGood Afternoon Mr./Mrs.", end=" ")
    else:
        print("\nWellcome Mr./Mrs.", end=" ")

def finalans(ans, cos): # Simple Funtion to avoid repeataion
    if ans == "y":
        print("\ncontact : +92355 555 5555")
    else:
        print("\nThanks Mr./Mrs.", cos, "Have a nice Day")

ti = "To check which Room is sutable for Guest\n"
print(ti.center(100))
cos = (input("Enter name of Coustomer : "))

greet() # Calling Greet Function
print(cos)

nop = int((input("\nPlease Enter Number of people : ")))
fam = (input("\nIs it family or not : y/n : "))

room = [101, 102, 103, 201, 202 ,203] # List of Room in our Guest House ref as Name of room
froom = room.copy() # Just creat another List for Family Room
froom.remove(103); froom.pop(4) # Use remove and pop to remove item from List

if fam == "y":
    if nop <= 2:
        print("\n", froom[0], froom[2], "These Room are best for", cos, "\n")
    elif nop <= 4:
        print("\n", froom[1], "This room is best for", cos, "\n")
    elif nop <=6:
        print("\n", froom[3], "This room is best for", cos, "\n")
    else:
        ans = input("\nSorry we have no Rooms for you But we can arrange for you if you like y/n : ")
        finalans(ans, cos) # Calling Finalans function

else:
    if nop <= 3:
        print("\n", room[2], "This room is best for", cos)
    elif nop <=5:
        print("\n", room[5], "This room is best for", cos)
    else:
        ans = input("\nSorry we have no Rooms for you But we can arrange for you if you like y/n : ")
        finalans(ans, cos) # caling Finalans Function