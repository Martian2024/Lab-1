#вариант задания - 4
from math import ceil, sqrt

WHITE_BACKGROUND = '\u001b[47m'
BLACK_BACKGROUND = '\u001b[40m'
RED_BACKGRAUND = '\u001b[41m'
RED_TEXT = '\u001b[31m'
RESET = '\u001b[0m'

width, height = 10, 4
print(WHITE_BACKGROUND + '\n'.join([' ' * width for _ in range(height // 2)]) + RESET)
print(RED_BACKGRAUND + '\n'.join([' ' * width for _ in range(height // 2)]) + RESET)
print(RESET + RED_TEXT + 'Bobr kurwa' + RESET)
print()

print(WHITE_BACKGROUND + ' ' * 13 + RESET)
print(WHITE_BACKGROUND + ' ' + BLACK_BACKGROUND + ' ' * 11 + WHITE_BACKGROUND + ' ' + RESET)
print(WHITE_BACKGROUND + ' ' * 6 + BLACK_BACKGROUND + ' ' + WHITE_BACKGROUND + ' ' * 6 + RESET)
print(WHITE_BACKGROUND + ' ' + BLACK_BACKGROUND + ' ' * 11 + WHITE_BACKGROUND + ' ' + RESET)
print(WHITE_BACKGROUND + ' ' * 3 + BLACK_BACKGROUND + ' ' + WHITE_BACKGROUND + ' ' * 5 + BLACK_BACKGROUND + ' ' + WHITE_BACKGROUND + ' ' * 3 + RESET)
print(WHITE_BACKGROUND + ' ' + BLACK_BACKGROUND + ' ' * 11 + WHITE_BACKGROUND + ' ' + RESET)
print(WHITE_BACKGROUND + ' ' * 13 + RESET)
print(RESET + '')

print('\t\ty=x^0.5')
matrix_width, matrix_height = 10, 10
for y in range(matrix_height - 1, -1, -1):
    output = str(y) + '|'
    for x in range(matrix_width):
        if y == ceil(sqrt(x)):
            output += RED_TEXT + '*' + RESET
        else:
            output += ' '
    print(output)
print('  ' + '‾' * 10)
print('  0123456789')
print()

with open('sequence.txt') as file:
    nums = list(map(lambda x: abs(float(x)), file.readlines()))
    sum1 = sum(nums[:len(nums) // 2])
    print(f'Процентное отношение сумм первых 125 чисел и вторых 125 чисел:{(sum1 / sum(nums)) * 100}% ' + '█' * (int((sum1 / sum(nums)) * 100) // 10) + '░' * (10 - (int((sum1 / sum(nums)) * 100) // 10)))

print()
input('Для выхода нажмите Enter')