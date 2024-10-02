#вариант задания - 4
from math import ceil, sqrt

white_background = '\u001b[47m'
black_bachground = '\u001b[40m'
red_background = '\u001b[41m'
red_text = '\u001b[31m'
reset = '\u001b[0m'

width, height = 10, 4
print(white_background + '\n'.join([' ' * width for _ in range(height // 2)]))
print(red_background + '\n'.join([' ' * width for _ in range(height // 2)]))
print(reset + red_text + 'Bobr kurwa')
print()

print(white_background + ' ' * 13)
print(' ' + black_bachground + ' ' * 11 + white_background + ' ')
print(' ' * 6 + black_bachground + ' ' + white_background + ' ' * 6)
print(' ' + black_bachground + ' ' * 11 + white_background + ' ')
print(' ' * 3 + black_bachground + ' ' + white_background + ' ' * 5 + black_bachground + ' ' + white_background + ' ' * 3)
print(' ' + black_bachground + ' ' * 11 + white_background + ' ')
print(white_background + ' ' * 13)
print(reset + '')

print('\t\ty=x^0.5')
matrix_width, matrix_height = 10, 10
for y in range(matrix_height - 1, -1, -1):
    output = str(y) + '|'
    for x in range(matrix_width):
        if y == ceil(sqrt(x)):
            output += red_text + '*' + reset
        else:
            output += ' '
    print(output)
print('  ' + '‾' * 10)
print('  0123456789')
print()

with open('sequence.txt') as file:
    nums = list(map(lambda x: abs(float(x)), file.readlines(0)))
    sum1 = sum(nums[:125])
    sum2 = sum(nums[125:251])
    print(f'Процентное отношение сумм первых 125 чисел и вторых 125 чисел:{int((sum1 / sum2) * 100)}% ' + '█' * (int((sum1 / sum2) * 100) // 10) + '░' * (10 - (int((sum1 / sum2) * 100) // 10)))

print()
input('Для выхода нажмите Enter')