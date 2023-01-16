# import view
import module
from itertools import zip_longest
module.init_givens()

x_list = []
y_list = []
num = 5
x = 1
y = 6
if 'given_1_0' in globals():
    print(globals()['given_1_0'])
# print(given_1_0)
for i in range(9):
    x_list.append((x, i))
    y_list.append((i, y))
for x, y in zip(x_list, y_list):
        name = 'given_' + str(x[0]) + '_' + str(x[1])
        for g in module.given_list:
            if g.name == name and g.num > 0:
                if g.num == num:
                    print("x fail")

        name = 'given_' + str(y[0]) + '_' + str(y[1])
        for g in module.given_list:
            if g.name == name and g.num > 0:
                if g.num == num:
                    print("y fail")

