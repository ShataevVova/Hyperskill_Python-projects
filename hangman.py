import random
import string

# menu of the game

def menu():
    print('H A N G M A N')
    print()
    choise = input("Type \"play\" to play the game, \"exit\" to quit:")
    if choise == "play":
        start_game()
    elif choise == "exit":
        quit()

# exit game

def quit():
    global game
    # print("exit game")
    game = False

# block of the game

def start_game():
    my_list = ['python', 'java', 'kotlin', 'javascript']

    word = random.choice(my_list)
    guess_word = '-' * len(word)

    print(guess_word)
    index = 0
    a = [i for i in word]
    b = [i for i in guess_word]
    other_letters = [] # список для хранения повторяющихся букв не встречающихся в загаданном слове
    guess_letter_list = [] # добавляю сюда все введёные буквы за один раз для подсчёта кол-ва введённых букв

    tries = 8
    answer = None
    msg = None

    while tries != 0:
        guess_letter = input('Input a letter:') # ввожу букву
        guess_letter_list = [i for i in guess_letter] # добавляю в список для подсчёта кол-ва введённых символов
        if len(guess_letter_list) > 1 or guess_letter == '': # если ввели больше одного символа
            print('You should input a single letter')
        else:
            if guess_letter in string.ascii_lowercase: # проверяю является ли введённая буква lowercase English letter

                if guess_letter in a:
                    if guess_letter in b:
                        msg = "You've already guessed this letter"
                        print(msg)

                    for i, letter in enumerate(a):
                        if letter == guess_letter:
                            index = i
                        else:
                            continue

                        b[index] = guess_letter
                else:
                    other_letters.append(guess_letter)
                    if other_letters.count(guess_letter) > 1: # проверяю, встречается ли введённая буква ещё раз
                        print("You've already guessed this letter")
                    else:
                        msg = "That letter doesn't appear in the word"
                        print(msg)
                        tries -= 1
                        if tries == 0:
                            answer = 'You lost!'
                            break
            else:
                print('Please enter a lowercase English letter')

        print()
        print(''.join(b))

        if a == b:
            answer = "You guessed the word!\nYou survived!\n"
            break
    print(answer)

# main loop

game = True
while game:
    menu()
