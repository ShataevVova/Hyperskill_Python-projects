import math
def menu():
    print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
    
def  user_choice():
    choice = input(">")
    if choice == "a":
        print("Enter the loan principal:")
        loan_principal = int(input())
        print("Enter the number of periods:")
        number_of_periods = int(input())
        print("Enter the loan interest:")
        loan_interest = float(input())
        print("Your monthly payment = " + str(monthly_payment_calc(loan_principal, number_of_periods, loan_interest)) + "!")
    elif choice == "n":
        print("Enter the loan principal:")
        loan_principal = int(input())
        print("Enter the monthly payment:")
        monthly_payment = int(input())
        print("Enter the loan interest:")
        loan_interest = float(input())
        s = (number_of_payments_calc(loan_principal, monthly_payment, loan_interest))
        print(s)
        print(f"It will take {s[0]} years and {s[1]} months to repay this loan!")
    elif choice == "p":
        print("Enter the annuity payment:")
        annuity_payment = float(input())
        print("Enter the number of periods:")
        number_of_periods = int(input())
        print("Enter the loan interest:")
        loan_interest = float(input())
        print("Your loan principal = " + str(loan_principal_calc(annuity_payment, number_of_periods, loan_interest)) + "!")
        
# вычисление основной суммы кредита (P)

def loan_principal_calc(annuity_payment, number_of_periods, loan_interest):
    a = annuity_payment
    n = number_of_periods
    li = loan_interest
    i = li / 12 / 100
    
    p = math.floor(a / (i * math.pow((1 + i), n) / ((math.pow((1 + i), n) - 1))))
    return p

# вычисление ежемесячного аннуитентного платежа (a)

def monthly_payment_calc(loan_principal, number_of_periods, loan_interest):
    p = loan_principal
    n = number_of_periods
    li = loan_interest
    i = li / 12 / 100
    a = math.ceil(p * (i * (math.pow((1 + i), n)) / ((math.pow((1 + i), n) - 1))))
    return a

# вычисление кол-ва платежей (n)

def number_of_payments_calc(loan_principal, monthly_payment, loan_interest):
    p = loan_principal
    a = monthly_payment
    li = loan_interest
    i = li / 12 / 100
    n = math.ceil(math.log((a / (a - i * p)), (1 + i)))
    
    return divmod(n, 12)
	
# Вычисление переплаты по аннуитентным платежам

def overpayment(loan_principal, annuity_payment, number_of_periods):
	a = annuity_payment
	p = loan_principal
	n = number_of_periods
	return int(p) - int(a) * int(n)
	
# вычисление дифференцированного платежа и переплаты по нему

def diff_payment_calc(loan_principal, loan_interest, number_of_periods):
	p = loan_principal
	i = loan_interest / 12 / 100
	n = number_of_periods
	amount = 0
	for m in range(1, n + 1):
		d = math.ceil(p/n + i * (p - ((p * (m - 1)) / n)))
		print('Month ' + str(m) + ': payment is',d)
		amount += d
	print('Overpayment =',amount - p)

    