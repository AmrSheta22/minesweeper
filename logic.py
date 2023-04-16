import numpy as np

def grid(height, width, bomb_density=.2):
    x= np.random.choice([0,1], size=(height, width), p=[1-bomb_density, bomb_density])
    return x

def check_around(grid, spot):
    upper_left = grid[spot[0]-1, spot[1]-1]
    upper = grid[spot[0]-1, spot[1]]
    upper_right = grid[spot[0]-1, spot[1]+1]
    left = grid[spot[0], spot[1]-1]
    right = grid[spot[0], spot[1]+1]
    lower_left = grid[spot[0]+1, spot[1]-1]
    lower = grid[spot[0]+1, spot[1]]
    lower_right = grid[spot[0]+1, spot[1]+1]
    return upper_left + upper + upper_right + left + right + lower_left + lower + lower_right

def is_it_edge(grid, spot):
    if spot[0] == 0:
        return (True, "top")
    elif spot[1] == 0:
        return (True, "left")
    elif spot[0]+1 == grid.shape[0]:
        return (True, "bottom")
    elif spot[1]+1 == grid.shape[1]:
        return (True, "right")
    else: 
        return (False, "not an edge")
    
def is_it_corner(grid, spot):
    if spot[0] ==0 and spot[1] == 0:
        return (True, "top left")
    elif spot[0]+1 == grid.shape[0] and spot[1] == 0:
        return (True, "bottom left")
    elif spot[0] == 0 and spot[1]+1 == grid.shape[1]:
        return (True, "top right")
    elif spot[0]+1 == grid.shape[0] and spot[1]+1 == grid.shape[1]:
        return (True, "bottom right")
    else: 
        return (False, "not a corner")    

def check_around_corner(grid, spot):
    if is_it_corner(grid, spot)[1] == "top left":
        right = grid[spot[0], spot[1]+1]
        lower = grid[spot[0]+1, spot[1]]
        lower_right = grid[spot[0]+1, spot[1]+1]
        return right + lower + lower_right
    elif is_it_corner(grid, spot)[1] == "bottom left":
        upper = grid[spot[0]-1, spot[1]]
        upper_right = grid[spot[0]-1, spot[1]+1]
        right = grid[spot[0], spot[1]+1]
        return upper + upper_right + right
    elif is_it_corner(grid, spot)[1] == "top right":
        left = grid[spot[0], spot[1]-1]
        lower_left = grid[spot[0]+1, spot[1]-1]
        lower = grid[spot[0]+1, spot[1]]
        return left + lower_left + lower
    else :
        upper_left = grid[spot[0]-1, spot[1]-1]
        upper = grid[spot[0]-1, spot[1]]
        left = grid[spot[0], spot[1]-1]
        return upper_left + upper + left

def check_around_edge(grid, spot):
    if is_it_edge(grid, spot)[1] == "top":
        left = grid[spot[0], spot[1]-1]
        right = grid[spot[0], spot[1]+1]
        lower_left = grid[spot[0]+1, spot[1]-1]
        lower = grid[spot[0]+1, spot[1]]
        lower_right = grid[spot[0]+1, spot[1]+1]
        return left + right + lower_left + lower + lower_right
    elif is_it_edge(grid, spot)[1] == "left":
        upper = grid[spot[0]-1, spot[1]]
        upper_right = grid[spot[0]-1, spot[1]+1]
        right = grid[spot[0], spot[1]+1]
        lower = grid[spot[0]+1, spot[1]]
        lower_right = grid[spot[0]+1, spot[1]+1]
        return upper + upper_right + right + lower + lower_right
    elif is_it_edge(grid, spot)[1] == "bottom":
        upper_left = grid[spot[0]-1, spot[1]-1]
        upper = grid[spot[0]-1, spot[1]]
        left = grid[spot[0], spot[1]-1]
        right = grid[spot[0], spot[1]+1]
        upper_right = grid[spot[0]-1, spot[1]+1]
        return upper_left + upper + left + right + upper_right
    else:
        upper_left = grid[spot[0]-1, spot[1]-1]
        upper = grid[spot[0]-1, spot[1]]
        lower = grid[spot[0]+1, spot[1]]
        left = grid[spot[0], spot[1]-1]
        lower_left = grid[spot[0]+1, spot[1]-1]
        return upper_left + upper + lower + left + lower_left     

def user_view_matrix(grid):
    x = np.zeros(grid.shape)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] == 1:
                x[i,j] = -1
            elif is_it_corner(grid, (i,j))[0]:
                x[i,j] = check_around_corner(grid, (i,j))
            elif is_it_edge(grid, (i,j))[0]:
                x[i,j] = check_around_edge(grid, (i,j))
            else:
                x[i,j] = check_around(grid, (i,j))
    return x
