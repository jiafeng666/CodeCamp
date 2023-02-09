class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, wid):
        self.width = wid

    def set_height(self, hei):
        self.height = hei

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        shape = ''
        for i in range(self.height):
            shape += '*' * self.width + '\n'
        return shape

    def get_amount_inside(self, tan):
        return self.width * self.height // tan.get_area()


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, sid):
        self.side = sid
        super().set_width(sid)
        super().set_height(sid)

    def set_width(self, wid):
        self.side = wid

    def set_height(self, hei):
        self.side = hei


if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
