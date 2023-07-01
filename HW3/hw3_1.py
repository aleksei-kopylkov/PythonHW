initial_list = [1, 1, 3, 32, 21, 32, 2, 1, 12, 65, 45, 33, 456, 45, 45]
res_list =[]
for item in initial_list:
    if initial_list.count(item) > 1 and item not in res_list:
        res_list.append(item)
print(*res_list)