"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculate():
    while True:
        input_string = raw_input("> ")
        tokens = input_string.split(" ")
        token_zero = tokens.pop(0)
        if token_zero == "q" or token_zero == "quit":
            break
        for current_index in range(len(tokens)):         
            try:
                type(tokens[current_index])
                num = int(tokens[current_index])
                tokens[current_index] = num
                type(tokens[current_index])
                # if len(tokens) > 1:
                #     num = int(tokens[i+1])
            except ValueError:
                print "Please enter only numbers for the second and third values."
                continue
        # specify that we can't accept a string other than square, cube, power, or modulus for token_one
        # also specify that if when we try to convert num_one and num_two into integers, and it doesn't work, we want to output "enter a number"
        if token_zero == "+":
            print add(num_one, num_two)
        elif token_zero == "-":
            print subtract(num_one, num_two)
        elif token_zero == "*":
            print multiply(num_one, num_two)
        elif token_zero == "/":
            print divide(num_one, num_two)
        elif token_zero == "square":
            print square(num_one)
        elif token_zero == "cube":
            print cube(num_one)
        elif token_zero == "power":
            print power(num_one, num_two)
        elif token_zero == "modulus":
            print mod(num_one, num_two)
        else:
            print "I do not understand."

calculate()