A = input("Введите через пробел последовательность чисел ").split() #Ввод последовательности через пробел
L = list(map(int, A)) #Преобразование последовательности в список чисел
print(L)
Number = int(input('Введите любое число  '))

def sortt(array): #Функция сортировки пузырьком
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return(array)

SortL = sortt(L)
print('Сортированный список:', SortL)

G = len(SortL)

if Number < SortL[0] or Number > SortL[-1]:
    print('Введенное число лежит за пределами списка')
else:

    i = 0
    while SortL[i] < Number:
        if SortL[i+1] >= Number:
            count = i
        i = i + 1

    print("Номер позиции элемента списка, меньшего введенного числа ", count)


