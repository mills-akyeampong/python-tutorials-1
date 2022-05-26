#creating user inputs

#user input 1
print("What is your First Name")
fname=input()
print("What is your Last Name")
lname=input()
print("Hello " + fname + " " + lname)

#user input 2
print("What is your favorite animal?")
animal=input()
print("Name a famous Building")
Building=input()
print("What is your favorite color?")
color=input()
print("HIckory Dickory Dock!")
print("The " +color+ " ran up the "+Building)


message="Hello World!"
print(message.lower())
print(message.upper())
print(message.swapcase())


print("What Country do you come from?")
country=input()
country = country.upper()
print("Hello, you are from "+country)


message="Hello World"
print(message.find("World"))
print(message.count("o"))
print(message.capitalize())
print(message.replace("Hello", "Funny"))

#Postal Code
print("Hello, welcome to the postal address unit. Kindly enter your postal code below:")
postalcode=input()
print(postalcode.upper())