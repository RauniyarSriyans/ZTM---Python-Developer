my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

my_list_2 = []

for item in my_list:
    if item in my_list_2:
        print(item)
    my_list_2.append(item)
