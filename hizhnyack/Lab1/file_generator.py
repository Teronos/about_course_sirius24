import os
import pandas as pd
from string import Template

# Функция создания и перехода в рабочую папку
def chdir(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    os.chdir(folder)
    return

# Читаем шаблон из файла (ниже под ремом про запас лежит этот же шаблон. Возможно лучше хранить шаблон в коде, чтобы в корневом каталоге программы было меньше файлов)
with open('template.html','r') as html:
       html = html.read()
# html = '''\
# <html>
# <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>
# <body>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none"><span style="font-family:'calibri';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000">С уважением, </span></p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none">&nbsp;</p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none"><span style="font-family:'calibri';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000"><b>$fio</b></span></p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none">&nbsp;</p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none"><span style="font-family:'calibri';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000">$dolzhnost </span></p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none"><span style="font-family:'calibri';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000">$otdel_1st_string</span></p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none"><span style="font-family:'calibri';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000">$otdel_2nd_string</span></p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none">&nbsp;</p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none"><span style="font-family:'calibri';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000">$organization</span></p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none">&nbsp;</p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none"><span style="font-family:'calibri';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000">$work_phone, вн. $inner_short | $mobile</span></p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none">
# <a href="mailto:$email" title="mailto:$email"><span style="font-family:'calibri';font-size:11pt;color:#0563c1;mso-style-textfill-fill-color:#0563c1"><u>$email</u></span></a>
# <span style="font-family:'calibri';font-size:11pt;color:#0563c1;mso-style-textfill-fill-color:#0563c1">|</span>
# <a href="https://$site/" title="https://$site/"><span style="font-family:'calibri';font-size:11pt;color:#0563c1;mso-style-textfill-fill-color:#0563c1"><u>$site</u></span></a>
# <span style="font-family:'Arial';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000"><br style="mso-special-character:line-break;"/></span></p>
# <p style="margin-top:0pt;margin-bottom:0pt;border:none;border-left:none;border-top:none;border-right:none;border-bottom:none;mso-border-between:none">
# <span style="font-family:'Arial';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000">
# <img style="max-width:100%;" width="192" height="93" src="data:image/png;base64, +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"/></span></p>
# </body>
# </html>
# '''
#  Обьявляем неудобные длинные строки для фильтров
nan_string = '''<p style="margin-top:0pt;margin-bottom:0pt;border:none;mso-border-left-alt:none;mso-border-top-alt:none;mso-border-right-alt:none;mso-border-bottom-alt:none;mso-border-between:none"><span style="font-family:'calibri';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000">12121232095776436</span></p>\n'''
nan_string_site = '''<span style="font-family:'calibri';font-size:11pt;color:#0563c1;mso-style-textfill-fill-color:#0563c1">|</span>\n<a href="https://12121232095776436/" title="https://12121232095776436/"><span style="font-family:'calibri';font-size:11pt;color:#0563c1;mso-style-textfill-fill-color:#0563c1"><u>12121232095776436</u></span></a>\n<span style="font-family:'Arial';font-size:11pt;color:#000000;mso-style-textfill-fill-color:#000000"><br style="mso-special-character:line-break;"/></span></p>\n'''

# Чтение датафрейма из таблицы
excel_data = pd.read_excel('data.xlsx')
data = pd.DataFrame(excel_data, columns=['ФИО','Должность','Название_отдела_1я_строка','Название_отдела_2я_строка','Организация','Рабочий_телефон','Внутренний_номер','Сотовый_телефон','Электронная_почта','Сайт'])

# Заполнение пустых ячеек таблицы высокоэнтропийным числом (17 знаков для текущей цели - пожалуй более чем достаточно)
data = data.fillna('12121232095776436')
# Ныряем в папку "оутпут"
chdir('output')

for k in range (0,len(data)):
    # Подсовываем в переменные html данные из датафрейма
    output_html = Template(html).safe_substitute(fio=data.ФИО[k], dolzhnost=data.Должность[k],otdel_1st_string=data.Название_отдела_1я_строка[k],\
                                                 otdel_2nd_string=data.Название_отдела_2я_строка[k],organization=data.Организация[k],\
                                                 work_phone=data.Рабочий_телефон[k],inner_short=int(data.Внутренний_номер[k]),\
                                                 mobile=data.Сотовый_телефон[k],email=data.Электронная_почта[k],site=data.Сайт[k])

    #Фильтрация отсутствующих значений
    output_html = output_html.replace(nan_string, '')
    output_html = output_html.replace(nan_string_site, '')
    output_html = output_html.replace(' | 12121232095776436</', '</')
    output_html = output_html.replace(', вн. 12121232095776436', '')
    output_html = output_html.replace('12121232095776436', '')

    #Сохраняем в файл
    filename = data.ФИО[k] + '_RuPost_' + str(k+1) + '_подпись.html'
    with open(filename,'w') as file:
        file.write (output_html)