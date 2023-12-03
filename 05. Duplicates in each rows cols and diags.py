def get_duplicates(num_list):
	return ", ".join([str(elem) for i, elem in enumerate(num_list) if num_list.count(elem)>1 and num_list.index(elem)==i])

n = int(input("Enter the no. of rows/columns in which elements are to be stored: "))
list2D = [[int(input(f"Enter number #({i+1}, {j+1}): ")) for j in range(n)] for i in range(n)]

dup_rows= [get_duplicates(list2D[i]) for i in range(n)]
dup_cols= [get_duplicates(column) for column in zip(*list2D)]
first_diag= [list2D[i][i] for i in range(n)]
second_diag= [list2D[i][n-i-1] for i in range(n)]

print("\n"+"\n".join([f"Row #{i+1} has {dup_rows[i]} as duplicate element(s)" for i in range(n) if dup_rows[i]!=""]+
	[f"Column #{i+1} has {dup_cols[i]} as duplicate element(s)" for i in range(n) if dup_cols[i]!=""]),
	(f"\n\nThe first diagoal has {get_duplicates(first_diag)} as the duplicate element(s)" if get_duplicates(first_diag)!="" else ""),
	(f"\n\nThe second diagoal has {get_duplicates(second_diag)} as the duplicate element(s)" if get_duplicates(second_diag)!="" else ""))
