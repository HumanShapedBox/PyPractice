import operations as o

def get_data():
    last_name = input('Введите фамилию: ').strip()
    first_name = input('Введите имя: ').strip()
    midle_name = input('Введите отчество: ').strip()
    phone_number = input('Введите номер: ').strip()
    return(last_name, first_name, midle_name, phone_number)

def get_operation_number():
    operation = input().strip()
    while operation not in ('1', '2', '3', '4', '5', '0'):
        print('Некорректный ввод. Попробуйте ещё раз: ')
        operation = input().strip()
    return operation

def perform_operation(operation_number):
    if operation_number == '1':
        o.print_book()
    elif operation_number == '2':
        o.add(get_data())
    elif operation_number == '3':
        print('\n'.join(o.find(input('Введите фамилию, имя, отчество или номер телефона: ').strip())))
    elif operation_number == '4':
        data = input('Введите фамилию, имя, отчество или телефон, которые нужно изменить: ')
        o.transformation(data)
    elif operation_number == '5':
        user = input('Введите фамилию, имя, отчество или телефон, чтобы удалить контакт: ')
        o.delete(user)
    else:
        print('Завершение работы')