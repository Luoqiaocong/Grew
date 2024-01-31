import csv


def seek_message(args):
    found = False  # 使用标志位判断是否找到匹配项
    for i in args:
        for j in ls:
            if str(i) == j[0]:
                print(f'{j[1]}假期是{j[2]}到{j[3]}之间')
                found = True
                break  # 找到匹配项后立即跳出内层循环
    if not found:
        print('没有找到')


ls = []
with open('PY301-vacations.csv', 'r') as f:
    reader = list(csv.reader(f))
    for data in reader[1:]:
        ls.append(tuple(data))
    while True:
        math = tuple(input('请输入序号(1-7):').split())
        seek_message(math)
