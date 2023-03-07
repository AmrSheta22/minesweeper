import cv2
import numpy as np
import os
import pickle
import warnings
warnings.filterwarnings("ignore")
knn = pickle.load(open("knn_model.pkl", "rb"))
# read the image Untitled.png

img = cv2.imread("D:\\minesweeper\\minesweeper\\Untitled.png")

# display the image
# get a mask between grey and black
upper = np.array([199, 199, 199])
lower = np.array([197, 197, 197])
mask = cv2.inRange(img, lower, upper)

cv2.imwrite("mask.png", mask)
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
        squares.append(last_square)
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
    
    return squares, numbers, num_index
# find the squares
squares, numbers, num_index = find_squares(mask, [])


print(squares[0])
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
def get_axis(num_index, width):
    axis = (num_index % width, num_index // width)
    return axis



# add last square to the list
# get min height 
def add_last_square(squares):
    squares = sorted(squares, key=lambda x: x[0][0][1])
    min_height = squares[0][0][0][1]
    squares = sorted(squares, key=lambda x: x[0][0][0])
    min_width = squares[0][0][0][0]
    # make a new square with the min height and width
    # height of square 1 
    squares[0][0][0][1]

    width = (squares[0][2][0][0] - squares[0][0][0][0])
    last_square = np.array([[[min_width, min_height], 
                            [min_width, min_height+width], 
                            [min_width+width, min_height+width], 
                            [min_width+width, min_height]]])
    return last_square

last_square = add_last_square(squares)
cv2.drawContours(img, squares, -1, (122, 255, 0), 3)
#cv2.drawContours(img, numbers, -1, (219, 255, 23), 3)
cv2.imwrite("D:\\minesweeper\\minesweeper\\Untitled4.png", img)



# preds = []
# for number in numbers:
#     preds.append(knn.predict([cv2.resize(mask[number[0][0][1]:number[2][0][1], number[0][0][0]:number[2][0][0]], (27,27)).flatten()])[0])
# write each prediction on top of the square it is in
# for i, square in enumerate(numbers):
#     cv2.putText(img, str(preds[i]), (square[0][0][0], square[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0), 2)
# cv2.imwrite("D:\\minesweeper\\minesweeper\\finished.png", img)

from game import make_hidden_grid
squares, numbers, num_index = find_squares(mask, last_square)
height, width =get_height_width(squares)
# sort numbers depending on the square list y value
# numbers = [x for _, x in sorted(zip(squares, numbers), key=lambda pair: pair[0][0][0][1], reverse=True)]

for i, number in enumerate(numbers):
    if type(number) != int:
        print(i)
        print(get_axis(i, width))
# for i, square in enumerate(numbers):
#     if type(square) != int:
#         cv2.putText(img, str(i), (square[0][0][0], square[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0), 2)
for i, square in enumerate(squares):
    cv2.putText(img, str(i), (square[0][0][0], square[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0), 2)
cv2.imwrite("D:\\minesweeper\\minesweeper\\finished.png", img)


# for i in num_index:
#     actual_index = i-2
#     print(actual_index)
#     print(get_axis(actual_index, width))

hidden_grid =make_hidden_grid(width,height)


































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