
str1 = input("Nhap string 1: ")
while 1>= len(str1) or len(str1)>=200:
    del str1
    str1 = input("Nhap string 1: ")

str2 = input("Nhap string 2: ")
while 1>=len(str2) or len(str2)>=200:  
    del str2
    str2 = input("Nhap string 2:")

print(str1.upper())
print(str2.upper())
print(str1.count(str2))
