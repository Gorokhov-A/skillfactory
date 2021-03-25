# Морской бой ( Задание С 2.5 )

from random import randint

class Dots:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x} {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:

    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dots(cur_x, cur_y))

        return ship_dots

    def hit(self, shoot):
        return shoot in self.dots

class Board:

    def __init__(self, hide=False, size = 6):
        self.hide = hide
        self.size = size
        self.field = [['O'] * size for _ in range(size)]
        self.count = 0
        self.busy = []
        self.ship = []

    def add_ship(self, ship):

        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipPlanting()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ship.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dots(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def __str__(self):
        res = ""
        res += "      1  |  2  |  3  |  4  |  5  |  6  |"
        for i, row in enumerate(self.field):
            res += f'\n{i+1}  |  ' + '  |  '.join(row) + "  |  "

        if self.hide:
            res = res.replace("■", "O")
        return res

    def shot(self, d):
        if self.out(d):
            raise BoardOutOfRange()

        if d in self.busy:
            raise BoardUsedDot()

        self.busy.append(d)

        for ship in self.ship:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy
    def ask(self):
        return NotImplementedError()
    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except Boardexception as e:
                print(e)

class AI(Player):
    def ask(self):
        d = Dots(randint(0,5), randint(0,5))
        print(f'Ход компьютера: {d.x +1} {d.y +1}')
        return d

class Human(Player):
    def ask(self):
        while True:
            coords = input("Введите координаты: ").split()
            if len(coords) != 2:
                print("Введите 2 координаты !")
                continue
            x, y = coords
            if not (x.isdigit()) and not (y.isdigit()):
                print("Ошибка ввода !")
                continue
            x, y = int(x), int(y)
            return Dots(x-1, y-1)

class Boardexception(Exception):
    pass

class BoardOutOfRange(Boardexception):
    def __str__(self):
        return("Выстрел  за пределами игрового поля! ")

class BoardUsedDot(Boardexception):
    def __str__(self):
        return("Попытка повторного выстрела в эту точку!")

class BoardWrongShipPlanting(Boardexception):
    pass


class Game():

    def __init__(self, size = 6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hide = True

        self.ai = AI(co, pl)
        self.hu = Human(pl, co)


    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        len = [3, 2, 2, 1, 1, 1]
        board = Board(size = self.size)
        attempts = 0
        for l in len:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dots(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))

                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipPlanting:
                    pass

        board.begin()
        return board



    def greet(self):
        print("-------------------")
        print("    Морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")




    def loop(self):
        num = 0
        while True:
            print("-" * 10)
            print("Игровое поле человека !")
            print(self.hu.board)
            print("-" * 10)
            print("Игровое поле компьютера !")
            print(self.ai.board)
            if num % 2 == 0:
                print("-" * 10)
                print("Человек, твой ход!")
                repeat = self.hu.move()
            else:
                print("-" * 10)
                print("Ходит компьютер!")
                repeat = self.ai.move()

            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 10)
                print("Победил компьютер!")
                break

            if self.hu.board.count == 7:
                print("-" * 10)
                print("Человек победил!")
                break

            num += 1

    def start(self):

        self.greet()

        self.loop()


g = Game()
g.start()