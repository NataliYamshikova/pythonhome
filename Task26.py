# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def degree(num1, num2):
    if num2 == 1:
        return num1
    return num1 * degree(num1, num2-1)

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print (degree(number1, number2))