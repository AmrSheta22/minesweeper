from logic import *

# make a numpy array with all elements set to "*"
OPENED= []
def make_hidden_grid(height, width):
    grid = np.full((height, width), "*")
    return grid
def check_element(grid, spot):
    upper_left = grid[spot[0]-1, spot[1]-1]
    upper = grid[spot[0]-1, spot[1]]
    upper_right = grid[spot[0]-1, spot[1]+1]
    left = grid[spot[0], spot[1]-1]
    right = grid[spot[0], spot[1]+1]
    lower_left = grid[spot[0]+1, spot[1]-1]
    lower = grid[spot[0]+1, spot[1]]
    lower_right = grid[spot[0]+1, spot[1]+1]
    around = [(upper_left, (spot[0]-1, spot[1]-1)), (upper, (spot[0]-1, spot[1])), (upper_right, (spot[0]-1, spot[1]+1)), (left, (spot[0], spot[1]-1)), (right, (spot[0], spot[1]+1)), (lower_left, (spot[0]+1, spot[1]-1)), (lower, (spot[0]+1, spot[1])), (lower_right, (spot[0]+1, spot[1]+1))]  
    return around


def middle_click(spot, user_view, hidden_grid):
    hidden_grid[spot[0]-1, spot[1]-1] = str(user_view[spot[0]-1, spot[1]-1] )
    hidden_grid[spot[0]-1, spot[1]] = str(user_view[spot[0]-1, spot[1]])
    hidden_grid[spot[0]-1, spot[1]+1]= str(user_view[spot[0]-1, spot[1]+1])
    hidden_grid[spot[0], spot[1]-1] = str(user_view[spot[0], spot[1]-1] )
    hidden_grid[spot[0], spot[1]+1] = str(user_view[spot[0], spot[1]+1])
    hidden_grid[spot[0]+1, spot[1]-1] = str(user_view[spot[0]+1, spot[1]-1]) 
    hidden_grid[spot[0]+1, spot[1]] = str(user_view[spot[0]+1, spot[1]])
    hidden_grid[spot[0]+1, spot[1]+1] = str(user_view[spot[0]+1, spot[1]+1])
    return hidden_grid
def edge_click(spot, user_view, hidden_grid):
    if is_it_edge(user_view, spot)[1] == "top":
        hidden_grid[spot[0], spot[1]-1] = str(user_view[spot[0], spot[1]-1] )
        hidden_grid[spot[0], spot[1]+1] = str(user_view[spot[0], spot[1]+1])
        hidden_grid[spot[0]+1, spot[1]-1] = str(user_view[spot[0]+1, spot[1]-1]) 
        hidden_grid[spot[0]+1, spot[1]] = str(user_view[spot[0]+1, spot[1]])
        hidden_grid[spot[0]+1, spot[1]+1] = str(user_view[spot[0]+1, spot[1]+1])
    elif is_it_edge(user_view, spot)[1] == "bottom":
        hidden_grid[spot[0]-1, spot[1]-1] = str(user_view[spot[0]-1, spot[1]-1] )
        hidden_grid[spot[0]-1, spot[1]] = str(user_view[spot[0]-1, spot[1]])
        hidden_grid[spot[0]-1, spot[1]+1]= str(user_view[spot[0]-1, spot[1]+1])
        hidden_grid[spot[0], spot[1]-1] = str(user_view[spot[0], spot[1]-1] )
        hidden_grid[spot[0], spot[1]+1] = str(user_view[spot[0], spot[1]+1])
    elif is_it_edge(user_view, spot)[1] == "left":
        hidden_grid[spot[0]-1, spot[1]] = str(user_view[spot[0]-1, spot[1]])
        hidden_grid[spot[0]-1, spot[1]+1]= str(user_view[spot[0]-1, spot[1]+1])
        hidden_grid[spot[0], spot[1]+1] = str(user_view[spot[0], spot[1]+1])
        hidden_grid[spot[0]+1, spot[1]] = str(user_view[spot[0]+1, spot[1]])
        hidden_grid[spot[0]+1, spot[1]+1] = str(user_view[spot[0]+1, spot[1]+1])
    elif is_it_edge(user_view, spot)[1] == "right":
        hidden_grid[spot[0]-1, spot[1]-1] = str(user_view[spot[0]-1, spot[1]-1] )
        hidden_grid[spot[0]-1, spot[1]] = str(user_view[spot[0]-1, spot[1]])
        hidden_grid[spot[0], spot[1]-1] = str(user_view[spot[0], spot[1]-1] )
        hidden_grid[spot[0]+1, spot[1]-1] = str(user_view[spot[0]+1, spot[1]-1]) 
        hidden_grid[spot[0]+1, spot[1]] = str(user_view[spot[0]+1, spot[1]])
    return hidden_grid


