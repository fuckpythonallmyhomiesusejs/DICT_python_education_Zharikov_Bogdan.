import argparse
import math

# create an argument parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--interest')
parser.add_argument('--annuity')
parser.add_argument('--payment')
parser.add_argument('--periods')

# parse the arguments
args = parser.parse_args()

# assign the arguments to variables
loan_type = args.type
principal = args.principal
interest = args.interest
annuity = args.annuity
payment = args.payment
periods = args.periods

# check the type of the loan and calculate accordingly
if loan_type == "annuity":
    if not annuity:
        principal = float(principal)
        periods = int(periods)
        interest_rate = float(interest) / (12 * 100)
        annuity = math.ceil(principal * (interest_rate * pow((1 + interest_rate), periods)) / (pow((1 + interest_rate), periods) - 1))
        overpayment = annuity * periods - principal
        print(f'Your monthly payment = {annuity}!\nOverpayment = {overpayment}')
    elif not principal:
        periods = int(periods)
        payment = float(payment)
        interest_rate = float(interest) / (12 * 100)
        principal = math.floor(payment / ((interest_rate * pow((1 + interest_rate), periods)) / (pow((1 + interest_rate), periods) - 1)))
        overpayment = payment * periods - principal
        print(f'Your loan principal = {principal}!\nOverpayment = {overpayment}')
    elif not periods:
        principal = float(principal)
        payment = float(payment)
        interest_rate = float(interest) / (12 * 100)
        periods = math.ceil(math.log((payment / (payment - interest_rate * principal)), 1 + interest_rate))
        years, months = divmod(periods, 12)
        if years == 1:
            years_string = "1 year"
        elif years > 1:
            years_string = f"{years} years"
        else:
            years_string = ""
        if months == 1:
            months_string = "1 month"
        elif months > 1:
            months_string = f"{months} months"
        else:
            months_string = ""
        if years_string and months_string:
            time_string = f'{years_string} and {months_string}'
        elif years_string:
            time_string = years_string
        else:
            time_string = months_string
        overpayment = payment * periods - principal
        print(f'It will take {time_string} to repay this loan!\nOverpayment = {overpayment}')
    else:
        print("Incorrect parameters")
elif loan_type == "diff":
    if not annuity and principal and periods and interest:
        principal = float(principal)
        periods = int(periods)
        interest_rate = float(interest) / (12 * 100)
        total_payment = 0
        for month in range(1, periods + 1):
            differential_payment = math.ceil(principal / periods + interest_rate * (principal - (principal * (month - 1)) / periods))
            total_payment += differential_payment
            print(f"Month {month}: payment is {differential_payment}")
        overpayment = total_payment - principal
        print(f'\nOverpayment = {overpayment}')
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
