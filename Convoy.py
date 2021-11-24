import pandas as pd
import csv, sqlite3, json, math
from lxml import etree

user_input = input('Input file name\n')


# очищаю число от "мусора"
# clean number from trash


def replace_letter(value):
    box = []
    if not value.isdigit():
        for i in value:
            if i.isdigit():
                box.append(i)
    return ''.join(box)


# преобразую файл c "мусором" в файл с корректными данными
# convert the file with "garbage" into a file with correct data


def modify_csv_file(f_name):
    replace_count = 0
    f_name = f_name.split('.')[0]
    with open(f'{f_name}.csv') as file:
        keys = []
        my_df = pd.read_csv(file)
        for col in my_df:
            keys.append(col)
        for key in keys:
            for val in my_df[key]:
                if type(val) == int:
                    continue  # если значение int - пропускаем преобразование
                elif not val.isdigit():
                    my_df = my_df.replace(val, replace_letter(val))
                    replace_count += 1

    # .strip('[CHECKED]') - убираю дублирующее окончание имени файла
    # remove the duplicate ending of the file name

    if replace_count > 1:
        my_df.to_csv(f'{f_name.strip("[CHECKED]")}[CHECKED].csv', index=False)
        print(f'{replace_count} cells were corrected in {f_name.strip("[CHECKED]")}[CHECKED].csv')
    elif replace_count == 1:
        my_df.to_csv(f'{f_name.strip("[CHECKED]")}[CHECKED].csv', index=False)
        print(f'{replace_count} cell was corrected in {f_name.strip("[CHECKED]")}[CHECKED].csv')


# calculate scores


def scores(engine_capacity, fuel_consumption, maximum_load):
    engine_capacity = int(engine_capacity)
    fuel_consumption = int(fuel_consumption)
    maximum_load = int(maximum_load)
    route = 450
    burned_fuel = (route * fuel_consumption / 100)
    number_pitstop = (burned_fuel / engine_capacity)
    if number_pitstop > 2:
        score_pitstop = 0
    elif number_pitstop >= 1:
        score_pitstop = 1
    else:
        score_pitstop = 2
    score_fuel = (2 if burned_fuel <= 230 else 1)
    score_load = (2 if maximum_load >= 20 else 0)
    return score_pitstop + score_fuel + score_load


# modify file_name in to db_name


def data_base_name(db_name):
    if db_name.split('.')[0].endswith('[CHECKED]'):
        return db_name.split('.')[0].strip('[CHECKED]')
    else:
        return db_name.split('.')[0]


# Создание таблицы в базе данных SQLITE3
# create the table in SQlite3

def create_db_table(db_name, table_name):
    conn = sqlite3.connect(f'{data_base_name(db_name)}.s3db')
    cur = conn.cursor()
    count_execute_table_row = 0
    cur.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                vehicle_id INTEGER PRIMARY KEY,
                engine_capacity INT NOT NULL,
                fuel_consumption INT NOT NULL,
                maximum_load INT NOT NULL,
                score INT NOT NULL
            );''')

    with open(f'{data_base_name(db_name)}[CHECKED].csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # пропускаю первую строку с заголовками ((miss first line with names of columns))
        for row in reader:
            score = scores(row[1], row[2], row[3])
            to_db = [row[0], row[1], row[2], row[3], score]
            cur.execute(f'''INSERT INTO {table_name} (
                        vehicle_id, engine_capacity, fuel_consumption, maximum_load, score
                        ) VALUES (?, ?, ?, ?, ?);''', to_db)
            count_execute_table_row += 1
    conn.commit()
    conn.close()

    if count_execute_table_row > 1:
        print(f'{count_execute_table_row} records were inserted into {data_base_name(db_name)}.s3db')
    else:
        print(f'{count_execute_table_row} record was inserted into {data_base_name(db_name)}.s3db')


# convert from Sqlite to json file

def convert_sql_to_json(db_name, table_name):
    conn = sqlite3.connect(f'{data_base_name(db_name)}.s3db')
    cur = conn.cursor()

    cur.execute(
        f'SELECT vehicle_id, engine_capacity, fuel_consumption, maximum_load FROM {table_name} WHERE score > 3;')
    row_headers = [x[0] for x in cur.description]  # извлекаем заголовки
    results = cur.fetchall()
    conn.close()

    json_data = []
    count = 0
    for result in results:
        json_data.append(dict(zip(row_headers, result)))
        count += 1
    json_file = {f'{table_name}': json_data}

    with open(f'{data_base_name(db_name)}.json', 'w') as file:
        json.dump(json_file, file)

    print(f'{count} vehicles were saved into {data_base_name(db_name)}.json' \
              if count > 1 or count == 0 else f'{count} vehicle was saved into {data_base_name(db_name)}.json')


# convert from Sqlite to xml file

def convert_sql_to_xml(db_name, table_name):
    conn = sqlite3.connect(f'{data_base_name(db_name)}.s3db')
    cur = conn.cursor()

    cur.execute(
        f'SELECT vehicle_id, engine_capacity, fuel_consumption, maximum_load FROM {table_name} WHERE SCORE <= 3;')
    row_headers = [x[0] for x in cur.description]  # извлекаем заголовки
    results = cur.fetchall()
    conn.close()

    data = []
    count_xml = 0
    for result in results:
        data.append(dict(zip(row_headers, result)))
        # count += 1
    obj = {f'{table_name}': data}
    for key, val in obj.items():
        root = etree.Element(key)  # create root element

        for dic in val:
            sub_root = etree.SubElement(root, 'vehicle')
            count_xml += 1
            for child, text in dic.items():
                etree.SubElement(sub_root, child).text = str(text)

    xml_obj = etree.ElementTree(root)
    xml_obj.write(f"{data_base_name(db_name)}.xml", method='html')

    print(f'{count_xml} vehicles were saved into {data_base_name(db_name)}.xml' \
              if count_xml > 1 or count_xml == 0 else f'{count_xml} vehicle was saved into {data_base_name(db_name)}.xml')


# main program


if '.xlsx' in user_input:
    file_name = user_input.split('.')[0]
    my_df = pd.read_excel(user_input, sheet_name='Vehicles', dtype=str)
    my_df.to_csv(file_name + '.csv', index=None)
    count_line = -1
    with open(file_name + '.csv', 'r') as f:
        for line in f:
            count_line += 1
        if count_line > 1:
            print(f'{count_line} lines were added to {file_name}.csv')
        else:
            print(f'{count_line} line was added to {file_name}.csv')
    modify_csv_file(file_name + '.csv')
    create_db_table(file_name, 'convoy')
    convert_sql_to_json(file_name, 'convoy')
    convert_sql_to_xml(file_name, 'convoy')
elif '.s3db' in user_input:
    convert_sql_to_json(user_input, 'convoy')
    convert_sql_to_xml(user_input, 'convoy')
else:
    modify_csv_file(user_input)
    create_db_table(user_input, 'convoy')
    convert_sql_to_json(user_input, 'convoy')
    convert_sql_to_xml(user_input, 'convoy')
