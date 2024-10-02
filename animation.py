import time
import os

lst = []
with open('text.txt', encoding='utf-8') as file:
    frame = []
    for line in file.readlines():
        if line == '\n':
            lst.append(frame)
            frame = []
        else:
            frame.append(line)

while True:
    for i in range(len(lst)):
        os.system("cls")
        print(''.join(lst[i]))
        time.sleep(0.1)
