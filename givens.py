class Given():
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
    def set_num(self, value):
        self.num = value
    def get_num(self):
        return self.num
    def toString(self):
        print((self.x, self.y),', value=',self.num)