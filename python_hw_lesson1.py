"""
# task 1
int_var = input("Enter number:")
str_var = input("Enter string:")
print(int_var)
print(str_var)


# task 2
int_sec = int(input("Enter time in seconds:"))
int_minute: int = int_sec // 60
int_hour: int = int_sec // 3600
int_sec = int_sec % 360
print(f"{int_hour}:{int_minute}:{int_sec}")


# task 3
int_n = input("Enter number n:")
print(int(int_n)+int(int_n+int_n)+int(int_n+int_n+int_n))


# task 4
a = int(input("Enter number: "))  # 15156
max_num = 0
while int(a) > 1:
    b = a % 10
    if max_num < b:
        max_num = b
    a = a // 10
print(max_num)


# task 5
v = int(input("Выручка: "))
i = int(input("Издержки: "))
if v > i:
    print("Работает в плюс")
elif i > v:
    print("Работает в минус")
else:
    print("В ноль")


#task 6
v = int(input("Выручка: "))
i = int(input("Издержки: "))
if v > i:
    print("Работает в плюс")
    r = (v-i)*100/v
    print("Рентабельность:", r)
    s = int(input("Количество сотрудников:"))
    print("Прибыль на одного сотрудника:", (v-i)/s)
elif i > v:
    print("Работает в минус")
else:
    print("В ноль")

"""
# task 7
a = int(input("a"))
b = int(input("b"))
i = 1
while a <= b:
    i = i + 1
    a = a + a * 0.1
print(i)
