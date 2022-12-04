import givens
import pygame

given_list = []


def init_givens():
    # in 9 x 9 game board
    for i in range(9):
        for j in range(9):
            # make givens instance by their location
            locals()['given_',i,'_',j] = givens.Given(i,j,1)
            # convert the original coord to px coord in the window
            locals()['given_',i,'_',j].coord_convert(i,j,42.5)
            given_list.append(locals()['given_',i,'_',j])
            # terminal print
            # print(given_list)
            # locals()['given_',i,'_',j].toString()

def text_render(window, given):
    font = pygame.font.Font(None,50)
    if given.get_num() > 0:
        text_surface = font.render(format(given.get_num()), True, "BLACK")
        return window.blit(text_surface,(given.get_x(), given.get_y()))
    else:
        return
    
def test(given):
    print(type(given.get_num()))