import module

# given_list = []
module.init_givens()
pos = (123,321)
given_list = module.given_list
def mousepos_to_boardpos(pos):
    # covert mouse click pos to boardpos
    # by finding nearest y first, then finding nearest x

    min_x = []
    min_y = []
    for i in range(9):
        name = 'given_' + str(i) + '_' + str(0)
        print(name)
        for g in given_list:
            if g.name == name:

                # append distance to list, min is the nearest
                temp = abs(g.window_x - pos[0])
                min_x.append(temp)
    for j in range(9):
        name = 'given_' + str(0) + '_' + str(j)
        for g in given_list:
            if g.name == name:

                # append distance to list, min is the nearest
                temp = abs(g.window_y - pos[1])
                min_y.append(temp)
    
    # return nearest pos(x,y) for upcoming operation
    return (min_x.index(min(min_x)), min_y.index(min(min_y)))

print(mousepos_to_boardpos(pos))
