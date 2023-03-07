import math

def with_draw(amount, number):
    if amount > 0 and number > 0:
        return amount - number
    elif amount <= 0:
        return "No enough money"
    elif number < 0:
        return "Enter correct number"
    else:
        return "Error"

def deposit(amount,number):
    if( number > 0):
        return amount + number
    else:
        return "Enter valid number of deposit"

def showAmount(value):
    print(value)

def exchangeToUsd(amount):
    if amount == 0:
        return 0
    elif amount < 0:
        return "No money"
    elif amount > 0:
       return amount / 4.45
def exchangeToPln(amount):

    if amount == 0:
        return 0
    elif amount < 0:
        return "No money"
    elif amount > 0:
       return math.floor(amount * 4.45)



