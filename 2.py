seconds = int(input('Введите количество секунд: '))

hours = seconds // 3600

if hours < 10:
    hours = f'0{hours}'
else:
    hours = f'{hours}'

minutes = (seconds - int(hours) * 3600) // 60

if minutes < 10:
    minutes = f'0{minutes}'

seconds = seconds - int(hours) * 3600 - int(minutes) * 60
if seconds < 10:
    seconds = f'0{seconds}'

print(f'{hours}:{minutes}:{seconds}')

