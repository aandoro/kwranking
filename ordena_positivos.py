def orderna_positivos(list):
    if list != []:
        list_positive = [k for k in list if k > 0]
        list_positive = sorted(list_positive)
        for index, number in enumerate(list):
            if number > 0:
                list[index] = list_positive.pop(0)
        pass
    return list


print(orderna_positivos([6, 3, -2, 5, -8, 2, -2]))

print(orderna_positivos([6, 5, 4, -1, 3, 2, -1, 1]))

print(orderna_positivos([-5, -5, -5, -5, 7, -5]))

print(orderna_positivos([]))
