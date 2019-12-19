# import math
# import random
# import re
import struct
import decimal
from fractions import Fraction

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
# print(ord('\n'))        # \n - один символ, кодируемый как десятичное значение 10
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
# print('sp\xc4m')                # Python 3.X: обычные строки str являются текстом Unicode
# print(b'a\x01c')                # Строки bytes - это данные, основанные на байтах
# print(u'sp\u00c4m')             # Литералы Unicode из Python 2.X работают в Python 3.3+: просто строка str
# print('spam')                   # Символы могут занимать 1, 2 или 4 байта в памяти
# print('spam'.encode('utf8'))    # В UTF-8 кодируется как 4 байта в файлах
# print('spam'.encode('utf16'))   # Но в UTF-16 кодируется как 10 байт
# print('sp\xc4\u00c4\U000000c4m')
# print(u'sp\xc4\u00c4\U000000c4m')


# Сопоставление с образцом
# match = re.match('Hello[\t]*(.*)world', 'Hello      Python world')
# print(match.group(1))
# match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
# print(match.groups())
# print(re.split('[/:]', 'usr/home/lumberjack'))


# Списки
# Операции над последовательностями
# L = [123, 'spam', 1.23]             # Список из трех объектов разных типов
# print(len(L))                       # Количество элементов в списке
# print(L[0])                         # Индексация по позиции
# print(L[:-1])                       # Нарезание списка возвращает новый список
# print(L + [4, 5, 6])                # Конкатенация и повторение также создают новый список
# print(L * 2)
# print(L)                            # Исходный список не изменился


# Операции, специфичные для типа
# L.append('NI')                      # Увеличение: добавление объекта в конец списка
# print(L)
# L.pop(2)                            # Уменьшение: удаление элемента из середины
# print(L)                            # del L[2] также выполняет удаление из списка
# M = ['bb', 'aa', 'cc']
# M.sort()
# print(M)
# M.reverse()
# print(M)                            # В обоих случаях методы модифицируют список напрямую


# Контроль границ
# print(L[99])
# L[99] = 1                         # Индексация и присваивание за концом списка всегда считается ошибкой


# Вложение
# M = [[1, 2, 3],                     # Матрица 3 х 3 в виде вложенных списков
#      [4, 5, 6],                     # При использовании квадратных скобок код
#      [7, 8, 9]]                     # может занимать несколько строк
# print(M)
# print(M[1])                         # Получить строку 2
# print(M[1][2])                      # Получить строку 2 и затем элемент 3 внутри этой строки


# Списковые включения
# col2 = [row[1] for row in M]        # Собрать элементы в столбце 2
# print(col2)
# print(M)                            # Матрица не изменилась
# col = [row[1] + 1 for row in M]     # Добавить 1 в каждом элементе в столбце 2
# print(col)
# col = [row[1] for row in M if row[1] % 2 == 0]      # Отфильстровать нечетные элементы
# print(col)
# diag = [M[i][i] for i in [0, 1, 2]]                 # Собрать диагональ из матрицы
# print(diag)
# doubles = [c * 2 for c in 'spam']                   # Повторить символы в строке
# print(doubles)
# print(list(range(4)))
# print(list(range(-6, 7, 2)))
# print([[x ** 2, x ** 3] for x in range(4)])         # Множество значений, фильтры if
# print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])
# G = (sum(row) for row in M)         # Создать генератор сумм элементов в строках
# print(next(G))
# print(next(G))                      # Запустить протокол итерации next()
# print(next(G))
# print(list(map(sum, M)))            # Отобразить sum на элементы M
# print({sum(row) for row in M})      # Создать множество сумм элементов в строках
# print({i : sum(M[i]) for i in range(3)})     # Создать таблицу ключей/значений значений сумм элементов в строках
# print([ord(x) for x in 'spaam'])             # Список порядковых чисел для символов
# print({ord(x) for x in 'spaam'})             # Множество с удаленными дубликатами
# print({x : ord(x) for x in 'spaam'})         # Словарь с уникальными ключами
# print((ord(x) for x in 'spaam'))             # Генератор значений