def corner_click(spot, user_view, hidden_grid):
    if is_it_corner(user_view, spot)[1] == "top left":
        hidden_grid[spot[0], spot[1]+1] = str(user_view[spot[0], spot[1]+1])
        hidden_grid[spot[0]+1, spot[1]] = str(user_view[spot[0]+1, spot[1]])
        hidden_grid[spot[0]+1, spot[1]+1] = str(user_view[spot[0]+1, spot[1]+1])
    elif is_it_corner(user_view, spot)[1] == "top right":
        hidden_grid[spot[0], spot[1]-1] = str(user_view[spot[0], spot[1]-1] )
        hidden_grid[spot[0]+1, spot[1]-1] = str(user_view[spot[0]+1, spot[1]-1]) 
        hidden_grid[spot[0]+1, spot[1]] = str(user_view[spot[0]+1, spot[1]])
    elif is_it_corner(user_view, spot)[1] == "bottom left":
        hidden_grid[spot[0]-1, spot[1]] = str(user_view[spot[0]-1, spot[1]])
        hidden_grid[spot[0]-1, spot[1]+1]= str(user_view[spot[0]-1, spot[1]+1])
        hidden_grid[spot[0], spot[1]+1] = str(user_view[spot[0], spot[1]+1])
    elif is_it_corner(user_view, spot)[1] == "bottom right":
        hidden_grid[spot[0]-1, spot[1]-1] = str(user_view[spot[0]-1, spot[1]-1] )
        hidden_grid[spot[0]-1, spot[1]] = str(user_view[spot[0]-1, spot[1]])
        hidden_grid[spot[0], spot[1]-1] = str(user_view[spot[0], spot[1]-1] )
    return hidden_grid

def around_edge(user_view, spot):
    around = []
    if is_it_edge(user_view, spot)[1] == "top":
        around.append((user_view[spot[0], spot[1]-1], (spot[0], spot[1]-1)))
        around.append((user_view[spot[0], spot[1]+1], (spot[0], spot[1]+1)))
        around.append((user_view[spot[0]+1, spot[1]-1], (spot[0]+1, spot[1]-1)))
        around.append((user_view[spot[0]+1, spot[1]], (spot[0]+1, spot[1])))
        around.append((user_view[spot[0]+1, spot[1]+1], (spot[0]+1, spot[1]+1)))
    elif is_it_edge(user_view, spot)[1] == "bottom":
        around.append((user_view[spot[0]-1, spot[1]-1], (spot[0]-1, spot[1]-1)))
        around.append((user_view[spot[0]-1, spot[1]], (spot[0]-1, spot[1])))
        around.append((user_view[spot[0]-1, spot[1]+1], (spot[0]-1, spot[1]+1)))
        around.append((user_view[spot[0], spot[1]-1], (spot[0], spot[1]-1)))
        around.append((user_view[spot[0], spot[1]+1], (spot[0], spot[1]+1)))
    elif is_it_edge(user_view, spot)[1] == "left":
        around.append((user_view[spot[0]-1, spot[1]], (spot[0]-1, spot[1])))
        around.append((user_view[spot[0]-1, spot[1]+1], (spot[0]-1, spot[1]+1)))
        around.append((user_view[spot[0], spot[1]+1], (spot[0], spot[1]+1)))
        around.append((user_view[spot[0]+1, spot[1]], (spot[0]+1, spot[1])))
        around.append((user_view[spot[0]+1, spot[1]+1], (spot[0]+1, spot[1]+1)))
    elif is_it_edge(user_view, spot)[1] == "right":
        around.append((user_view[spot[0]-1, spot[1]-1], (spot[0]-1, spot[1]-1)))
        around.append((user_view[spot[0]-1, spot[1]], (spot[0]-1, spot[1])))
        around.append((user_view[spot[0], spot[1]-1], (spot[0], spot[1]-1)))
        around.append((user_view[spot[0]+1, spot[1]-1], (spot[0]+1, spot[1]-1)))
        around.append((user_view[spot[0]+1, spot[1]], (spot[0]+1, spot[1])))
    return around

