#  Задание 1
#  Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя
#  программа выводит на экран сумму трёх чисел или произведение трёх чисел.

print("\tЗадание 1\n\tВведите поочередно три числа. \n\tЗатем выберете предложенные Вам варианты действий.")
print()

num1 = int(input("1-ое число: "))
num2 = int(input("2-ое число: "))
num3 = int(input("3-е число: "))
print()

sum = (num1+num2+num3)
proizv = (num1*num2*num3)

print("\t1. Для вывода суммы введённых Вами чисел \n\tвведите цифру: 1")
print("\t2. Для вывода произведения всех введенных Вами чисел \n\tвведите цифру: 2")
print()

i = int(input("Ввод числа: "))
print()

if i == 1:
    print(f'\tСумма введенных Вами цифр равна: {sum}\n\tПрограмма завершена.')
elif i == 2:
    print(f'\tПроизведение введенных Вами цифр равна: {proizv}\n\tПрограмма завершена.')
else:
    print(f'\t! Ввод числа только 1 или 2, - перезапустите заново >>>')