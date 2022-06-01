import nltk, random, re

from nltk.tokenize import WhitespaceTokenizer
from collections import Counter

# читаю файл и разбиваю текст на токены
lst = []
with open(input(), "r", encoding="utf-8") as file:
    f = file.read()
    lst.extend(WhitespaceTokenizer().tokenize(f))

# разбиваю токены на триграммы
trigrams = (list(nltk.trigrams(lst)))

# разделяю триграммы на голову и хвост, составляю словарь, где ключ - это голова, а значения это хвосты
head_tail = {}
head_lst = []

for first, sec, third in trigrams:
    head = first + " " + sec
    head_lst.append(head)
    head_tail.setdefault(head, []).append(third)

count = 0 # счётчик  для условия выхода из цикла
chain = [] # список в котором будут собираться первое слово из словаря и затем последующие токены
lst_sentence = [] # список - с получившимися выражениями

# первый цикл в котором будут формироваться 10 выражений
while count != 10:
    first_word = "".join(random.choices(head_lst,  weights=None))
    head = first_word

    # проверка на то, что первое слово начинается с заглавной буквы и не имеет .!? знак в конце
    if re.match(r'^[A-Z].*[^.!?]\s.*', first_word):
        chain.append(first_word) # добавляю первое слово в список из 10 токенов
        count += 1
    else:
        continue

    # второй цикл - в котором формируется выражение (из 10 токенов)
    while True:
        tails = nltk.Counter(head_tail[head])
        max_val = max(tails.values())
        second_word = [k for k, v in tails.items() if v == max_val]
        # условие выбора второго слова, если имеем несколько токенов с одинаковым весом, то берём самый первый из списка
        if len(second_word) > 1:
            second_word = "".join(second_word[0])
        else:
            second_word = "".join(second_word)

#     — always end with a sentence-ending punctuation mark like ., !, or ?

        if re.match(r'.+[.?!]$', second_word):
            if len(chain) < 3:
                chain.append(second_word)
                head = chain[-2].split()[-1] + " " + chain[-1]
            else:
                chain.append(second_word)
                break
        else:
            chain.append(second_word)
            head = chain[-2].split()[-1] + " " + chain[-1]

    lst_sentence.append(" ".join(chain))
# после прохождения цикла нужно очистить список рандомных токенов, чтобы с новой итерацией цикла записать туда новый набор для нового выражения
    chain.clear()

# выводим на экран получившиеся предложения с новой строки
for sentence in lst_sentence:
    print(sentence)
