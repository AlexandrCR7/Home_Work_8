def write_name(name):
    with open('tel.txt', 'a', encoding='utf-8') as file:
        file.write(name)


def read_element(ele):
    with open('tel.txt', 'r', encoding='utf-8') as file:
        for i in file.readlines():
            if ele in i:
                print(i)


def show_elements():
    with open('tel.txt', 'r', encoding='utf-8') as file:
        for i in file.readlines():
            print(i)


def change_string(arg_2, arg_1):
    with open('tel.txt', 'r', encoding='utf-8') as file:
        old_data = file.read().split('\n')
        old_data[arg_2 - 1] = arg_1
    with open('tel.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(old_data))


def change_string_22(arg, arg_1):
    with open('tel.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        for j in range(len(lst)):
            if arg in lst[j]:
                lst[j] = arg_1 + '\n'
    with open('tel.txt', 'w', encoding='utf-8') as file:
        for row in lst:
            file.write(row)


def del_string(arg_1):
    with open('tel.txt', 'r', encoding='utf-8') as file:
        old_data = file.read().split('\n')
        old_data.pop(arg_1 - 1)
    with open('tel.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(old_data))

def del_string_22(arg):
    with open('tel.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        for j in range(len(lst)):
            if arg in lst[j]:
                lst.remove(lst[j])
    with open('tel.txt', 'w', encoding='utf-8') as file:
        for row in lst:
            file.write(row)


def add_number_id():
    j = 1
    with open('tel.txt', 'r', encoding='utf-8') as file:
        for i in file.readlines():
            print(f'#{j} - {i}')
            j += 1
