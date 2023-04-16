import cv2
import numpy as np
import os
import pickle
import warnings
warnings.filterwarnings("ignore")
knn = pickle.load(open("knn_model.pkl", "rb"))
# read the image Untitled.png

img = cv2.imread("D:\\minesweeper\\minesweeper\\not_played.png")

# display the image
# get a mask between grey and black

def load_model():
    knn = pickle.load(open("knn_model.pkl", "rb"))
    return knn
def make_mask(up, low, img):
    mask = cv2.inRange(img, low, up)
    return mask
# a function that looks for squares
def find_squares(mask, last_square):
    # find the contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # find the squares
    squares = []
    numbers = []
    num_index = []

    hierarch= []
    count = 0
    if len(last_square) != 0:
        count+=1
        squares.append(last_square[1])
    for contour, h in zip(contours, hierarchy[0]):
        # approximate the contour
        epsilon = 0
        approx = cv2.approxPolyDP(contour, epsilon, True)
        # if the contour is a square
        if len(approx) == 4  and h[0] != -1  and h[1] != -1  and h[3]!= -1 :  
            # add the square to the list
            squares.append(approx)
            hierarch.append(h)
            if h[2] != -1:
                numbers.append(approx)
                num_index.append(count)
            else:
                numbers.append(0)
            count+=1
    if len(last_square) != 0:
        count+=1
        squares.append(last_square[0])

    return squares, numbers, num_index

# know how many squares there are in height and width
def get_height_width(squares):
    # sort the squares by their y value
    squares = sorted(squares, key=lambda x: x[0][0][1], reverse=True)
    
    # get the squares that are in the first row
    first_row = []
    for square in squares:
        if square[0][0][1] == squares[0][0][0][1]:
            first_row.append(square)
        else:
            break
    # get the squares that are in the first column
    squares = sorted(squares, key=lambda x: x[0][0][0], reverse=True)
    first_column = []
    for square in squares:
        if square[0][0][0] == squares[0][0][0][0]:
            first_column.append(square)
        else:
            break
    # return the height and width
    return len(first_row), len(first_column)

# get the axis where the numbers are from their index in the num_index list
def get_axis(i, height, width):
    # get the row and column of the number from its index
    row = i // width
    column = i % width
    # return the axis
    return (row, column)




# add last square to the list
# get min height 
def add_last_first_square(squares):
    squares = sorted(squares, key=lambda x: x[0][0][1])
    min_height = squares[0][0][0][1]
    squares = sorted(squares, key=lambda x: x[0][0][0])
    min_width = squares[0][0][0][0]
    # make a new square with the min height and width
    # height of square 1 
    squares[0][0][0][0]

    width = (squares[0][2][0][0] - squares[0][0][0][0])
    last_square = np.array([[[min_width, min_height], 
                            [min_width, min_height+width], 
                            [min_width+width, min_height+width], 
                            [min_width+width, min_height]]])
    # now make a square with the max height and width
    squares = sorted(squares, key=lambda x: x[0][0][1], reverse=True)
    max_height = squares[0][0][0][1]
    squares = sorted(squares, key=lambda x: x[0][0][0], reverse=True)
    max_width = squares[0][0][0][0]
    # height of square 2
    width = (squares[0][2][0][0] - squares[0][0][0][0])
    last_square2 = np.array([[[max_width, max_height],
                            [max_width, max_height+width],
                            [max_width+width, max_height+width],
                            [max_width+width, max_height]]])
    return last_square, last_square2

# a function that ca;lculates the number of squares in each row
def get_row_width(squares):
    # sort the squares by their y value
    squares = sorted(squares, key=lambda x: x[0][0][1], reverse=True)
    # get the squares that are in the first row
    first_row = []
    for square in squares:
        if square[0][0][1] == squares[0][0][0][1]:
            first_row.append(square)
        else:
            break
    return len(first_row)

def make_matrix_index(squares, col_width, row_width):
    # sort the squares by their y value
    sq_w_index = {}
    for i, square in reversed(list(enumerate(squares))):
        sq_w_index[get_axis(i, col_width, row_width)] = squares[-i-1]
    return sq_w_index
# for number in numbers:
#     preds.append(knn.predict([cv2.resize(mask[number[0][0][1]:number[2][0][1], number[0][0][0]:number[2][0][0]], (27,27)).flatten()])[0])
# write each prediction on top of the square it is in
# for i, square in enumerate(numbers):
#     cv2.putText(img, str(preds[i]), (square[0][0][0], square[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0), 2)
# cv2.imwrite("D:\\minesweeper\\minesweeper\\finished.png", img)





































# count = 0

# for i, square in enumerate(squares):
#     #mask[294:980, 588:1613]
#     if 0  in mask[square[0][0][1]:square[2][0][1], square[0][0][0]:square[2][0][0]].flatten():
#         count+=1
#         print(count)
#         if count == 32:
#             cv2.imwrite("data/img{}.png".format(i), mask[square[0][0][1]:square[2][0][1], square[0][0][0]:square[2][0][0]])
#             # write the number to a file
#             with open("data/labels.txt", "a") as f:

    #     squares.pop(i)
# filter out the squares that contain a numpip install number-recognition




# for square in squares:
#     print(square)

# cv2.drawContours(img, squares, -1, (122, 255, 0), 3)
# cv2.imwrite("D:\\minesweeper\\minesweeper\\Untitled3.png", img)
# search for a square that is filled in
# for i, square in enumerate(squares):
    #mask[294:980, 588:1613]
    # if 0 in mask[square[0][0][1]:square[2][0][1], square[0][0][0]:square[2][0][0]].flatten():
    #     squares.pop(i)
# save image
# print(squares[2])
# cv2.drawContours(img, squares, -1, (122, 255, 0), 3)
# cv2.imwrite("D:\\minesweeper\\minesweeper\\Untitled2.png", img)