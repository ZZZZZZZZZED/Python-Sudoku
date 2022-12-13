class Given():
    def __init__(self, x, y, num, name):
        self.x = x
        self.y = y
        self.num = num
        self.name = name
        self.window_x = 0
        self.window_y = 0
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def set_num(self, value):
        self.num = value
    def get_num(self):
        return self.num
    def df_get_num(self, df):
        
        return
    def __str__(self):
        return "Name: {}, located({}, {}), window_coord({}, {}), num={}".format(self.name, self.x, self.y, self.window_x, self.window_y, self.num)
        # (self.x, self.y),', value=',self.num

    def coord_convert(self, to_x, to_y, gap):
        #starts at px(21,13), make the px location spread on the game board
        self.window_x = 21 + (gap * to_x)
        self.window_y = 13 + (gap * to_y)
