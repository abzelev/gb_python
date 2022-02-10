"""
#task 1
f = open('file1.txt','w',encoding='utf-8')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()

# task 2
f = open('file2.txt', 'r', encoding='utf-8')
l_cnt = 0
for i in f.readlines():
    w_cnt = 0
    l_cnt += 1
    w_cnt = len(i.split())
    print("Words count in line-",l_cnt,":" , w_cnt)
print ("Line count:" , l_cnt)
f.close()


#task 3
f = open('file3.txt','r', encoding='utf-8')
for i in f.readlines():
    income = i.split()
    if float(income[1]) < 20000:
        print(income[1])
f.close()
"""
# task 4
my_dict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}

f = open('file4.txt', 'r', encoding='utf-8')
f2 = open('file4_new.txt', 'w', encoding='utf-8')
for i in f.readlines():
    temp = i.split()
    print(my_dict.get(int(temp[2])) + temp[1] + temp[2])
    f2.write(my_dict.get(int(temp[2])) + temp[1] + temp[2] + '\n')
f.close()
f2.close()


# task 5
from random import randint

with open('file5.txt', 'w', encoding='utf-8') as f:
    for _ in range(10):
        f.write(str(randint(0, 10))+' ')

with open('file5.txt', 'r', encoding='utf-8') as f1:
    sm = 0
    ls = f1.readline().split()
    print(ls)
    for s in ls:
        sm = sm+int(s)
    print('Sum: ' + str(sm))

# task 6
my_dict = {}
with open('file6.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        temp = i.split()
        lecture = temp[0]
        l_hours = 0

        for z in temp:
            n_filter = filter(str.isdigit, z)
            n_string = "".join(n_filter)
            if (n_string.isdigit()):
                l_hours = l_hours + int(n_string)
        my_dict.__setitem__(lecture, l_hours)
print(my_dict)

# task 7
dict_profit = {}
dict_avg = {}
avg_profit = 0
cnt = 0
with open('file7.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        firm_name = i.split()[0]
        profit = float(i.split()[2]) - float(i.split()[3])
        if profit > 0:
            avg_profit = avg_profit + profit
            cnt += 1
        dict_profit.__setitem__(firm_name, profit)
    dict_avg.__setitem__("avg_profit", avg_profit / cnt)
ls = [dict_profit, dict_avg]
print(ls, file=open("file7.json", 'w', encoding='utf-8'))
