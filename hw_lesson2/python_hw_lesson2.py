"""
# task 1
i = 1
j = 'Hello World'
k = 1 / 4
l = [i, j, k]
while l.__len__():
    print(type(l.__getitem__(0)))
    l.pop(0)


# task 2
l = list(input())
l_reverse = list()
t = list()
while l:
    t = l[0:2]
    t.reverse()
    l_reverse.extend(t)
    if(l) :
        l.pop(0)
    if(l):
        l.pop(0)
print(l_reverse)

# task 3
m = int(input("Enter number between 1 and 12: "))
my_dict = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
           8: 'summer', 9: 'outumn', 10: 'outumn', 11: 'outumn', }
print(my_dict.get(m))


#task 4

s = input("Enter sentence: ")
i = 1
ss = str()
for x in s.split():
    ss = str(ss+str(i)+x[0:10]+"\n")
    i = i+1
print (ss)
"""

#task 5
my_list = [7, 5, 3, 3, 2]
i = int(input("Enter number:"))
my_list.append(i)
my_list.sort()
my_list.reverse()
print (my_list)