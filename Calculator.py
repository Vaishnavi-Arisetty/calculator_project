# Committing changes to github new

import math as m

print("Calculator Operations\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Square\n"
      "6. Square Root\n"
      "7. Sine\n"
      "8. Cosine\n"
      "9. Tangent\n"
      "10.Log\n"
      "11.Reciprocal")
operationNumber = int(input("Enter the respective number you want to perform operation: "))
if operationNumber > 4:
    number = float(input("Enter the number: "))
else:
    number1 = float(input("Enter number1: "))
    number2 = float(input("Enter number2: "))


def add(number_1, number_2):
    return number_1 + number_2


def sub(number_1, number_2):
    return number_1 - number_2


def multiply(number_1, number_2):
    return number_1 * number_2


def divide(number_1, number_2):
    return number_1 / number_2


def square(num):
    return num ** 2


def square_root(num):
    return m.sqrt(num)


def sine(num):
    return m.sin((m.pi / 180) * num)


def cosine(num):
    return m.cos((m.pi / 180) * num)


def tangent(num):
    return m.tan((m.pi / 180) * num)


def logarithm(num):
    return m.log10(num)


def reciprocal(num):
    return 1 / num


if operationNumber == 1:
    print(f'Addition of {number1} and {number2} is {add(number1, number2)}')
elif operationNumber == 2:
    print(f'Subtraction of {number1} and {number2} is {sub(number1, number2)}')
elif operationNumber == 3:
    print(f'Multiplication of {number1} and {number2} is {multiply(number1, number2)}')
elif operationNumber == 4:
    print(f'Division of {number1} and {number2} is {divide(number1, number2)}')
elif operationNumber == 5:
    print(f'Square of {number} is {square(number)}')
elif operationNumber == 6:
    print(f'Square Root of {number} is {square_root(number)}')
elif operationNumber == 7:
    print(f'Sine of {number} is {sine(number)}')
elif operationNumber == 8:
    print(f'Cosine of {number} is {cosine(number)}')
elif operationNumber == 9:
    print(f'Tangent of {number} is {tangent(number)}')
elif operationNumber == 10:
    print(f'Logarithm of {number} is {logarithm(number)}')
else:
    print(f'Reciprocal of {number} is {reciprocal(number)}')
