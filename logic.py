# Miraj
# Game Logic, select numbers and operations
# Algorithms
import random
import math

def elementary(userIn):
    
    if userIn is None:
        choice = random.randint(0,3)
    else:
        choice = userIn

    if choice == 0:
        operator = "+"
        num1, num2 = addition()
    
    elif choice == 1:
        operator = "-"
        num1, num2 = subtraction()

    elif choice == 2:
        operator = "*"
        num1, num2 = multiplication()
    
    elif choice == 3:
        num1, num2 = division()

    return num1, num2

def addition():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 200)
    return num1, num2
def subtraction():
    num1 = random.randint(1, 200)
    num2 = random.randint(1, num1 - 1)
    answer = num1 - num2
    return num1, num2
def multiplication():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    return num1, num2
def division():
    num2 = random.randint(1, 20)
    answer = random.randint(1, 50)
    num1 = num2 * answer
    return num1, num2

def advanced(userIn):
    """Advanced section"""
    if userIn is None:
        choice = random.randint(0,3)
    else:
        choice = userIn

    if choice == 0:
        a, b, c, discriminant, xPos, xNeg = quadratic()
        return a, b, c, discriminant, xPos, xNeg
    
    elif choice == 1:
        a, b, c = pythagorean()
        return a, b, c
    
    elif choice == 2:
        base, num, answer = logarithm()
        return base, num, answer

def quadratic():
    """Quadratic formula"""
    # Keeps working until there are solutions
    while True:
        a=random.randint(1,5)
        b=random.randint(-10,10)
        c=random.randint(-10,10)
        discriminant = (b**2)-(4*a*c)
        if discriminant > 0:
            square_root = math.sqrt(discriminant)
            xPos = round(((-b + square_root) / (2 * a)), 2)
            xNeg = round(((-b - square_root) / (2 * a)), 2)
            return a, b, c, discriminant, xPos, xNeg
        else:
            pass


def pythagorean():
    """Pythagorean theorem"""
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    c = round((math.sqrt((a**2 + b**2))), 2)
    return a, b, c

def logarithm():
    """Logarithm"""
    base = random.randint(2, 10)
    answer = random.randint(1, 5)
    num = base ** answer
    return base, num, answer