documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_people(documents,document_number='10006'):

    name = ''
    for document in documents:
        if document_number == document['number']:
            name = document['name']
            break
        else:
            name = 'Номер документа введен неверно или не существует'
    return name

def get_shelf(directories, shelf='Номер документа введен неверно или не существует'):
    document_number = input('Введите номер документа: ')
    for key, document in directories.items():
        for number in document:
            if document_number == number:
                shelf = key
    return shelf


def get_document_list(documents):
    for people in documents:
        print('  '.join(people.values()))


def add_document():
    info = {}
    info['type'] = '1'
    info['number'] = '2'
    info['name'] = '3'
    documents.append(info)

    def add_namber_in_directories():
        direct = '3'

        if direct not in directories.keys():
            print('Такой полки не существует. Повторите ввод')
            print()
            add_namber_in_directories()
        else:
            for shelf, value in directories.items():
                if shelf == direct:
                    directories.setdefault(shelf,value.append(info['number']))
                break

    add_namber_in_directories()
    return len(documents)

#main()
