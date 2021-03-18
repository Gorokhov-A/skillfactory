class Users:

    def __init__(self, name, surname, city, status):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    def get_name(self):
        return (self.name)

    def get_surname(self):
        return (self.surname)

    def get_city(self):
        return (self.city)

    def get_status(self):
        return (self.status)

class Guest(Users):

    def __init__(self, name='', surname='', city='', status=''):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status


Ivan_Petrov = Guest(name='Иван', surname='Петров', city='Москва', status='Наставник')

print(f' {Ivan_Petrov.name} {Ivan_Petrov.surname}, г.{Ivan_Petrov.city}, статус"{Ivan_Petrov.status}"')