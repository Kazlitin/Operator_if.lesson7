x = 38
if x > 0:
    print('дратути!')
if x < 0:
    print('досвидания!')

x = 38

print('дратути!')
if x < 0:
    print('Меньше нуля')
print('досвидания!')



a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a >0:
    print('успех')

if (a > b) and (a > 0 or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')

if '34' > '123':
    print('успех')

if '123' > '12':
    print("успех")

if [1, 2] > [1, 1]:
    print('успех')

if '6' > 5:           #cравнить строки и числа нельзя
    print('успех')


if [5, 6] > 5:  #сравнить список и число нельзя
    print('успех')

if '6' != 5:   #восклицательный знак позволяет вывести 'успех' так ка он означает неравенство
    print('успех')













#age = int(input("введите Ваш возраст")) # команда int - переводит то что введено с клавиатуры в целое число. Команда input переводит в строку слова и числа
#if age >= 18:   # if - используется для того что бы создать условия
#    print('OK')
#if age < 18:
#    print('NO')

#print(1 < 0)
#if '01' > "120": #когда мы сравниваем по символьно строки, в данном случае 34 больше 12 ответ получили OK (True)
#    print('OK')  #в случае когда первые два символа равны будет проверяться длина строки (где больше символов та и будет считаться большей)

#помимо "строк" и чисел 1, 2,  мы можем сравнивать [списки]
#if [2, 1] > [1, 2]: #сравниваются первые 2 элемента, помимо больше или меньше можно ставить >=;  <=; == - равенство 2 элементов
#    print('OK')   # != - означает НЕ РАВНО ! - означает что первое не равняется второму

# можем использовать последовательности, т.е. интервалы...представим что есть переменная а
#a = 5
#if 2 < a <= 5:
#    print('OK')   # тут используется одно выражение в одном if

# для того что бы проверить несколько выражений в одном if существуют специальные команджы and и or
#a = 5
#if a > 1 and a < 10:  # and - строгий оператор и левая часть выражения и правая часть обязательно должны быть правдой (True) что бы появилась ОК
#    print("OK")  #если and заменить на or то достаточно что бы хотябы одна часть выражения была правдой что бы решение было ОК

#a = 10
#if a == 5 and (a > 1 or a < 10):  # В этом случае строгое and не даёт завершить команду надписью OK
#   print('OK')

 #Строки и числа нельзя сравнивать НАПРИМЕР:
#a = 10
#if '2' > a:    # тут "2" - это строка а  а= 10 (это число)
#    print('OK')