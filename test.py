import module

module.init_givens()

def abd_pos(pos):
    if 
    return

def overwrite(pos, input):
    name = 'given_' + str(pos[0]) + '_' + str(pos[1])
    for g in module.given_list:
        if g.name == name:
            g.num = input

def mousepos_to_boardpos(x, y):
    min_x = []
    min_y = []
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
    print(min_x.index(min(min_x)), min_y.index(min(min_y)))
    return (min_x.index(min(min_x)), min_y.index(min(min_y)))

overwrite(mousepos_to_boardpos(123,234),9)
for g in module.given_list:
    print(g)