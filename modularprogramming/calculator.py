#this is a calculator project

number1=eval(input("Enter first number"))
number2=eval(input("Enter second number"))

operator=input("Enter operator:")

def add(num1,num2):
    result=num1+num2
    return result

def subtract(num1,num2):
    result=num1-num2
    return result

def divide(num1,num2):
    result=num1/num2
    return result

def multiply(num1,num2):
    result=num1*num2
    return result


if operator =="+":
    add(number1,number2)
elif operator=="-":
    subtract(number1,number2)
elif operator=="/":
    divide(number1,number2)
elif operator=="x" or operator:
    multiply(number1,number2)
