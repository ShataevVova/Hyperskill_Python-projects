import requests

have_currency = input().lower().strip()
wallet = {}
r = requests.get(f'http://www.floatrates.com/daily/{have_currency}.json').json()

for key in r.keys():
    if key == "usd":
        wallet['usd'] = r.get('usd')['rate']
    elif key == "eur":
        wallet['eur'] = r.get('eur')['rate']

flag = True
while flag:
    get_currency = input().lower().strip()
    if get_currency == '':
        break
    amount_money = input().strip()
    if amount_money == '':
        break
    if get_currency in wallet:
        print('Checking the cache…')
        print('Oh! It is in the cache!')
        new_currency = wallet[get_currency]
        print('You received ' + str(round(float(new_currency) * float(amount_money), 2)) + ' ' + get_currency.upper() + '.')
    else:
        print('Checking the cache…')
        print('Sorry, but it is not in the cache!')
        wallet[get_currency] = r.get(get_currency)['rate']
        new_currency = wallet[get_currency]
        print('You received ' + str(round(float(new_currency) * float(amount_money), 2)) + ' ' + get_currency.upper() + '.')
