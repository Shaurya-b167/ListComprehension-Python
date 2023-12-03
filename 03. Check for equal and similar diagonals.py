n = int(input("Enter the no. of rows/columns in which elements are to be stored: "))
list2D = [[int(input(f"Enter number #({i+1}, {j+1}): ")) for j in range(n)] for i in range(n)] 

first_diag= [list2D[i][i] for i in range(n)]
second_diag= [list2D[i][n-i-1] for i in range(n)]
similar_cnt= sum(second_diag.count(num)==first_diag.count(num) for num in first_diag)

if similar_cnt!=n:
	print("\nThe diagonals of the given list are neither equal nor similar!",
		"\nThe elements of the given list after swapping the diagonals are:\n",
		"\n".join("\t".join((f"{second_diag[i] if i==j else first_diag[i] if i==n-j-1 else list2D[i][j]}\t") for j in range(n)) for i in range(n)), sep='')
else:
	if first_diag==second_diag:
		print("\nThe diagonals of the given list are equal and similar!")
	else:
		print("\nThe diagonals of the given list are similar!")