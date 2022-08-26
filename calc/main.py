import module # импортируем модуль для работы с ним в главном файле

class Member:
    '''создали класс для обращения к: имени, фамилии и телефону'''
    def __init__(self, last_name=None, name=None, phone_number=None, from_line=None):
        if from_line==None: # если в строке пустота, то присваиваем параметрам переменные
            self.last_name = last_name
            self.name = name
            self.phone_number = phone_number
        else: # иначе кладем в параметры класса строку из файла
            self.last_name, self.name, self.phone_number = str(from_line).replace(" ", '').split("|")

    def input_charcters(self): # создали функцию для ввода данных в справочник
        self.last_name = input("Введите фамилию: ").capitalize()
        self.name = input("Введите имя: ").capitalize()
        self.pone_number = input("Введите номер телефона: ").capitalize()

    def __str__(self):
        return '{0:10} | {1:10} | {2}'.format(self.last_name, self.name, self.pone_number) + '\n'

class Contacts: # создали класс для и положили в него функцию, которая обрабатывет запрос 
    def find_member(self, query):
        with open('file.txt') as file: # открыли файл и далее обращаемся к нему через имя file
            for line in file: # проверяем значения строк в файле
                member = Member(from_line=line) # положили в переменную объекты класса, которые лежат в файле
                if (member.last_name, member.name) == query: # если значения строго равны запросу, то возвращаем искомое значение
                    return member
                

            
    def add_member(self): # создали функцию для добавления новых данных в справочник
        m = Member() # положили в переменную объекты класса
        m.input_charcters # записывает данные нового контакта с клавиатуры
        if c.find_member(query=(m.last_name, m.name)) is None: # если запрошенные данные отсутствуют 
            f = open('file.txt', 'a') # открываем файл для записи
            f.write('{0:10} | {1:10} | {2}'.format(m.last_name, m.name, m.phone_number) + '\n') # записываем в файл 
            print('\nКонтакт {lastName} {name} успешно добавлен\n'.format(lastName=m.last_name, name=m.name))
            f.close()
        else:
            print('Такой контакт уже есть')

    def delete_member(self, query): # создали функцию для удаления данных
        objects = []  # создали пустой список
        f = open('file.txt', 'r+') # открыли файл для чтения и записи
        for line in f.readlines(): # запустили цикл по строке файла 
            member = Member(from_line=line) # положили в переменную объкт класса мембер и передали туда строку из файла
            objects.append(member) # использовали функцию аппенд для заполнения строки
        for object in objects: # запустили цикл по списку
            if (object.last_name, object.name) != query: # если строка не соответствует запросу, то мы записываем её в файл, а то, что равно запросу - не записываем
                f.write(objects.__str__())

    def show_all_contacts(self):  # функция для вывода записной книжки
        with open('file.txt') as file:
            for line in file:
                member = Member(from_line=line)
                print(member)


c = Contacts() # создали объект класса контактс
while True:
    selector = module.choice()
    if selector == 1:
        query = (input('Для поиска контакта введите его фамилию: ').capitalize(),input('Для поиска контакта введите его имя ').capitalize()) 
        print(c.find_member(query))
    elif selector == 2:
        c.add_member()
    elif selector == 3:
        query = (input('Для удаления контакта введите его фамилию: ').capitalize,
        input('Для поиска контакта введите его имя: ').capitalize)
        c.delete_member(query)
    else:
        c.show_all_contacts()
    

    
