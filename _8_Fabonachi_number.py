def fabonachi(num):
    if num <= 1 :
        return 0
    else:
        return (num - 2) + (num - 1)
    
numbers = range(1, 15)
for num in numbers:
    fab = fabonachi(num)
    print(fab)