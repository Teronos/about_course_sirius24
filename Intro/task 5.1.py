#В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и «G».
#Нужно написать программу, которая получате на вход последовательность ДНК и на выходе отображает комлементарную ей.

from types import GeneratorType
dnk = input("Введите цепочку ДНК: ")

for i in dnk:
  match i:
    case "A":
      print("T", end = "")
    case "T":
      print("A", end = "")
    case "C":
      print("G", end = "")
    case "G":
      print("C", end = "")
    case _ :
      print ("error")