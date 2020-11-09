import random

import sqlite3
#  -------------------------------------------------------
# methods for working with database
# подключение к базе данных

DB_FILE = 'card.s3db'

# создание таблицы для данных о картах пользователя
def create_table():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS card (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0
        );''')
    conn.commit()
    cur.close()
    conn.close()

# заполнить таблицу данными о карте пользователя

def fill_data_of_card(card_number, pin):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('INSERT INTO card (number, pin) VALUES (?, ?);',(card_number, pin))
    global last_id
    last_id = cur.lastrowid
    conn.commit()
    cur.close()
    conn.close()
    # print('str_last ID: ', last_id)

# Получение данных из базы данных
def get_number_info(last_id):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT number FROM card WHERE id = (?);', (last_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def get_pin_info(last_id):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT pin FROM card WHERE id = (?);', (last_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def get_last_id():
    global last_id
    return str(last_id)

def get_all_cards():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM card;')
    row = cur.fetchall()
    cur.close()
    conn.close()
    return row

def get_number_from_db():
    for i in get_number_info(get_last_id()):
        return i

def get_pin_from_db():
    for i in get_pin_info(get_last_id()):
        return i

def valid_card_number(number):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT number FROM card WHERE number = (?);', (number,))
    row = cur.fetchone()
    if row != None:
        for i in row:
            return i
    cur.close()
    conn.close()

def valid_pin(pin):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT pin FROM card WHERE pin = (?);', (pin,))
    row = cur.fetchone()
    if row != None:
        for i in row:
            return i

def get_balance(number):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT balance FROM card WHERE number = (?);', (number,))
    row = cur.fetchone()
    if row != None:
        for i in row:
            return i


def income_add(income, number):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("UPDATE card  SET balance = balance + (?) WHERE number = (?);", (income, number))
    conn.commit()
    cur.close()
    conn.close()


def sub(income, number):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('UPDATE card  SET balance = balance - (?) WHERE number = (?);', (income, number))
    conn.commit()
    cur.close()
    conn.close()


def check_card(number):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT number FROM card WHERE number = (?);', (number,))
    row = cur.fetchone()
    if row is None:
        return True


def del_account(number):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('DELETE FROM card WHERE number = (?);', (number,))
    conn.commit()
    cur.close()
    conn.close()
#  --------------------------------------------------------------
#
# генерируем номер карты и пин номер

def generate_card_number():
    number = '400000' + "".join([str(random.randint(0, 9)) for i in range(0, 9)])
    return number

def generate_pin():
    pin = "".join([str(random.randint(0, 9)) for i in range(0, 4)])
    return pin
#___________________
def luhn_algorithm():
    # модуль умножения нечётных чисел на 2
    gen_num = generate_card_number()
    int_list = [int(i) for i in gen_num]
#     print('before', int_list)

    modif_list = []
    for index, i in enumerate(int_list):
        if (index - 1) % 2 != 0:
            i *= 2
            modif_list.append(i)
        else:
            i = i
            modif_list.append(i)

    # модуль вычитания 9 из чисел больше 9
    for index, i in enumerate(modif_list):
        if i > 9:
            modif_list[index] -= 9
#     print('after ', modif_list)

    # модуль сложения всех чисел
    amount = 0
    for i in range(len(modif_list)):
        amount += modif_list[i]
#     print('amount:', amount)

    # модуль проверки числа контрольной суммы
    count = 0
    if amount % 10 == 0:
        modif_list.append(0)
    else:
        while amount % 10 != 0:
            amount += 1
            count += 1
#     print('am:', amount)
#     print('count:', count)
    int_list.append(count)
#     print('ml: ', int_list)

    # преобразование полученного списка цифр в строку для последующего объединения
    str_list = [str(i) for i in int_list]
    return ''.join(str_list)

# Проверка алгоритма луна
def luhn_algorithm_check(card_number):
    mod_card_number = card_number[:-1]
    int_list = [int(i) for i in mod_card_number]
    modif_list = []
    for index, i in enumerate(int_list):
        if (index - 1) % 2 != 0:
            i *= 2
            modif_list.append(i)
        else:
            i = i
            modif_list.append(i)

    # модуль вычитания 9 из чисел больше 9
    for index, i in enumerate(modif_list):
        if i > 9:
            modif_list[index] -= 9
    amount = 0
    for i in range(len(modif_list)):
        amount += modif_list[i]

    # модуль проверки числа контрольной суммы
    count = 0
    if amount % 10 == 0:
        modif_list.append(0)
    else:
        while amount % 10 != 0:
            amount += 1
            count += 1
    int_list.append(count)
    str_list = [str(i) for i in int_list]
    if card_number == "".join(str_list):
        return True
    else:
        return False



#______________________

# создание аккаунта

def create_an_account():
    card_number = luhn_algorithm()
    pin = generate_pin()
    fill_data_of_card(card_number, pin)
    print('Your card has been created')
    print('Your card number:')
    print(get_number_from_db())
    print('Your card PIN:')
    print(get_pin_from_db())
    print()

# показать меню
def show_menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit\n")


def show_menu_in():
    print('1. Balance')
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
    print("0. Exit\n")

# выбор пользователя первое меню
def user_choice_1():
    choice = input()
    print()
    while choice.isdigit() != True :
        choice = input('enter digits')
    if choice == '1':
        create_an_account()
    elif choice == '2':
        log_in()
    elif choice == '0':
        exit()

# выбор пользователя второе меню
def user_choice_2():
    choice = input()
    print()
    while choice.isdigit() != True :
        choice = input('enter digits')

    if choice == '1':
        balance()
    elif choice == '2':
        add_income()
    elif choice == '3':
        do_transfer()
    elif choice == '4':
        close_account()
    elif choice == '5':
        log_out()
    elif choice == '0':
        exit()

# логинимся
def log_in():
    flag_1 = False
    flag_2 = False
    print('Enter your CARD NUMBER')
    global card_num
    card_num = input()
    if valid_card_number(card_num) == card_num:
        flag_1 = True
        if flag_1 == True:
            print('Enter your pin')
            input_pin = input()
            if valid_pin(input_pin) == input_pin:
                flag_2 = True
    if flag_1 and flag_2 == True:
        print('You have successfully logged in!\n')
        show_menu_in()
        user_choice_2()
    else:
        print('Wrong card number or pin')

# выход из аккаунта
def log_out():
    print('You have successfully logged out!\n')
    show_menu()
    user_choice_1()

# меню баланса
def balance():
    global card_num
    print('Balance: ', get_balance(card_num), '\n')
    show_menu_in()
    user_choice_2()

#пополнить
def add_income():
    global card_num
    print('Enter income:\n')
    income = input()
    income_add(income, card_num)
    print('Income was added!\n')
    show_menu_in()
    user_choice_2()

# перевести на другой аккаунт
def do_transfer():
    global card_num
    print('Transfer')
    print('Enter card number:')
    transfer_card_number = input()
    if not luhn_algorithm_check(transfer_card_number):
        print('Probably you made a mistake in the card number. Please try again!')
    elif transfer_card_number == card_num:
        print("You can't transfer money to the same account!")
    elif check_card(transfer_card_number):
        print('Such a card does not exist.')
    else:
        print('Enter how much money you want to transfer:')
        money = input()
        if int(money) > get_balance(card_num):
            print('Not enough money!\n')
        else:
            income_add(money, transfer_card_number)
            print('balance of transfer account: ', get_balance(transfer_card_number))
            sub(money, card_num)
            print(get_balance(card_num))

    show_menu_in()
    user_choice_2()

# удалить аккаунт из базы данных
def close_account():
    global card_num
    del_account(card_num)
    print('account has been deleted')

# выход
def exit():
    global quit
    quit = True
    print('Bye!')
    return

#  ----------MAIN PROGRAM------------------
# работа основной программы

quit = False
create_table()
while quit == False:
    show_menu()
    user_choice_1()