def around_corner(user_view, spot):
    around = []
    if is_it_corner(user_view, spot)[1] == "top left":
        around.append((user_view[spot[0], spot[1]+1], (spot[0], spot[1]+1)))
        around.append((user_view[spot[0]+1, spot[1]], (spot[0]+1, spot[1])))
        around.append((user_view[spot[0]+1, spot[1]+1], (spot[0]+1, spot[1]+1)))
    elif is_it_corner(user_view, spot)[1] == "top right":
        around.append((user_view[spot[0], spot[1]-1], (spot[0], spot[1]-1)))
        around.append((user_view[spot[0]+1, spot[1]-1], (spot[0]+1, spot[1]-1)))
        around.append((user_view[spot[0]+1, spot[1]], (spot[0]+1, spot[1])))
    elif is_it_corner(user_view, spot)[1] == "bottom left":
        around.append((user_view[spot[0]-1, spot[1]], (spot[0]-1, spot[1])))
        around.append((user_view[spot[0]-1, spot[1]+1], (spot[0]-1, spot[1]+1)))
        around.append((user_view[spot[0], spot[1]+1], (spot[0], spot[1]+1)))
    elif is_it_corner(user_view, spot)[1] == "bottom right":
        around.append((user_view[spot[0]-1, spot[1]-1], (spot[0]-1, spot[1]-1)))
        around.append((user_view[spot[0]-1, spot[1]], (spot[0]-1, spot[1])))
        around.append((user_view[spot[0], spot[1]-1], (spot[0], spot[1]-1)))
    return around

def click(spot, user_view, hidden_grid):
    if user_view[spot[0], spot[1]] == 0:
        hidden_grid[spot[0], spot[1]] = "0"
        OPENED.append(spot)
        if is_it_corner(user_view, spot)[0]:
            around = around_corner(user_view, spot)
            hidden_grid = corner_click(spot, user_view, hidden_grid)
        elif is_it_edge(user_view, spot)[0]:
            around = around_edge(user_view, spot)
            hidden_grid = edge_click(spot, user_view, hidden_grid)
        else:
            hidden_grid = middle_click(spot, user_view, hidden_grid)
            around = check_element(user_view, spot)
        for i in around:
            if i[0] != 0 and i[1] not in OPENED:
                OPENED.append(i[1])
        for i in around:
            if i[0] == 0 and i[1] not in OPENED:
                OPENED.append(i[1])
                click(i[1], user_view, hidden_grid)
        return hidden_grid
    elif user_view[spot[0], spot[1]] == -1:
        return "You lost"
    else:
        hidden_grid[spot[0], spot[1]] = str(user_view[spot[0], spot[1]])
        OPENED.append(spot)
    return hidden_grid

# main_grid = grid(10, 10, .16)
# user_view = user_view_matrix(main_grid)
# hidden_grid = make_hidden_grid(10, 10)
# print("   0   1   2   3   4   5   6   7   8   9")
# print(hidden_grid)
# while True:
#     x = input("Enter x coordinate: ")
#     y = input("Enter y coordinate: ")
#     try:
#         spot = (int(x), int(y))
#     except:
#         print("Enter a number")
#         continue
#     if x == "q" or y == "q":
#         break
#     if int(x) > hidden_grid.shape[0] or int(y) > hidden_grid.shape[1]:
#         print("Enter a number within the grid")
#         continue
#     print("   0   1   2   3   4   5   6   7   8   9")
#     print(click(spot, user_view, hidden_grid))


