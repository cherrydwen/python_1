example = 'Экстраполяция'
print(example[0])
print(example[-1])
length=len(example)//2
# print(example[length:] - почему-то использование переменной не работает, хотя она int
print(example[6:])
print(example[::-1])
print(example[::2])