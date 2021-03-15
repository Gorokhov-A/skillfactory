class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

    def print_cat(self):
        print('Имя', self.name)
        print('Пол', self.sex)
        print('Возраст', self.age)