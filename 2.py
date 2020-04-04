seconds = int(input('Введите количество секунд: '))

hours = seconds // 3600
minutes = (seconds - int(hours) * 3600) // 60
seconds = seconds - int(hours) * 3600 - int(minutes) * 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

