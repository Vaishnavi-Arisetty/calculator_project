import math as m
import numpy as np


class Calculator:

    def __init__(self, *number):
        self.__number = number[0]

    def add(self):
        return sum(self.__number)

    def sub(self):
        return self.__number[0] - self.__number[1]

    def multiply(self):
        return np.prod(self.__number)

    def divide(self):
        return self.__number[0] / self.__number[1]

    def square(self):
        return list(map(np.square, self.__number))

    def square_root(self):
        return list(map(m.sqrt, self.__number))

    def sine(self):
        return list(map(m.sin, (m.pi / 180) * np.array(self.__number)))

    def cosine(self):
        return list(map(m.cos, (m.pi / 180) * np.array(self.__number)))

    def tangent(self):
        return list(map(m.tan, (m.pi / 180) * np.array(self.__number)))

    def logarithm(self):
        return list(map(m.log10, self.__number))

    def reciprocal(self):
        return list(map(np.reciprocal, self.__number))

    def update_values(self, *number):
        self.__number = number[0]

    def calling_operations(self, operation_number):
        switcher = {
            1: f'Addition of given numbers is {self.add()}',
            2: f'Subtraction of given numbers is {self.sub()}',
            3: f'Multiplication of given numbers is {self.multiply()}',
            4: f'Division of given numbers is {self.divide()}',
            5: f'Square of given numbers is {self.square()}',
            6: f'Square Root of given numbers {self.square_root()}',
            7: f'Sine of given numbers is {self.sine()}',
            8: f'Cosine of given numbers is {self.cosine()}',
            9: f'Cosine of given numbers is {self.cosine()}',
            10: f'Logarithm of given numbers is {self.logarithm()}',
            11: f'Reciprocal of given numbers is {self.reciprocal()}'
        }
        return switcher.get(operation_number)


class CallingCalculator:
    def __init__(self):
        self.calculator = None
        self.num = []
        self.c = 'c'
        self.op_num = 0

    def printing_operations(self):
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
              "11.Reciprocal\n")
        self.num = list(
            map(int, input("Enter the numbers you want to perform operation separated by space: ").split(" ")))
        self.calculator = Calculator(self.num)
        self.user_side_functions()

    def get_user_interest(self):
        self.c = input("If you want to exit enter 'e' \n"
                       "If you want to update the values enter 'u' \n"
                       "If you want to continue enter 'c' \n"
                       "Enter the variable : ")

    def user_side_functions(self):
        while self.c != 'e':
            if self.c == 'u':
                self.num = list(map(int, input("Enter the updated values separated by space: ").split(" ")))
                self.calculator.update_values(self.num)
                self.op_num = int(input("Enter the respective number you want to perform operation: "))
                print(self.calculator.calling_operations(self.op_num))
                self.get_user_interest()
            else:
                self.op_num = int(input("Enter the respective number you want to perform operation: "))
                print(self.calculator.calling_operations(self.op_num))
                self.get_user_interest()


call = CallingCalculator()
call.printing_operations()
