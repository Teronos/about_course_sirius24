import os
import pandas as pd
from string import Template

# Функция создания и перехода в рабочую папку
def chdir(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    os.chdir(folder)
    return

# Читаем шаблон из файла
with open('program_data/signature_template.html','r') as html_file:
    html = html_file.read()

# Чтение датафрейма из таблицы
excel_data = pd.read_excel('program_data/recipients_list.xlsx')
data = pd.DataFrame(excel_data, columns=['ФИО','Должность','Название_отдела_1я_строка','Название_отдела_2я_строка','Организация','Рабочий_телефон','Внутренний_номер','Сотовый_телефон','Электронная_почта','Сайт'])

# Заполнение пустых ячеек таблицы высокоэнтропийным числом (17 знаков для текущей цели - пожалуй более чем достаточно) upd: при этом - не боле 17ти, ограничено преобразованием короткого номера в int
randm = 12332434234987546
data = data.fillna(randm)

# Подготавливаем строки для фильтров, читаем их построчно из файла "nan_strings.html" в список
with open('program_data/nan_strings.html','r') as nan:
    nan_strings = nan.readlines()

# Допиливаем список: подставляем значение randm, удоляем перенос в конце строки (их плодит "readlines")
for i in range (0,len(nan_strings)):
    nan_strings[i] = nan_strings[i].replace('randm', str(randm))
    nan_strings[i] = nan_strings[i].replace('\n','')

# Ныряем в папку "оутпут"
chdir('output')

for k in range (0,len(data)):
    # Подсовываем в переменные html данные из датафрейма
    output_html = Template(html).safe_substitute(fio=data.ФИО[k], dolzhnost=data.Должность[k],otdel_1st_string=data.Название_отдела_1я_строка[k],\
                                                 otdel_2nd_string=data.Название_отдела_2я_строка[k],organization=data.Организация[k],\
                                                 work_phone=data.Рабочий_телефон[k],inner_short=int(data.Внутренний_номер[k]),\
                                                 mobile=data.Сотовый_телефон[k],email=data.Электронная_почта[k],site=data.Сайт[k])

    #Фильтрация отсутствующих значений
    for i in range (0,len(nan_strings)):
        output_html = output_html.replace(str(nan_strings[i]), '')

    #Сохраняем в файл
    filename = data.ФИО[k] + '_RuPost_' + str(k+1) + '_подпись.html'
    with open(filename,'w') as file:
        file.write (output_html)
        
    # Сообщаем об успешном успехе
    print('Создан файл ',filename)
