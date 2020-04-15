import json

avrage = {}
firms = {}
sum = 0
with open(r"D:\CloudStation\GeekBrains\31.03.2020\Python_lessons\text_7.txt", encoding='utf-8') as file:
    """счетчик фирм с прибылью"""
    i = 0
    for line in file:
        data = line.split()
        if int(data[2]) - int(data[3]) > 0:
            sum += int(data[2]) - int(data[3])
            res = int(data[2]) - int(data[3])
            firms[data[0]] = res
            i += 1
        else:
            res = int(data[2]) - int(data[3])
            firms[data[0]] = res
avrage['average_profit'] = sum / i
mylist = []
mylist.append(firms)
mylist.append(avrage)
print(mylist)

with open(r"D:\CloudStation\GeekBrains\31.03.2020\Python_lessons\my_file.json", "w") as write_f:
    json.dump(mylist, write_f, indent=4, ensure_ascii=False)
