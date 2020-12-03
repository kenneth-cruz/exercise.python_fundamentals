# Created by Leon Hunter at 9:54 AM 10/23/2020
class Calculator(object):
    def add(self, a, b):
        sum = a + b
        return sum

    def subtract(self, a, b):
        difference = a - b
        return difference

    def multiply(self, a, b):
        product = a * b
        return product

    def divide(self, a, b):
        quotient = a / b
        return round(quotient, 3)
