number = input("Введите номер билета: ")
if len(number) != 6: #проверка условия что ввели корректно номер из 6 ти цифр
    print("Вы ввели не верно номер билета")
else:
    digits = list(map(int, number))
    if sum(digits[:3]) == sum(digits[3:]):
        print("УРА! Ваш билет счатсливый!")
    else:
        print("К сожалению, это не счастливый билет")
