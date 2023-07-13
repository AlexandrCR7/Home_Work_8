def input_number():
    ask = int(input('Выберите действие:\n'
                    '9 - Прекратить запись\n'
                    '1 - Записать нового пользователя:\n'
                    '2 - Найти пользователя по элементу:\n'
                    '3 - Показать весь справочник: \n'
                    '4 - Внести изменения в справочник:\n'
                    '5 - Удалить строку:\n'))
    return ask


def input_del_number():
    ask_1 = int(input('Выберите способ изменения контакта:\n'
                      '0. Вернуться в основное меню\n'
                      '1. Изменение по номеру строки.\n'
                      '2. Изменение по элементу.\n'))
    return ask_1


def input_name():
    id = input('Введите id: ')
    name = input('Введите ФИО: ')
    tel = input('Введите телефон: ')
    data_name = id + ' ' + name + ' ' + tel
    return data_name


def input_element():
    element = input('Введите элемент для поиска: ')
    return element


def search_id():
    element = int(input('Введите номер строки, которую хотите поменять: '))
    return element


def del_id():
    element = int(input('Введите номер строки, которую хотите удалить: '))
    return element
