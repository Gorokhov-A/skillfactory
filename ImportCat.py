from cats_house import Cat

cats = [Cat(name='Барон', sex='мальчик', age='2 года'),
        Cat(name='Сэм', sex='мальчик', age='2 года')]

for pet in cats:
    pet.print_cat()