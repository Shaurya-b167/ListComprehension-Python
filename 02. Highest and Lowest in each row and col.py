print("Enter the dimensions of the 2-D list:")
r = int(input("Enter the no. of rows: "))
c = int(input("Enter the no. of columns: "))
list2D = [[int(input(f"Enter number #({i+1}, {j+1}): ")) for j in range(c)] for i in range(r)] 

max_rows = [max(list2D[i]) for i in range(r)]
min_rows = [min(list2D[i]) for i in range(r)]
max_cols = [max(column) for column in zip(*list2D)]
min_cols = [min(column) for column in zip(*list2D)]

print("\n".join([f"\nRow #{i+1}:" +
	f"\nHighest element is {max_rows[i]} occurs at location ({i+1}, {max_rows.index(max_rows[i])+1})" +
	f"\nLowest element is {min_rows[i]} occurs at location ({i+1}, {min_rows.index(min_rows[i])+1})" for i in range(r)] +
	[f"\nColumn #{i+1}:" +
	f"\nHighest element is {max_cols[i]} occurs at location ({column.index(max_cols[i])+1}, {i+1})" +
	f"\nLowest element is {min_cols[i]} occurs at location ({column.index(min_cols[i])+1}, {i+1})" for i, column in enumerate(zip(*list2D))]))
