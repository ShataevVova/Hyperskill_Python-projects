# write your code here

step = input("Enter 9 symbols: ")
rev_step = ' '.join(step) # добавляем пробелы между введёнными символами
dash = "---------"
separator = '\n'
end_ = '|'
# Получаю первые 3 элемента
one_part = slice(0,5)
two_part = slice(6,11)
three_part = slice(12,17)
print(dash)
print('|', rev_step[one_part], end = ' | \n')
print('|', rev_step[two_part], end = ' | \n')
print('|', rev_step[three_part], end = ' | \n')
print(dash)



