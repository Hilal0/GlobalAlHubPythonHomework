list = []

name = str(input("Please enter a name:"))
lastname = str(input("Please enter a lastname:"))
age = int(input("Please enter a age:"))
dateofbirth = int(input("Please enter a dateofbirth:"))

list.append(name)
list.append(lastname)
list.append(age)
list.append(dateofbirth)

for i in list:
    print(i)

print(list)

if age >= 18 :
    print("You can go out to the street")
elif age > 0 and age < 18:
    print("You can't go out because it's too dangerous")
else:
    print("You entered your age wrong")