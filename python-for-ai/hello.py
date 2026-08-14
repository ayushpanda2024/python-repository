print("Hello, World!")
print("This is a simple Python script for AI enthusiasts.")
str1 = "atrrrr" 
str2 = "Hello,AI!"
final  = str1 + str2
age = 12
vote = age >= 18
print(vote)

temperature = 24
if temperature > 30:
    print("it is veryhot")
elif temperature > 25:
    print("it is  hot") 
else:
    print("it is nice weather")   



def greet():
    print("Hello, welcome to the AI world!")

greet()
greet()

def check_weather(temp):
    if temp > 30:
        print(f"it is very hot{temp} degrees")
    elif temp > 25:
        print(f"it is hot {temp} degrees") 
    else:
        print(f"it is nice weather at {temp} degrees")
check_weather(28)
check_weather(31)

def plus(a,b):
       return(f"The result of {a} + {b} is: {a+b}")
def minus(a,b):
         return(f"The result of {a} - {b} is: {a-b}")
a= int(input("Enter first number: "))
input_operator = input("Enter operator (+ or -): ")
b= int(input("Enter second number: "))
if input_operator == "+":
    plus(a,b)
elif input_operator == "-":
    minus(a,b)

