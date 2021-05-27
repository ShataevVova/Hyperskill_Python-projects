import random
def random_name(s):
    name = random.choice(s)
    return name
    
print('Enter the number of friends joining (including you):')
persons = int(input())
if persons <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    names = {}
    i = 0
    while i < persons:
        names.update(dict.fromkeys([input()], 0))
        i += 1
    name  = []
    for k in names.keys():
        name.append(k)
    
    print('Enter the total bill value:')
    total_bill = int(input())
    for k in names:
            names[k] = round(total_bill / persons)
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_feature = input()
    if lucky_feature == 'Yes':
        lucky_name = random_name(name)
        print(f'{lucky_name} is the lucky one!')
        for k in names:
            names[k] = round(total_bill / (len(name) - 1))
        names[lucky_name] = 0
        print(names)
    else:
        print('No one is going to be lucky')
        print(names)
