import os
f = open("New.txt", "r")
data = f.read()
print(data)

os.remove("New.txt")
f.close()