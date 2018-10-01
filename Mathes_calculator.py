HOUSING = float(input("Enter how much you pay for your housing: "))
if HOUSING<0:
    HOUSING = float(input("Please, enter a valid number: "))

ELETRIC = float(input("Enter the sum of your last 3 electric bills: "))
if ELETRIC<0:
    ELETRIC = float(input("Please, enter a valid number: "))
ELETRIC_AVERAGE = ELETRIC/3

CELLPHONE = float(input("Enter how much you pay for your cellphone: "))
if CELLPHONE<0:
    CELLPHONE = float(input("Please, enter a valid number: "))

GROCERIES = float(input("Enter how much you pay for your groceries: "))
if GROCERIES<0:
    GROCERIES = float(input("Please, enter a valid number: "))

PAYCHECK = float(input("How much is your monthly income? "))
if PAYCHECK<0:
    PAYCHECK = float(input("Please, enter a valid number: "))

INTERNET = float(input("Enter how much you pay for your internet: "))
if INTERNET<0:
    INTERNET = float(input("Please, enter a valid number: "))

MONTHLY_OUT = HOUSING + ELETRIC_AVERAGE + CELLPHONE + GROCERIES + INTERNET
BUDGED = PAYCHECK - MONTHLY_OUT

print("Your monthly expense is ", format(MONTHLY_OUT, '.2f'))

GOAL = float(input("What is your goal? Do you know how much it will cost? Enter the total value: "))
SAVINGS = GOAL - BUDGED
TIME_IN_MONTHS= GOAL/BUDGED

print("This is the amount you should save to get your goal:", format(SAVINGS,'.2f'),
      "and you should be able to reach it in", format(TIME_IN_MONTHS, '.1f'), "months")
