import argparse
import modul_for_calculator
parser = argparse.ArgumentParser(description = "calc")
parser.add_argument('--type', type=str,
                    help='type of payments')

parser.add_argument('--principal', type=int,
                    help='loan principal')
parser.add_argument('--payment', type=int, 
					help='monthly payment')
parser.add_argument('--periods', type=int, 
					help='denotes the number of months needed to repay the loan')
parser.add_argument('--interest', type=float,
					help='interest')
args = parser.parse_args()

#short names for usability

n1 = args.type # выбор типа платежа (дифференциальный или аннуитентный)
n2 = args.principal # основная сумма кредита
n3 = args.payment # сумма ежемесячного платежа
n4 = args.periods # обозначает количество месяцев, необходимое для погашения кредита
n5 = args.interest # процентная ставка
count_non = 0
if n1 == None:	#где-то здесь ошибка , из-за которой не выводится сообщение о неправильном вводе
	print('Incorrect parameters')
elif n1 not in ('annuity', 'diff'):
	print('Incorrect parameters')
else:
	if n1 == 'diff':
		if n3 == None:
			count_non += 1
			modul_for_calculator.diff_payment_calc(int(n2), float(n5), int(n4))
		else:
			print('Incorrect parameters')
		
	elif n1 == 'annuity':
		if n5 == None: 
			count_non += 1
			print('Incorrect parameters')
			# вычисление аннуитентного платежа
		elif n3 == None:
			count_non += 1
			if n2 < 0 or n4 < 0 or n5 < 0:
				print('Incorrect parameters')
			else:
				annuity_payment = modul_for_calculator.monthly_payment_calc(n2, n4, n5)
				print('Your annuity payment = ', str(annuity_payment) + '!')
				print('Overpayment = ', abs(modul_for_calculator.overpayment(n2, annuity_payment, n4)))
	# вычисление основной суммы кредита
		elif n2 == None:
			count_non += 1
			if n3 < 0 or n4 < 0 or n5 < 0:
				print('Incorrect parameters')
			else:
				loan_principal = modul_for_calculator.loan_principal_calc(n3, n4, n5)
				print('Your loan principal = ', str(loan_principal) + '!')
				print('Overpayment = ', abs(modul_for_calculator.overpayment(loan_principal, n3, n4)))
	# вычисление количества времени для выплаты кредита
		elif n4 == None:
			count_non  += 1
			if n2 < 0 or n3 < 0 or n5 < 0:
				print('Incorrect parameters')
			else:
				periods = (modul_for_calculator.number_of_payments_calc(n2, n3, n5))
			#вывод, если круглое число лет
				if periods[1] != 0:
					print(f"It will take {periods[0]} years and {periods[1]} months to repay this loan!")
			# вывод, если не круглое число лет
				else:
					print(f"It will take {periods[0]} years to repay this loan!")
				print('Overpayment = ', abs(modul_for_calculator.overpayment(n2, n3, periods[0]*12 + periods[1])))
if count_non >= 2:
    print('Incorrect parameters', count_non)
	
# на 27.12.2020 -===>>>>> доработать некоректный ввод данных и ошибки!!!!