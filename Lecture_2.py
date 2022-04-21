s = input()
i = 0
while i < len(s) - 1:
    print(s[i], end='')
    if i == 3:
        ++i
    if s[i] == 'c':
        print("\nI found letter \"c\"")
    i = i + 1