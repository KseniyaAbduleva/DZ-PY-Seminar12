# Задача 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

""" def sum (number):
    sum = 0
    for i in number:
        if i != '.':
            sum = sum + int(i)
    return sum


number = input('Введите вещественное число: ')

print (sum(number)) """

# Задача 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

""" def factorial(n):
    count = 1
    for i in range (1, n+1):
        count*=i
        print(count)

n = int(input('Введите число N: '))
factorial(n) """

# Задача 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.

""" n = int(input('Enter number: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n)))) """

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

""" from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
x = open('file.txt','r')
result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(result) """

# Задача 5. Реализуйте алгоритм перемешивания списка.

""" from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число чтобы указать число элементов: '))
numbers = list(n)
print(numbers)
for i in range (len(numbers)):
    random_num = randint(i, n-1)
    temp = numbers[i]
    numbers[i] = numbers[random_num]
    numbers[random_num] = temp

print(numbers) """
