#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1

    try:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        if b == 0:
            print("Error: Division by zero")
            return 1
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        return 1

    print(f"{a} {operator} {b} = {result}")
    return 0

if __name__ == "__main__":
    exit(main())

