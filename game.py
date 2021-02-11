import game_moduls

# основная функция игры камень-ножницы-бумага


def run_game():
    user_name = game_moduls.correct_name(input('Enter your name: '))
    print(f'Hello, {user_name}')

    user_options = game_moduls.get_user_list()

    if user_options == ['']: # игра по умолчанию
        game_moduls.default_mode(user_name)
    else:                               # играем с использованием пользовательского списка вариантов
        game_moduls.user_mode(user_name, user_options)


# __________________________________

# game_moduls.add_new_name('Name', 'Scores') # В начале новой игры создаём файл rating.txt
                                                   # и записываем имя пользователя с 0 баллами в файл
                                                   # НО для прохождения тестов это не требуется, т.к. такой файл
                                                   # уже существует!
run_game()
