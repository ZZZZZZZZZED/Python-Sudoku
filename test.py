import module

module.init_givens()

min_x = []
min_y = []

def input_value(x, y, input):
    name = 'given_' + str(x) + '_' + str(y)
    for g in module.given_list:
        if g.name == name:
            g.num = input

def mousepos_to_boardpos(x, y):

    for i in range(9):
        name = 'given_' + str(i) + '_' + str(0)
        for g in module.given_list:
            if g.name == name:
                temp = abs(g.window_x - x)
                min_x.append(temp)
    for j in range(9):
        name = 'given_' + str(0) + '_' + str(j)
        for g in module.given_list:
            if g.name == name:
                temp = abs(g.window_y - y)
                min_y.append(temp)
    return (min_x.index(min(min_x)), min_y.index(min(min_y)))

print(mousepos_to_boardpos(350,2))