# Словари
# Операции над отображениями
# D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
# print(D['food'])                        # Извлечь значение, связанное с ключом 'food'
# D['quantity'] += 1                      # Добавить 1 к значению, связанному с ключом 'quantity'
# print(D)
# D = {}
# D['name'] = 'Bob'                       # Присваивание приводит к созданию ключей
# D['job'] = 'dev'
# D['age'] = 30
# print(D)
# print(D['name'])
# bob1 = dict(name='Bob', job='dev', age=40)                       # Ключевые слова
# print(bob1)
# bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))     # Связывание вместе
# print(bob2)


# Снова о вложении
# rec = {'name': {'first': 'Bob', 'last': 'Smith'},
#        'jobs': ['dev', 'mgr'],
#        'age': 40.5}
# print(rec['name'])                      # 'name' - вложенный словарь
# print(rec['name']['last'])              # Индексация во вложенном словаре
# print(rec['jobs'])                      # 'jobs' - вложенный список
# print(rec['jobs'][-1])                  # Индексация во вложенном списке
# rec['jobs'].append('janitor')           # Расширение списка дложностей на месте
# print(rec)
# rec = 0                                 # Теперь область памяти, занимаемая объектом, восстановлена


# Недостающие ключи: проверки if
# D = {'a': 1, 'b': 2, 'c': 3}
# print(D)
# D['e'] = 99                        # Присваивание новому ключу увеличивает словари
# print(D)
# # print(D['f'])                      # Ссылка на несуществующий ключ приводит к ошибке
# print('f' in D)
#
# if not 'f' in D:                   # Единственный оператор выбора в Python
#      print('missing')
#
# value = D.get('x', 0)              # Индекс со стандартным вариантом
# print(value)
# value = D['x'] if 'x' in D else 1  # Форма выражения if/else
# print(value)


# Сортировка ключей: цикл for
# D = {'a': 1, 'c': 3, 'b': 2}
# print(D)
# Ks = list(D.keys())                # Неупорядоченный список ключей
# print(Ks)
# Ks.sort()                          # Отсортированный список ключей
# print(Ks)
#
# for key in Ks:                     # Проход по отсортированным ключам
#      print(key, '=>', D[key])
#
# print(D)
#
# for key in sorted(D):
#      print(key, '=>', D[key])
#
# for c in 'spam':
#      print(c.upper())
#
# x = 4
# while x > 0:
#      print('spam!' * x)
#      x -= 1


# Итерация и оптимизация
# squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
# print(squares)
#
# squares = []
# for x in [1, 2, 3, 4, 5]:                    # Это то, что делает списковое включение
#      squares.append(x ** 2)                  # Оба инструмента внутренне следуют протоколу итерации
#
# print(squares)


# Кортежи
# T = (1, 2, 3, 4)                   # Кортеж из 4х элементов
# print(len(T))                      # Длина
# print(T + (5, 6))                  # Конкатенация
# print(T[0])                        # Индексация, нарезание и т.д.
# print(T.index(4))                  # Методы кортежей: 4 однаруживается по индексу 3
# print(T.count(4))                  # 4 обнаруживается один раз
# T[0] = 2                           # Кортежи неизменяемы
# T = (2,) + T[1:]                   # Создает новый кортеж для нового значения
# print(T)
# T = 'spam', 3.0, [22, 33, 44]
# print(T[1])
# print(T[2][1])
# T.append(4)


# Файлы
# f = open('data.txt', 'w')           # Создать новый файл в режиме записи ('w')
# print(f.write('Hello\n'))           # Записать в него строки символов
# print(f.write('world\n'))           # Возвратить количество записанных символов
# f.close()                           # Закрыть для сбрасывания буферов вывода на диск
#
# f = open('data.txt')                # 'r' (чтение) - стандартный режим обработки
# text = f.read()                     # Прочитать все содержимое файла в строку
# print(text)
# print(text.split())                 # Содержимое файла - всегда строка
#
# for line in open('data.txt'): print(line)
#
# print(dir(f))
# print(help(f.seek))


