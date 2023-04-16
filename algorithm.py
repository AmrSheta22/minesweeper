from game import *

# a function that takes the hidden grid and recursively find mines

def find_mines(hidden_grid, x, y):
    corr_mat = hidden_grid.copy()
    around = None
    if hidden_grid[x][y] == "0":
        if is_it_corner(hidden_grid, (x,y)):
            around = check_around_corner(hidden_grid, (x,y))
        elif is_it_edge(hidden_grid, (x,y)):
            around = check_around_edge(hidden_grid, (x,y))
        else:
            around = check_around(hidden_grid, (x,y))
        around = [i for i in around]
        for i in around:
            try:
                if int(i) :
                    continue
            except:
                break



main_grid = grid(10, 10, .10)
user_view = user_view_matrix(main_grid)
hidden_grid = make_hidden_grid(10, 10)
matrix_to_string(hidden_grid)
while True:
    x = input("Enter x coordinate: ")
    y = input("Enter y coordinate: ")
    if x == "q" or y == "q":
        break
    try:
        spot = (int(x), int(y))
    except:
        print("Enter a number")
        continue
    if int(x) > hidden_grid.shape[0] or int(y) > hidden_grid.shape[1]:
        print("Enter a number within the grid")
        continue
    mat = click(spot, user_view, hidden_grid)
    print(hidden_grid[int(x)][int(y)])
    #find_mines(hidden_grid, int(x), int(y))
    if type(mat) == str:
        print(mat)
        break
    matrix_to_string(mat)

