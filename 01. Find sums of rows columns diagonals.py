n = int(input("Enter the no. of rows/columns in which elements are to be stored: "))
list2D = [[int(input(f"Enter number #({i+1}, {j+1}): ")) for j in range(n)] for i in range(n)] 

row_sums = [sum(list2D[i]) for i in range(n)]
col_sums = [sum(column) for column in zip(*list2D)]
first_diag= [list2D[i][i] for i in range(n)]
second_diag= [list2D[i][n-i-1] for i in range(n)]

print("\n".join(f"\nSum of row #{i+1}: {row_sums[i]}\nSum of column #{i+1}: {col_sums[i]}" for i in range(n)),
	"\n\nSum of the first diagonal of the array: ", sum(first_diag),
	"\nSum of the second diagonal of the array: ", sum(second_diag),
	"\n\nSum of all elements of the array: ", sum(row_sums))