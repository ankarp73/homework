
# Задание 3

# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа 
# переводит метры в мили, дюймы или ярды.

print("\tЗадание 1\n\tВведите количество (число) метров. \n\tЗатем для перевода выберете предложенные Вам варианты действий.")
print()

m = int(input("Введите количество (число) метров: "))
print()

mi = 0.000621371*m
inch = 39.37*m
yd = 1.094*m

print("\t1. Для перевода метров в мили \n\t-введите цифру: 1")
print("\t2. Для перевода метров в дюймы \n\t-введите цифру: 2")
print("\t3. Для перевода метров в ярды \n\t-введите цифру: 3")
print()

i = int(input("Для перевода введите,пожалуйста,предлагаемую цифру (1-3): "))
print()

if i == 1:
    print(f'\t {m} метров - это {mi} милей\n\n>>> Программа завершена <<<')
elif i == 2:
    print(f'\t {m} метров - это {inch} дюймов\n\n>>> Программа завершена <<<')
elif i == 3:
    print(f'\t {m} метров - это {yd} ярдов\n\n>>> Программа завершена <<<')    
else:
    print(f'\n <<< ! Ввод только числа 1, 2 или 3, - перезапустите заново >>>')
    print()