import json
data = json.loads(input())
# -------------------------------------------------------------------------------------------
# Это предыдущее задание по проверки наличия START и STOP остановок

# определяю , какие маршруты имеем на входе
def lines(data):
    bus = []
    for n in range(len(data)):
        bus.append(data[n].get('bus_id'))
    return list(set(bus))

# сгруппирую входные данные в словарь  для каждой имеющейся линии
def group_lines():
    line_info = {}
    for n in range(len(data)):
        for line in lines(data):
            if data[n].get('bus_id') == line:
                line_info.setdefault(line, [])
                line_info[line].append(data[n])
    return line_info

# проверка трансферных остановок
def check_transfer(lst):
    transfer_stops = []
    for i, stop1 in enumerate(lst):
        for stop2 in lst[i + 1:]:
            if stop1 == stop2:
                transfer_stops.append(stop1)
    return transfer_stops

# определяю наличие START and STOP для каждой линии, если нет того или другого у линии, тогда брейк
def process(group_lines):
    stops = {}
    stop_names = [] # список названий всех остановок, буду использовать для поиска трансферных
    start_stops = []
    finish_stops = []
    for line in group_lines().keys():
        for n in range(len(group_lines()[line])):
            if group_lines()[line][n].get("stop_type") == 'S' or group_lines()[line][n].get("stop_type") == 'F':
                stops.setdefault(line, [])
                stops[line].append(group_lines()[line][n].get("stop_name"))
                
                # заношу в список название всех остановок START
            if group_lines()[line][n].get("stop_type") == 'S':
                start_stops.append(group_lines()[line][n].get("stop_name"))
                
               # заношу в список название всех остановок FINISH
            elif group_lines()[line][n].get("stop_type") == 'F':
                finish_stops.append(group_lines()[line][n].get("stop_name"))
            stop_names.append(group_lines()[line][n].get("stop_name"))

# проверяю список остановок по каждой линии, если меньше 2х, то сообщение об ошибке
        if len(stops[line]) != 2:
            print(f'There is no start or end stop for the line: {line}.')
        else:
            continue
    print('Start stops:', len(list(set(start_stops))), sorted(list(set(start_stops))))
    print('Transfer stops:', len(list(set(check_transfer(stop_names)))), sorted(list(set(check_transfer(stop_names)))))
    print('Finish stops:', len(list(set(finish_stops))), sorted(list(set(finish_stops))))
# process(group_lines)

# ------------------------------------------------------------------------
# Проверка корректности времени остановок

def check_time(dct):
    line_info = {}
    line_error = []
    error_time_point = {}
    response = []
    # создаю словарь с номерами линий и с некорректным временем в значениях
    for n in range(len(data)):
        for line in lines(data):
            if data[n].get('bus_id') == line:
                line_info.setdefault(line, [])
                line_info[line].append(data[n].get('a_time'))
    # Проверка корректности времени остановок (должны идти по возрастанию)
    for l in line_info.keys():
        # если отсортированный список со значением времени не равен имеющемуся списку,
        # значит в имеющемся списке время указано неверно
        if sorted(line_info[l]) != line_info[l]:
            # добавляем в словарь номера линий, в которых имеется некорректное время
            line_error.append(l)
            # Записываю в словарь название линии и некорректное время
    for line in line_error:
        error_time_point.setdefault(line, []).append(check(line_info.get(line)))
    # Нахожу название остановки по полученному некорректному времени
    for key in error_time_point.keys():
        for i in range(len(group_lines().get(key))):
            # Записываю в словарь с линиями и некорректным временем название соответсвтующей остановки
            # если остановка не имеет STOP_TYPE == 'S'
            if group_lines()[key][i].get("a_time") == "".join(error_time_point[key]) and group_lines()[key][i].get("stop_type") != 'S':
                error_time_point[key].append(group_lines()[key][i].get("stop_name"))
                response.append(f'bus_id line {key}: wrong time on station {error_time_point[key][1]}')
    # Проверяю, есть ли содержимое в словаре с ошибками, если да , то ответ об ошибках, если нет - то ОК
    if len(error_time_point) != 0:
        print('Arrival time test:')
        for res in response:
            print(res)
    else:
        print("OK")

# Вспомогательные функции для работы со значениями времени
# сравнение времён в списке и вывод первого меньшего значение
def check(time):
    int_time = []
    error_time = 0
    # Преобразование строки временного формата к типу INT
    for i in time:
        int_time.append(int(i.replace(":", '')))
    for n in range(len(int_time)-1):
        if int_time[n] < int_time[n+1]:
            continue
        else:
            error_time = (int_time[n+1])
            break
    # Преобразование числа в строковый формат времени
    n = list(str(error_time))
    if len(n) == 4:
        n.insert(2,":")
    else:
        n.insert(0,"0")
        n.insert(2,":")
    return "".join(n)

# check_time(group_lines)

#___________________________________________________________________________________________________

# проверка правильности остановок по требованию, они не должны быть Старт, финишь и трансферными.

def on_demand_stop(group_lines):
    o_stops = []
    sf_stops = []
    other_stops = []
    for line in group_lines().keys():
        for n in range(len(group_lines()[line])):
            # заношу в список название всех остановок  типа О
            if group_lines()[line][n].get("stop_type") == 'O':
                o_stops.append(group_lines()[line][n].get("stop_name"))
            # заношу в список название всех остановок  типа ""
            elif group_lines()[line][n].get("stop_type") == '':
                other_stops.append(group_lines()[line][n].get("stop_name"))
            # заношу в список название всех остановок  типа S и F
            elif group_lines()[line][n].get("stop_type") == 'S' or group_lines()[line][n].get("stop_type") == 'F':
                sf_stops.append(group_lines()[line][n].get("stop_name"))
#     print('sf_stops:', sf_stops)
#     print('o_stops:', o_stops)
#     print('other stops:', other_stops)

     #Затем сравниваю каждое имя_остановки из списка «О» с каждым именем_остановки во всех других списках.
#    Если элемент «О» находится в любом другом списке, это неправильно.
    intersect1 = list(set.intersection(set(o_stops), set(sf_stops)))
    intersect2 = list(set.intersection(set(o_stops), set(other_stops)))
    intersect = sorted(intersect1 + intersect2)
    print('On demand stops test:')
    if len(intersect) != 0:
        print(f'Wrong stop type: {intersect}')
    else:
        print('OK')

on_demand_stop(group_lines)
