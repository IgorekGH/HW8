# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 4. Выход по требованию пользователя
# 5. Дополнить телефонный справочник возможностью изменения и удаления данных.

def all_contact():
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            print(line)

def find_contact(name):
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            if name in line:
                print(line)
                
def add_contact(new_contact):
    with open('phone_number.txt', 'a', encoding='utf8') as data:
        data.write('\n')
        data.write(new_contact)

def delete_contact(name):
    with open('phone_number.txt', 'r', encoding='utf8') as data:
        for line in data:
            if name in line:
                print(line)
           


def main_menu(numb):
    if numb == 1:
        all_contact()
    elif numb == 2:
        name = input('Введите искомое имя: ')
        find_contact(name)
    elif numb == 3:
        data = input('Введите новый контакт: ')
        add_contact(data)
while True:
    numb = int(input('Введите' 
        ' 1 - для печати всего справочника ;'
        ' 2 - для поиска контакта ;' 
        ' 3 - для записи контакта ;' 
        ' 4 - для выхода из программы ;' 
        ' 5 - для удаления данных: '))
    if numb == 4:
        break
    elif numb == 5:
        name = input('Введите данные которые хотите удалить: ')
        del(name)
    main_menu(numb)
    



    # def delete(contacts):
    # print("Введите контакт: ")
    # name = input('> ')
    # for contact in contacts:
    #     if contact['name'] == name:
    #         print("Вы хотите удалить контакт %s (yes/no)?: " % name )
    #         name_del = input('> ')
    #         if name_del == 'yes':
    #            contacts.remove(contact)
    #            print("Вы удалили контакт %s " % name)