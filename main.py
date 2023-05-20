def description_of_the_digit(x,):
    if x == 0:
        print ("Нулевое число")
    elif x < -1000 or x > 1000:
        print("Напиши от -1000 до 1000. Мне что по миллиону раз повторять?")
    elif x != 0:
        if x in range(-1001, -1):
            s1 = "Отрицательное "
        elif x in range(1, 1001):
            s1 = "Положительное "
        if x == 1000 or x == -1000:
            s2 = "четырёхзначное "
            sf = s1 + s2
        elif x in range(-999, -100) or (100, 1000):
            s2 = "трёхзначное "
            sf = s1 + s2
        elif x in range(-100, -10) or (10, 100):
            s2 = "двухзначное "
            sf = s1 + s2
        elif x in range(-10, -1) or (1, 10):
            s2 = "однозначное "
            sf = s1 + s2
        if x % 2 == 0:
            s3 = "чётное "
            sf = s1 + s2 + s3
        elif x % 2 != 0:
            s3 = "нечётное "
            sf = s1 + s2 + s3
        print(sf + "число")
x = int(input("Введите число от -1000 до 1000: "))
description_of_the_digit(x)
