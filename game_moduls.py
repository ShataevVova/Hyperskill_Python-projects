import random


# игра камень-ножницы-бумага

# вспомогательные функции

# 1 функция получения очков, если такой пользователь существует


def get_rating(name):
    with open('rating.txt', 'r') as rating:  # читаем список из файла
        rating_list = [line.split() for line in rating]
    rating_dict = dict(rating_list)  # преобразуем полученный список в словарь
    if name in rating_dict.keys():
        return int(rating_dict[name])  # если имя есть в списке, то вернуть баллы рейтинга
    if name not in rating_dict.keys():  # если имени нет, то добавить имя и 0 баллов в список и записать в файл
        add_new_name(name, score=0)


# 2 функция добавления нового имени и баллов в файл


def add_new_name(name, score):
    with open('rating.txt', 'a') as rating:
        print(name, score, file=rating, sep=' ', end='\n')


# 3 функция добавления баллов к существующему рейтигу


def add_scores(name, score):
    with open('rating.txt', 'r') as rating:  # читаем список из файла
        rating_list = [line.split() for line in rating]
    rating_dict = dict(rating_list)  # преобразуем полученный список в словарь
    new_score = int(rating_dict[name]) + (int(score))  # обновляем баллы
    rating_dict[name] = str(new_score)  # записываем полученные баллы в словарь по ключу с искомым именем
    rating_list = list(rating_dict.items())  # преобразуем словарь в список для дальнейшей записи в файл
    with open('rating.txt', 'w') as file:
        result = [(" ".join(each) + '\n') for each in
                  rating_list]  # создаём список result, куда добавляем преобразованный список для записи в файл
        file.writelines(result)


# стереть содержимое файла рейтинг


def clear_file():
    with open('rating.txt', 'w') as rating:
        rating.write('')


# 4 Преобразование имени, написанного с маленькой буквы


def correct_name(name):
    if name.islower():
        return name.title()
    else:
        return name


# 5 запрос и получение списка фигур для игры от пользователя


def get_user_list():
    ui_figures = input("enter figures ").split(",")
    ui_figures = [i.strip() for i in ui_figures]
    print("Okay, let's start")
    return ui_figures


# 6 получение новых правил игры


def new_rules(user_name, user_choice, user_options):
    # ___________получение правил с новыми фигурами______________________________________________
    shapes = 'rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', \
             'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'

    rules = {}  # словарь с выйгрыщными комбинациями
    for index, figure in enumerate(shapes):

        rules[figure] = (shapes[index + 1:] + shapes[:index])[:(len(shapes) // 2)]

    # ___________________________________________________________________________________________
# правила для пользовательского списка

    machine_choice = random.choice(user_options)
    if user_choice in user_options:
        if user_choice == machine_choice:
            add_scores(user_name, 50)
            print(output_msg('draw', machine_choice))
        elif machine_choice in rules[user_choice]:
            add_scores(user_name, 100)
            print(output_msg('win', machine_choice))
        elif machine_choice not in rules[user_choice]:
            if user_choice in rules[machine_choice]:
                print(output_msg('lose', machine_choice))


# Правила по умолчанию


def default_rules(user_name, user_choice, default_options):
    machine_choice = random.choice(default_options)
    win_combinations = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    if user_choice in win_combinations.keys():
        if user_choice == machine_choice:
            add_scores(user_name, 50)
            print(output_msg('draw', machine_choice))
        elif win_combinations[user_choice] == machine_choice:
            add_scores(user_name, 100)
            print(output_msg('win', machine_choice))
        elif win_combinations[user_choice] != machine_choice:
            print(output_msg('lose', machine_choice))


# 7 Сообщения при различных вариантах окончания игры

def output_msg(state, machine_choice):
    lose = f"Sorry, but the computer chose {machine_choice}"
    draw = f"There is a draw ({machine_choice})"
    win = f"Well done. The computer chose {machine_choice} and failed"
    state_list = {'lose': lose, "draw": draw, "win": win}
    if state == 'lose':
        return state_list['lose']
    elif state == 'draw':
        return state_list['draw']
    elif state == 'win':
        return state_list['win']


# выбор игры (по умолчанию или пользовательская)
# 8 игра по умолчанию


def mode(user_name):
    default_options = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input()
        get_rating(user_name)  # добавляем в файл rating.txt новое имя пользователя с 0 баллами
        if user_choice == "!exit":
            print('Bye!')
            break
        elif user_choice == '!rating':
            print('Your rating: ', get_rating(user_name))  # получаем рейтинг игрока
        elif user_choice in default_options:
            default_rules(user_name, user_choice, default_options)  # вызов правил игры по умолчанию
        else:
            print('Invalid input')


# 9 пользовательская игра (с вариантами фигур, выбранными пользователем)


def user_mode(user_name, user_options):
    while True:
        user_choice = input()
        get_rating(user_name)  # добавляем в файл rating.txt новое имя пользователя с 0 баллами
        if user_choice == "!exit":
            print('Bye!')
            break
        elif user_choice == '!rating':
            print('Your rating: ', get_rating(user_name))  # получаем рейтинг игрока
        elif user_choice in user_options:
            new_rules(user_name, user_choice, user_options)  # вызов правил игры с новыми вариантами!!!!!
        else:
            print('Invalid input')
