from game import *

# a function that takes the hidden grid and recursively find mines
COUNTED = []
MINES = []

def get_around_points(hidden_grid, x, y):
    if is_it_corner(hidden_grid, (x,y))[0]:

        around = check_around_corner(hidden_grid, (x,y))
        state = "corner"
    elif is_it_edge(hidden_grid, (x,y))[0]:
        around = check_around_edge(hidden_grid, (x,y))
        state = "edge"
    else:
        around = check_around(hidden_grid, (x,y))
        state = "normal"
    around = [i for i in around]
    corr_spots = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]
    # get the corresponding spots
    around_spot = []
    for i in corr_spots:
        if not ((i[0] < 0) or (i[0] > hidden_grid.shape[0]-1) or (i[1] < 0) or (i[1] > hidden_grid.shape[1]-1)):
            around_spot.append(i)
    return around, around_spot, state
def count_mines(around, around_spot):
    count = 0
    mines = []
    number_spots = []
    for index, i in enumerate(around):
        if i == "*":
            count += 1
            mines.append(around_spot[index])
        elif i.isdigit():
            number_spots.append(around_spot[index])
    return count, mines, number_spots
def count_known(around, around_spot):
    count = 0
    mines = []
    number_spots = []
    for index, i in enumerate(around):
        if i == "!":
            count += 1
            mines.append(around_spot[index])
        elif i.isdigit():
            number_spots.append(around_spot[index])
    return count, mines, number_spots
def find_mines(corr_mat, hidden_grid, x, y):
    around = None
    state = None
    if hidden_grid[x][y] == "0":
        around, around_spot, _ = get_around_points(hidden_grid, x, y)
        COUNTED.append((x,y))
        for i,k in enumerate(around):
            # check if corresponding spot is out of bounds
            if k.isdigit():
                if int(k) > 0:
                    around_k, around_spot_k, state = get_around_points(hidden_grid, around_spot[i][0], around_spot[i][1])
                    count, mine_spots, _ = count_mines(around_k, around_spot_k)
                    if count == int(k):
                        for i in mine_spots:
                            corr_mat[i[0]][i[1]] = "!"
                            MINES.append(i)
                else:
                    if (around_spot[i][0], around_spot[i][1]) not in COUNTED:
                        find_mines(corr_mat, hidden_grid, around_spot[i][0], around_spot[i][1])
                        COUNTED.append((around_spot[i][0], around_spot[i][1]))

def update_hidden_grid(hidden_grid):
    # add the mine spots in MINES to the hidden grid
    for i in MINES:
        hidden_grid[i[0]][i[1]] = "!"
    return hidden_grid

def auto_click(corr):
    for i_row, row in enumerate(corr):
        for i_col, n in enumerate(row):
            if  (n == "!") or (n == "*"):
                continue
            else:
                around, around_spot, state = get_around_points(corr, i_row, i_col)
                count, mine_spots, number_spots = count_known(around, around_spot)
                if count == int(n):
                    print(mine_spots)
                    print(number_spots)
                    click_spots = list(set(around_spot).difference(set(mine_spots)).difference(set(number_spots)))
                    print(click_spots)
                    for i in click_spots:
                        click(i, user_view, hidden_grid)





main_grid = grid(10, 10, .10)
user_view = user_view_matrix(main_grid)
hidden_grid = make_hidden_grid(10, 10)
matrix_to_string(hidden_grid)
z = 0
corr = make_hidden_grid(10, 10)
while True:
    x = input("Enter x coordinate: ")
    y = input("Enter y coordinate: ")
    if x == "q" or y == "q":
        break
    if x.isdigit() and y.isdigit():
        spot = (int(x), int(y))
    else:
        print("Enter a number")
        continue
    if int(x) > hidden_grid.shape[0] or int(y) > hidden_grid.shape[1]:
        print("Enter a number within the grid")
        continue
    if z == 0:
        mat = click(spot, user_view, hidden_grid)
        find_mines(corr, hidden_grid, spot[0], spot[1])
        hidden_grid = update_hidden_grid(hidden_grid)

    else:
        if type(mat) == str:
            print(mat)
            break
        else:
            hidden_grid = update_hidden_grid(hidden_grid)
            mat = auto_click(hidden_grid)
    print("\n\n\n")
    matrix_to_string(hidden_grid)
    z+=1

