import os


filelist = os.listdir("D:\Downloads\IMAGES\.PNG")
i = 1
for file in filelist:
    if file.endswith(".png"):
        os.rename(file, f"{i}.png")
        i = i + 1




