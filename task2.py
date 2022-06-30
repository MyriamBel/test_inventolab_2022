"""
Задание 2 "Стремится к нулю или к бесконечности?"
	(n! обозначает factorial(n))
	Будет ли выражение вида:
		un = (1 / n!) * (1! + 2! + 3! + ... + n!)
	стремится к 0 или к бесконечности?
	Реализуйте функцию, которая расчитывает значение un для целочисленных n > 1
	(с точностью не хуже 6 знаков после запятой).
"""


"""
Логика:
Напишем базовую (1) функцию вычисления факториала, которую можем обернуть в функцию(2), 
вычисляющую некоторую формулу с использованием этого факториала. Функцию 2 завернем в функцию (3), которая будет 
анализировать, куда стремится функция 2 - к 0 или бесконечности.
    # Декоратор позволяет применить дополнительную логику к какой-либо базовой функции.
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
"""


def seq_type(function_to_decorate):
    # Эта обертка перехватывает аргумент, получаемый перехватываемой функцией и отвечает,
    # будет ли функция стремиться к 0 или к бесконечности.
    # Последовательность может возрастать, убывать или быть монотонной.
    # Если она не стремится к 0 и не стремится к бесконечности - она монотонная.
    def wrapper(arg):
        to0 = False
        to_infinity = False
        list_ansvers = []
        for i in range(1, arg+1):
            list_ansvers.append(function_to_decorate(i))
            if i > 1:
                sign = list_ansvers[i-1] - list_ansvers[i-2]
                if sign < 0:
                    to0 = True
                    to_infinity = False
                elif sign > 0:
                    to_infinity = True
                    to0 = False
                else:
                    to0 = False
                    to_infinity = False
        print(str(list_ansvers))
        print("Стремится к 0: " + str(to0) + "\nСтремится к бесконечности: " + str(to_infinity))
        # prev_value = function_to_decorate(arg-1)
        # current_value = function_to_decorate(arg)
        # where = "cтремится к бесконечности" if current_value > prev_value else "cтремится к нулю" if current_value < prev_value else "является монотонной"
        # ansver = 'На отрезке от 1 до {} функция {}'.format(arg, where)
        # print(ansver)
        return function_to_decorate(arg)
    return wrapper


def factorial_from1_toN(function_to_decorate):
    def wrapper(arg):
        total = function_to_decorate(arg)
        summ_factorials = 0
        for i in range(1, arg):
            summ_factorials += function_to_decorate(i)  # Сама функция
        summ_factorials += total
        return round(summ_factorials/total, 6)
    # Вернём эту функцию
    return wrapper


@seq_type
@factorial_from1_toN
def factorial(number):
    """
    Вычислим факториал числа number: перемножим все числа от 1 до number между собой.
    """
    answer = 1
    for i in range(1, number + 1):
        answer *= i
    return answer


x = int(input("Введите число"))
if x < 2:
    raise ValueError("Число должно быть больше единицы.")
value = factorial(x)
print(value)
