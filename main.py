from matrix_generation import *
img = cv2.imread("D:\\minesweeper\\minesweeper\\not_played.png")
upper = np.array([199, 199, 199])
lower = np.array([197, 197, 197])
mask = make_mask(upper, lower, img)
squares, numbers, num_index = find_squares(mask, [])
last_square, first_square = add_last_first_square(squares)
squares, numbers, num_index = find_squares(mask, [last_square, first_square])
height, width =get_height_width(squares)
row_width = get_row_width(squares)
col_width = len(squares) / row_width
sq_w_index = make_matrix_index(squares, col_width, row_width)
model = load_model()

print(sq_w_index)