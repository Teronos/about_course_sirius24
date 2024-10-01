DNK = input("Введите последовательность ДНК: ")

# Словарь
slovar = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


slovar_seq = "".join([slovar[nucleotide] for nucleotide in DNK])

# Выводим результат
print(slovar_seq)
