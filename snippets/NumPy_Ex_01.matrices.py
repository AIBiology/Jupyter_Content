# A 4X4 matrix with ones in every cell
ones = np.ones((4, 4))
print(ones, "\n\n")

# A 6X6 matrix with ones on the diagonal from top left to bottom right.
diag = np.eye(6)
print(diag, "\n\n")

# A 3X3X3 matrix with normally distributed random numbers with mean of 5 and standard deciavion of 2
cube = np.random.normal(5, 2, (3, 3, 3))
print(cube, "\n\n")

# A vector with 1,000,000 evenly spaced numbers between five and 10.
np.linspace(5, 10, 1000000)