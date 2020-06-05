from math import log, ceil, floor
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=float)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--principal", type=int)
args = parser.parse_args()

if args.type == "diff":

    if args.payment or not (args.principal > 0 and args.periods > 0 and args.interest > 0):

        print("Incorrect parameters")

    else:

        i = args.interest / (12 * 100)
        sum = 0

        for m in range(1, args.periods + 1):

            d = ceil(args.principal / args.periods +
                     i * (args.principal - (m - 1) * (args.principal / args.periods)))
            sum += d

            print(f"Month {m}: paid out {d}")

        print(f"\nOverpayment = {sum - args.principal}")

elif args.type == "annuity":

    if args.periods is None and args.principal and \
            args.principal > 0 and args.interest and args.interest > 0 and \
            args.payment and args.payment > 0:

        i = args.interest / (12 * 100)

        n = ceil(log(args.payment / (args.payment - i * args.principal), 1 + i))

        years = n // 12
        months = n % 12

        if years > 0 and months > 0:
            print(f"You need {years} years and {months} months to repay this credit!")

        elif years == 0:
            print(f"You need {months} months to repay this credit!")

        else:
            print(f"You need {years} years to repay this credit!")

        print(f"Overpayment = {int(args.payment) * (years * 12 + months) - args.principal}")

    elif args.payment is None and args.principal > 0 and args.periods > 0 and args.interest > 0:

        i = (1/12) * (args.interest / 100)

        payment = ceil(args.principal * ((i * (1 + i)**args.periods) / ((1 + i)**args.periods - 1)))

        print(f"Your annuity payment = {payment}!")

        print(f"Overpayment = {payment * args.periods - args.principal}")

    elif args.principal is None and args.interest > 0 and args.payment > 0 and args.periods > 0:

        i = (1/12) * args.interest / 100

        principal = floor(args.payment / ((i * (1 + i)**args.periods) / ((1 + i)**args.periods - 1)))

        print(f"Your credit principal = {principal}!")

        print(f"Overpayment = {int(args.payment) * args.periods - principal}")

    else:

        print("Incorrect parameters")

else:

    print("Incorrect parameters")
