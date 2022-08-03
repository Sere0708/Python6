# 1. Задача

# values = [1, 23, 42 "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
    # print('ok')
# else:
    # print('fail')


# values = lambda: print(1, 23, 42 "asdfg")
 
# values()   # hello




# 2. Задача 

# from math import pi
 
# def findFarthestOrbit(listOfOrbits):
    # return max([orbit for orbit in listOfOrbits if orbit[0] != orbit[1]], key=lambda x: pi * x[0] * x[1])
 
 
# listOfOrbits = [(1, 3),(2.5, 10),(7, 2),(6, 6),(4, 3)]
 
# print(findFarthestOrbit(listOfOrbits))




# 3. Задача

# def rifma(chant):
    # st = chant.lower().split()
    # f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    # tmp = f(st[0])
    # if all([f(i) == tmp for i in st]):
        # return 'Парам пам-пам'
    # return 'Пам парам'
 
# print(rifma("Хорошо-живет-на-свете-Винни-Пух!\
#  Оттого-поет-он-эти-Песни-вслух!"))
 
# print(rifma("И-не-важно,-чем-он-занят,\
#  Если-он-худеть-не-станет,"))
 
# print(rifma("А-ведь-он-худеть-не-станет,\
#  Если-конечно...-Вовремя-подкрепиться..."))


