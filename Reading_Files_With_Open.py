file = open("/Users/tibi/test20032021/newyear/test3.txt","r")
file.name
file.mode
FileContent = file.read()
FileContent
print(FileContent)
type(FileContent)
file.close()
file.closed

with open("", "r") as file:
    file.read()
    file.name
    file.close()
with open("", "r") as File:
    File.read()
    File.readline()

with open("/Users/tibi/test20032021/newyear/test3.txt","r") as file1:
    i = 0
    for line in file1:
        print("Iteration ", str(i), ":", line)
        i = i + 1

with open("/Users/tibi/test20032021/newyear/test3.txt","r") as file1:
    FileasList = file1.readlines()
    FileasList
