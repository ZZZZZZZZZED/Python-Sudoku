class Given():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def set_num(self, value):
        self.num = value
    def get_num(self):
        return self.num
    def __str__(self):
        print((self.x, self.y),', value=',self.num)
    def coord_convert(self, to_x, to_y, gap):
        #starts at px(21,13), make the px location spread on the game board
        x = 21 + (gap * to_x)
        y = 13 + (gap * to_y)
        self.set_x(x)
        self.set_y(y)