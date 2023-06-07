import controller as c

def print_notes():
    notes = open('Notes.csv', 'r')
    print(notes.read())
    notes.close()

def find(name):
    notes = open('Notes.csv', 'r')
    find_list = list()
    for line in notes:
        if name in line.split():
            find_list.append(line)
    notes.close()
    return find_list

def add(data):
    notes = open('Notes.csv', 'a')
    notes.write(' '.join(data) + '\n')
    notes.close()

def transformation(data):
    notes = open('Notes.csv', 'a')
    new_data = input('Введите актуальные данные: ')
    if c.data in notes:
        return notes.replace(data, new_data)
    notes.close()

def delete(name):
    notes = open('Notes.csv', 'a')
    data = notes.readlines()
    data = filter(lambda line: name not in line, data)
    notes.close()