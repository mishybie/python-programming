# import mathematics
#import operators
#import others




# x=mathematics.add(12,34)
# print(x)

# y=mathematics.subtract(45,89)
# print(y)


# from mathematics import subtract

# x=add(23,45)
# y=subtract(89,34)

# print(x)

##get numbers
import operators
import others
import trigonometric
if operators=="cube":
        num=eval(input("Enter number:"))
        x=others.cube(num)
        print(x)

elif operators=="sin":
        angle=eval(input("Enter angle in degrees:"))
        sin_of_angle =trigonometric.get_sine(angle)
        print(sin_of_angle)
else:
    num1=eval(input("Enter number 1:"))
    num2=eval(input("Enter a number 2:"))
    operator=input("Enter operator:")

    if operator=="+":
        x=operator.add(num1,num2)
        print(x)

    elif operator=="-":
        x=operator.subtract
        print(x)

    elif operator=="/":
        x=operator.divide(num1,num2)
        print(x)

    elif operator=="*"or"*"or"*":
        x=operator.multiply(num1,num2)



