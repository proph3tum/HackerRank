# list1 = [x for x in range(10)]
# print(list1)

# print([[x, y, z] for x in [1, 2, 3] for y in [4, 5, 6] for z in [6, 8, 9]])

# ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
# print(ListOfThreeMultiples)

# Даны три целых числа x, y, z, вместе с целым числом n
# Выведите список всех возможных координат, заданных (i,j,k) на трехмерной сетке, где сумма i + j + k не равно n


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(result)


