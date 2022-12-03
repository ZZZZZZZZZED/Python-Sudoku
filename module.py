import givens



def init_givens():
    for i in range(9):
        for j in range(9):
            locals()['given_',i,'_',j] = givens.Given(i,j,0)
            locals()['given_',i,'_',j].toString()

def convert_to_window_coord():
    #the coord of 0,0 is 21px,13px. Gap = 42px
