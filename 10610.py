n = input()

n_list = list(map(int, str(n)))

n_list.sort(reverse=True)

# print(n_list)

if 0 in n_list and sum(n_list) % 3 == 0:
    for i in range(len(n_list)):
        print(n_list[i], end='')
else:
    print(-1)
