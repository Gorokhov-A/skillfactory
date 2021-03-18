class Users:
    def __init__(self, name='', surname='', balance=0):
        self.name = name
        self.surname = surname
        self.balance = balance

    def get_data(self, name):
        return self.name

    def get_name(self, surname):
        return self.surname

    def get_balance(self, balance):
        return self.balance

Ivan_Petrov = Users(name='Иван', surname='Петров', balance=50)

print(f'Клиент "{Ivan_Petrov.name} {Ivan_Petrov.surname}". Баланс: {Ivan_Petrov.balance}" руб.')