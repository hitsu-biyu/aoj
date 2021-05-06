str = input()
q = int(input())
for _ in range(q):
    cmd = input().split()
    a, b = int(cmd[1]), int(cmd[2]) + 1
    if cmd[0] == 'replace':
        p = cmd[3]
        str = str[:a] + p + str[b:]
    elif cmd[0] == 'reverse':
        rev = str[a: b][::-1]
        str = str[:a] + rev + str[b:]
    else:
        print(str[a:b])
