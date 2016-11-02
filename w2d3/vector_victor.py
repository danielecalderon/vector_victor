import matplotlib.pyplot as plt




# Implement these linear algebra functions:
#
# vector shape in shape()
def draw_vector(x, y, start_x=0, start_y=0, **kwargs):
    args = dict(head_width=0.15, head_length=0.3,
                overhang=0.5, length_includes_head=True)
    args.update(kwargs)
    plt.arrow(start_x, start_y, start_x + x, start_y + y, **args)

plt.figure(figsize=(7, 7))

draw_vector(5, 0, color="blue")
draw_vector(3, 4, color="red")

plt.grid(True)
plt.axis([-1, 7, -1, 7])

plt.text(2.5, 0.3, r"$v = \left[\stackrel{5}{0}\right]$", fontsize=20)
plt.text(1.5, 2.3, r"$w = \left[\stackrel{3}{4}\right]$", fontsize=20)
plt.show()



#
# vector addition in vector_add()
#
# vector subtraction in vector_sub()
#
# vector sum in vector_sum()
#
# dot product in dot()
#
# vector multiplication by a scalar in vector_multiply()
#
# mean of multiple vectors in vector_mean()
#
# magnitude in magnitude()












# Advanced Mode (optional)
#
# Implement these additional linear algebra functions:
#
# matrix and vector shape in shape()
# matrix row in matrix_row()
# matrix column in matrix_col()
# matrix addition in matrix_add()
# matrix subtraction in matrix_sub()
# matrix multiplication by a scalar in matrix_scalar_multiply()
# matrix multiplication by a vector in matrix_vector_multiply()
# matrix multiplication by a matrix in matrix_matrix_multiply()
# These functions must:
#
# Check the shape of the incoming vector or matrix before any calculations.
# Refactor any duplicated code in to reused functions.
# Pass all of their corresponding unit tests.
