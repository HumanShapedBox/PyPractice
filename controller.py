import operations as o
from datetime import date

def get_data():
    title = input('Введите название заметки: ').strip()
    body = input('Напишите что-нибудь: ').strip()
    #current_date = date
    return(title, body)#, current_date)

def get_operation_number():
    operation = input().strip()
    while operation not in ('1', '2', '3', '4', '5', '0'):
        print('Некорректный ввод. Попробуйте ещё раз: ')
        operation = input().strip()
    return operation

def perform_operation(operation_number):
    if operation_number == '1':
        o.print_notes()
    elif operation_number == '2':
        o.add(get_data())
    elif operation_number == '3':
        print('\n'.join(o.find(input('Введите название заметки: ').strip())))
    elif operation_number == '4':
        data = input('Введите название заметки, которую хотите отредактировать: ')
        o.transformation(data)
    elif operation_number == '5':
        user = input('Введите название заметки, которую требуется удалить: ')
        o.delete(user)
    else:
        print('Завершение работы')