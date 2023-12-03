n = int(input("Enter the no. of rows/columns in which elements are to be stored: "))
list2D = [[int(input(f"Enter number #({i+1}, {j+1}): ")) for j in range(n)] for i in range(n)]
check_sum= sum(list2D[0])

row_cnt= sum(sum(list2D[i])==check_sum for i in range(1, n))
col_cnt= sum(sum(column)==check_sum for column in zip(*list2D))
first_diag= sum(list2D[i][i] for i in range(n))
second_diag= sum(list2D[i][n-i-1] for i in range(n))

if row_cnt!=n-1 or col_cnt!=n or first_diag!=check_sum or second_diag!=check_sum:
	print("\nThe given 2D list is NOT a Magic Square!")
	saddle_point= [[min(list2D[j]) for j in range(n) if max(column)==min(list2D[j]) and j==column.index(min(list2D[j]))] for column in zip(*list2D)]
	print(f"\nSaddle point {saddle_point[0]} exists in the list at location ", sep='') 
else:
	print("\nThe given 2D list is a Magic Square!")