def greet():        # Creat a function Using Time module
    import time
    timestamp = int(time.strftime("%H"))
    if timestamp >= 4 and timestamp <= 11:
        print("\nGood Morning Mr./Mrs.", end=" ")
    elif timestamp >= 12 and timestamp <=18:
        print("\nGood Afternoon Mr./Mrs.", end=" ")
    else:
        print("\nWellcome Mr./Mrs.", end=" ")
    return ""


if __name__ == "__main__":
    greet() # Calling the greet function
    print("Hacker")