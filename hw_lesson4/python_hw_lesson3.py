"""
# task 1
def fn_divider(arg_1, arg_2):
    if (arg_2) == 0:
        print("division by zero")
    else:
        return arg_1 / arg_2


num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))

print("Result", fn_divider(num_1, num_2))


# task 2
def fn_user_info():
    name = input("Enter name:")
    surname = input("Enter surname:")
    birth_date = input("Enter birth date:")
    city = input("Enter city:")
    email = input("Enter email:")
    phone_no = input("Enter phone number")

    return name, surname, birth_date, city, email, phone_no


print(fn_user_info())



# task 3
def fn_big_multiplier(num_1, num_2, num_3):
    l_num = [num_1, num_2, num_3]
    l_num.sort()
    l_num.pop(0)
    return l_num[0]*l_num[1]


int_1 = int(input("Enter first number:"))
int_2 = int(input("Enter second number:"))
int_3 = int(input("Enter third number:"))
print(fn_big_multiplier(int_1, int_2, int_3))


# task 4
def fn_powof(x, y):
    return x ** y


def fn_powof_2(x, y):
    num_result = x
    num_temp = y

    if (y < 0):
        num_temp = y * -1

    while (num_temp > 1):
        num_result = num_result * x
        num_temp = num_temp - 1

    if (y < 0):
        return 1 / num_result
    else:
        return num_result


x = int(input("Enter x:"))
while x < 0:
    num1 = int(input("Enter positive value for x:"))
    x = num1
y = int(input("Enter y:"))
while y > 0:
    num2 = int(input("Enter negative value for y:"))
    y = num2

print(fn_powof(x, y))
print(fn_powof_2(x, y))


# task 5
flag = 1
s = 0

def fn_sum():
    global flag
    global s
    ls = input("Enter number or sign Q:").split()
    for i in ls:
        if i in ('q', 'Q'):
            flag = 0
            return s
        elif i.isdigit():
            s = s + int(i)
        else:
            print("Enter only number or sign Q")
    return s

while flag == 1:
    print("Result:", fn_sum())

# task 6
def int_func (s):
    return  s.lower().title()

my_str = input("Enter string")
print (int_func(my_str))

"""


# task 7
def int_func(s):
    return s.title()


my_str = input("Enter string that consint of lower case alphabetic characters:").split()
result = []
for i in my_str:
    if (i.islower() and i.isalpha()):
        result.append(int_func(i))
    else:
        print("Enter valid string")
        break
print(result)
