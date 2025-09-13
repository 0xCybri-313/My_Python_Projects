import os

def change_name(name, i):
    new_name = name.replace(".", "")
    # new_name = name.replace(f" ", f"_")
    return new_name

list_py = os.listdir("D:\Backup\Download\Python\My Python Projects")
        
for i, name in enumerate(list_py, start = 1):
    if name.endswith(".py"):
        new_name = name.rstrip(".py")
        new_name_2 = change_name(name, i)
        new_name_3 = new_name_2 + ".py"
        os.rename(name, new_name_3)