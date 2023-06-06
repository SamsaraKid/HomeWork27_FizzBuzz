
# Задача 1
num1 = int(input('Введите начало диапазона:\n'))
num2 = int(input('Введите конец диапазона:\n'))

# Скучный вариант решения
# for i in range(num1, num2+1):
#     output = str(i)
#     if i % 3 == 0:
#         output = 'Fizz'
#         if i % 5 == 0:
#             output += ' Buzz'
#     elif i % 5 == 0:
#         output = 'Buzz'
#     print(output)

# Интересный вариант решения
for i in range(num1, num2 + 1):
    Divide3 = i % 3 == 0
    Divide5 = i % 5 == 0
    print(Divide3 * 'Fizz' + (Divide3 and Divide5) * ' ' + Divide5 * 'Buzz' + (not(Divide3 or Divide5)) * str(i))

# Задача 2
num1 = int(input('Введите начало диапазона:\n'))
num2 = int(input('Введите конец диапазона:\n'))

# Скучный вариант решения
# even = 0
# odd = 0
# for i in range(num1, num2 + 1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print('Сумма чётных = %s\nСумма нечётных = %s' % (even, odd))

# Интересный вариант решения
def calculateSum(n1, n2):
    return int((n1 + n2) * ((n2 - n1 + 2) / 2) / 2) # сумма членов арифметической прогрессии с разностью 2

def sumEven(n1, n2):
    n1 += int(n1 % 2 != 0) # убираем лишнее нечётное в начале
    n2 -= int(n2 % 2 != 0) # убираем лишнее нечётное в конце
    print('Сумма чётных =', calculateSum(n1, n2))

def sumOdd(n1, n2):
    n1 += int(n1 % 2 == 0) # убираем лишнее чётное в начале
    n2 -= int(n2 % 2 == 0) # убираем лишнее чётное в конце
    print('Сумма нечётных =', calculateSum(n1, n2))

sumEven(num1, num2)
sumOdd(num1, num2)
