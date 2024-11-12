import re
import os
import smtplib
from getpass import getpass
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# Функция прикрепления файла к телу письма
def attach_file (mesg, attachname):
    with open(attachname, "rb") as att_file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(att_file.read())
        encoders.encode_base64(part)
        if attachname == manual:
            attachname = attachname.replace('program_data/','')
        else:
            attachname = attachname.replace('output/','')
        part.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', attachname))
    mesg.attach(part)
    return msg

#объявим местоположение инструкции и текст письма
manual = 'program_data/Инструкция по подключению файла подписи_RuPost_Thunderbird.pdf'
with open('program_data/message_for_mailing_list.html', 'r') as message:
    message = message.read()

#подготовим почтовый сервис к рассылке
print('Введите учётные данные почтового ящика @sirius-ft.ru, из которого будет совершена рассылка')
sender = input('Введите логин почты (только логин, "@sirius-ft.ru" не надо):  ')
sender = sender+'@sirius-ft.ru'
passwd = getpass('Введите пароль: ')
theme = 'Рассылка о подключении единообразных подписей к письмам'
#логинимся на почтовый сервер
smtp = smtplib.SMTP_SSL('mail.sirius-ft.ru', 465)
smtp.login(sender, passwd)
print ('Установлено соединение с почтовым сервером')

# Создаём папку для отправленных файлов
if not os.path.isdir('output/sent'):
    os.mkdir('output/sent')

# Перебираем файлы в папке
for filename in os.listdir(os.getcwd()+'/output'):
    # Пропускаем каталог с отработкой
    if filename == 'sent':
        continue

    # Делаем переменную с путём, чтобы не писать каждый раз субдиректорию
    way_filename = 'output/'+filename

    # Проверка файла на расширение *.html, все не *.html файлы пропускаем
    if re.search(r'.+?html',way_filename) is None:
        print('Пропущен файл',filename, '\n')
        continue
    with open(os.path.join(os.getcwd(), way_filename), 'r') as file:
      # Читаем содержимое *.html файла в переменную "attach"
      attach = file.read()
      # Ищем в переменной адрес эл.почты. Если находим - пишем его в переменную "email"
      email = re.search(r'[\w.-]+@[\w.-]+(\.\w+)+', attach)
      # Если нет - запускаем следующую итерацию
      if email is None:
         continue
      # После re.search в переменной "email" много служебной инфы. Оставляем только адрес, применяем инструкцию group
      email = email.group()

      # Готовим письмо к отправке, пишем хэдер и текст письма (текст берём из файла program_data/message_for_mailing_list.html)
      msg = MIMEMultipart()
      msg['From'], msg['To'], msg['Subject'] = sender, email, theme
      msg.attach(MIMEText(message, 'html'))
      # Крепим вложения
      attach_file(msg,way_filename)
      attach_file(msg,manual)

     # Отправляем письмо
      smtp.send_message(msg)

      # Копируем в папку с отработанными подписями, выводим сообщение о факте отправки
      os.replace (way_filename,"output/sent/"+filename)
      print('Отравлен файл подписи',filename,'для адреса',email)

# Закрываем соединение с почтовым сервером
smtp.quit()
print('Закрыто соединение с почтовым сервером')
