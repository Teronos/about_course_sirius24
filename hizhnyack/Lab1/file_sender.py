import re
import os
import smtplib
from getpass import getpass
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

#объявим длинные переменные и текст письма
manual_name = 'Инструкция по подключению файла подписи_RuPost_Thunderbird.pdf'
with open('message.html', 'r') as message:
    message = message.read()

#подготовим почтовый сервис к рассылке
print('Введите учётные данные почтового ящика @sirius-ft.ru, из которого будет совершена рассылка')
sender = input('Введите логин почты (только логин, "@sirius-ft.ru" не надо):  ')
sender = sender+'@sirius-ft.ru'
passwd = getpass('Введите пароль: ')
#логинимся на почтовый сервер
smtp = smtplib.SMTP_SSL('mail.sirius-ft.ru', 465)
smtp.login(sender, passwd)
print('Установлено соединение с почтовым сервером')

# Переходим из корневой папки в ту где лежат подписи
os.chdir('output')

# Создаём папку для отправленных файлов
if not os.path.isdir('sent'):
    os.mkdir('sent')

# Перебираем файлы в папке
for filename in os.listdir(os.getcwd()):
    # Пропускаем каталог с отработкой
    if filename == 'sent':
        continue
    # Проверка файла на расширение *.html, все не *.html файлы пропускаем
    if re.search(r'.+?html',filename) is None:
        print('Пропущен файл',filename, '\n')
        continue
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
      # Читаем содержимое *.html файла в переменную "attach"
      attach = file.read()
      # Ищем в переменной адрес эл.почты. Если находим - пишем его в переменную "email"
      email = re.search(r'[\w.-]+@[\w.-]+(\.\w+)+', attach)
      # Если нет - запускаем следующую итерацию
      if email is None:
         continue
      # После re.search в переменной "email" много служебной инфы. Оставляем только адрес, применяем инструкцию group
      email = email.group()

      # Готовим письмо к отправке, пишем хэдер и текст письма (текст берём из файла message.html корневого каталога программы)
      msg = MIMEMultipart()
      msg['From'], msg['To'], msg['Subject'] = sender, email, "Рассылка о подключении единообразных подписей к письмам"
      msg.attach(MIMEText(message, 'html'))

      # Крепим к письму файл подписи
      with open(filename, "rb") as att_file:
          part = MIMEBase('application', 'octet-stream')
          part.set_payload(att_file.read())
          encoders.encode_base64(part)
          part.add_header('Content-Disposition', 'attachment', filename=('utf-8','',filename))
      msg.attach(part)

      # Крепим к письму файл с инструкцией по установке подписи
      with open('../'+manual_name, "rb") as att_file:
          part = MIMEBase('application', 'octet-stream')
          part.set_payload(att_file.read())
          encoders.encode_base64(part)
          part.add_header('Content-Disposition', 'attachment', filename=('utf-8','',manual_name))
      msg.attach(part)

      # Отправляем письмо
      smtp.send_message(msg)

      # Копируем в папку с отработанными подписями, выводим сообщение о факте отправки
      os.replace (filename,"sent/"+filename)
      print('Отравлен файл подписи',filename,'для адреса',email)

# Закрываем соединение с почтовым сервером
smtp.quit()
print('Закрыто соединение с почтовым сервером')
