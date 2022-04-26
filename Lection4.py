def task1():
    print("task1")
    s = input().split(',')
    s2 = input(f"Введите столько же слов: {len(s)} \n").split(',')
    d = {}
    for i in range(len(s)):
        d.update({s[i]: s2[i]})
    print(d)


def task2():
    print("task2")
    my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    dict = {}
    for i in sorted(my_dict.values()):
        for k in my_dict.keys():
            if my_dict[k] == i:
                dict[k] = my_dict[k]
                my_dict.pop(k)
                break
    i = 0
    print("Три максимальных значений: ")
    for a in dict:
        if len(dict) - i >= 3:
            break
        print(a, end=" ")
        i += 1


def is_year_leap(year):
    if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
        return True
    else:
        return False


task1()
task2()
print(is_year_leap(int(input("Input year: "))))