# Файлы с двоичными байтами
# packed = struct.pack('>i4sh', 7, b'spam', 8)            # Создать упакованные двоичные данные
# print(packed)                                           # 10 байт, не объекты и не текст
#
# file = open('data.bin', 'wb')                           # Открыть двоичный файл для записи
# print(file.write(packed))                               # Записать упакованные двоичные данные
# file.close()
#
# data = open('data.bin', 'rb').read()                    # Открыть/прочитать двоичный файл данных
# print(data)                                             # 10 байт, неизмененные
# print(data[4:8])                                        # Нарезать байты в середине
# print(list(data))                                       # Последовательность 8-битных байт
# print(struct.unpack('>i4sh', data))                     # Снова распаковать в объекты


# Файлы с текстом Unicode
# S = 'sp\xc4m'                       # Текст Unicode, отличающийся от ASCII
# print(S)
# print(S[2])                         # Последовательность символов
#
# file = open('unidata.txt', 'w', encoding='utf-8')       # Записать/закодировать текст UTF-8
# print(file.write(S))                # Записано 4 символа
# file.close()
#
# text = open('unidata.txt', encoding='utf-8').read()     # Прочитать/декодировать текст UTF-8
# print(text)
# print(len(text))                    # 4 символ (кодовые строчки)
#
# raw = open('unidata.txt', 'rb').read()                  # Читать закодированные байты
# print(raw)
# print(len(raw))
#
# print(text.encode('utf-8'))         # Вручную кодировать в байты
# print(raw.decode('utf-8'))          # Вручную декодировать в строку
#
# print(text.encode('latin-1'))       # Байты отличаются от других
# print(text.encode('utf-16'))
# print(len(text.encode('latin-1')), len(text.encode('utf-16')))
# print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))      # Но декодируются в ту же смаую строку


# Прочие основные типы
# X = set('spam')                 # Создать множество из последовательности
# Y = {'h', 'a', 'm'}             # Создать множество с помощью литералов
#
# print(X, Y)                     # Кортеж из двух множеств без круглых скобок
# print(X & Y)                    # Пересечение
# print(X | Y)                    # Объединение
# print(X - Y)                    # Разность
# print(X > Y)                    # Надмножество
# print({n ** 2 for n in [1, 2, 3, 4]})           # Включение множеств в Python 3.X, 2.7
#
# print(list(set([1, 2, 1, 3, 1])))               # Фильстрация дубликатов (возможно неупорядоченных)
# print(set('spam') - set('ham'))                 # Нахождение разностей в коллекции
# print(set('spam') == set('aspm'))               # Нейтральная к порядку проверка равенства
#
# print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'ham', 'spam'])
#
# print(1/3)                      # Математика с плавающей точкой
# print(2/3 + 1/2)
#
# d = decimal.Decimal('3.141')
# print(d + 1)
#
# decimal.getcontext().prec = 2
# print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
#
# f = Fraction(2, 3)              # Дроби: числитель + знаменатель
# print(f + 1)
# print(f + Fraction(1, 2))
#
# print(1 > 2, 1 < 2)             # Булевые значения
# print(bool('spam'))             # Булевое значение объекта
# X = None                        # Заполнитель None
# print(X)
# L = [None] * 100
# print(L)                        # Инициализировать список сотней объектов None
#
# print(type(L))                  # Типы являются классами и наоборот
# print(type(type(L)))
#
# if type(L) == type([]):         # Проверка типа при необходимости
#     print('yes')
#
# if type(L) == list:             # Использование имени типа
#     print('yes')
#
# if isinstance(L, list):         # Объекто-ориентированная проверка
#     print('yes')


# Классы, определяемые пользователем
class Worker:
    def __init__(self, name, pay):          # Инициализировать при создании self - новый объект
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]        # Разбить строку по пробелам
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)         # Обновить pay на месте

bob = Worker('Bob Smith', 50000)            # Создать два экземпляра класса
sue = Worker('Sue Jones', 60000)            # Каждый имеет name и pay

print(bob.lastName())                       # Вызвать метод: bob - это self
print(sue.lastName())                       # sue - это self
sue.giveRaise(.10)                          # Обновить атрибут pay в экземпляре sue
print(sue.pay)