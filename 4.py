string = input('введите влова через пробел: ')
words = (string.split())

for ind, word in enumerate(words, 1):
    if len(word) > 10:
        print(f'{ind}: {word[:10]}')
    else:
        print(f'{ind}: {word}')
