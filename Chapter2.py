import math
import random

# Числа
# print(123 + 222)                    # Целочисленное сложение
# print(1.5 * 4)                      # Умножение с плавающей точкой
# print(2 ** 100)                     # 2 в степени 100
# print(len(str(2 ** 1000000)))       # Сколько цифр в действительно БОЛЬШОМ числе?
# print(3.1415 * 2)                   # str: вид, дружественный к пользователю
# print(math.pi)
# print(math.sqrt(85))
# print(random.random())


# Строки
# S = 'Spam'          # Создать 4-символьную строку и присвоить её некоторому значению
# print(len(S))       # Длина
# print(S[0])         # Первый элемент в S, который индексируется по позиции, начиная с нуля
# print(S[1])         # Второй элемент слева
# print(S[-1])        # Последний элемент с конца в S
# print(S[-2])        # Второй элемент с конца в S
# print(S[-1])        # Последний элемент в S
# print(S[len(S)-1])  # Отрицательная индексация, сложный путь
# print(S[1:3])       # Срез S со смещения 1 до 2 (не 3)
# print(S[1:])        # Все после первого элемента (1:len(S))
# print(S[0:3])       # Все кроме последнего элемента
# print(S[:3])        # То же, что и S[0:3]
# print(S[:-1])       # Снова вес кроме последнего элемента, но проще (0:-1)
# print(S[:])         # Вся строка S как копия верхнего уровня (0:len(S))
# print(S + 'xyz')    # Конкатенация
# print(S * 8)        # Повторение


# Неизменяемость
# S[0] = 'z'           # Неизменяемые объекты нельзя модифицировать
# S = 'z' + S[1:]        # Но мы можем выполнять выражения для создания новых объектов
# print(S)
# S = 'shrubbery'
# L = list(S)            # Развернуть в список [...]
# print(L)
# L[1] = 'c'             # Изменить на месте
# L = ''.join(L)         # Объединить с пустым разделителем
# print(L)
# B = bytearray(b'spam') # Гибрид байтов/списка
# B.extend(b'eggs')      # b необходимо в Python 3.X, но не в Python 2.X
# print(B)               # B[i] = ord(x) тоже здесь работает
# B.decode()             #  ???? Преобразовать в обычную строку
# print(B)


# Методы, специфичные для типа
# S = 'Spam'
# print(S.find('pa'))            # Найти смещение подстроки в S
# print(S.replace('pa', 'XYZ'))  # Заменить вхождение подстроки в S другой подстрокой
# print(S)
# line = 'aaa,bbb,cccc,dd'
# line = line.split(',')         # Разбить по разделителю в список подстрок
# print(line)
# S = 'spam'
# print(S.upper())               # Преобразовать в верхний и нижний регистры
# print(S.isalpha())             # Проверить содержимое: isalpha, isdigit и т.д.
# line = 'aaa,bbb,cccc,dd\n'
# print(line.rstrip())           # Удалить пробельные символы с правой стороны
# print(line.rstrip().split(','))# Скомбинировать две операции
# print('%s,eggs, and %s' % ('spam', 'SPAM'))           # Выражение форматирования (все версии)
# print('{0},eggs, and {1}'.format('spam', 'SPAM'))     # Метод форматирования (2.6+, 3.0+)
# print('{},eggs, and {}'.format('spam', 'SPAM'))       # Номера необязательны (2.7+, 3.1+)
# print('{:,.2f}'.format(296999.257))                   # Разделители, десятичные цифры
# print('%.2f | %+05d' % (3.14159, -42))


# Получение справки
# S = 'string'
# print(dir(S))
# print(S + 'NI!')
# print(S.__add__('NI!'))
# print(help(S.replace))


# Другие способы написания строк
# S = 'A\nB\tC'           # \n - конец строки, \t - табуляция
# print(S)
# print(len(S))           # Как \n, так и \t являются одним символом
# print(ord('\n'))        # \n - один символ, кодируемый какдесятичное значение 10
# S = 'A\0B\0C'           # \0, байт с двоичными нулями, не завершает строку
# print(len(S))
# print(S)                # Непечатаемые символы отображаются как шестнадцатеричные управляющие последовательности \xNN
# msg = """
# aaaaaaaaaa
# bbb'''bbbbbbbbbb""bbbbb'bbb
# cccccccccc
# """
# print(msg)


# Строки Unicode
print('sp\xc4m')                # Python 3.X: обычные строки str являются текстом Unicode
print(b'a\x01c')                # Строки bytes - это данные, основанные на байтах
print(u'sp\u00c4m')             # Литералы Unicode из Python 2.X работают в Python 3.3+: просто строка str
print('spam')                   # Символы могут занимать 1, 2 или 4 байта в памяти
print('spam'.encode('utf8'))    # В UTF-8 кодируется как 4 байта в файлах
print('spam'.encode('utf16'))   # Но в UTF-16 кодируется как 10 байт
print('sp\xc4\u00c4\U000000c4m')
print(u'sp\xc4\u00c4\U000000c4m')