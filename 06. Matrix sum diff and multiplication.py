print("Enter the dimensions of the first 2-D list:")
r1 = int(input("Enter the no. of rows: "))
c1 = int(input("Enter the no. of columns: "))
first_list = [[int(input(f"Enter number #({i+1}, {j+1}): ")) for j in range(c1)] for i in range(r1)]
print("\nEnter the dimensions of the second 2-D list:")
r2 = int(input("Enter the no. of rows: "))
c2 = int(input("Enter the no. of columns: "))
second_list = [[int(input(f"Enter number #({i+1}, {j+1}): ")) for j in range(c2)] for i in range(r2)]

print("\nFirst matrix:\n", "\n".join("\t".join((f"{first_list[i][j]}\t") for j in range(c1)) for i in range(r1)), 
	"\n\nSecond matrix:\n", "\n".join("\t".join((f"{second_list[i][j]}\t") for j in range(c2)) for i in range(r2)), sep='')
if r1==r2 and c1==c2:
	sum_list= [[first_list[i][j]+second_list[i][j] for j in range(c1)] for i in range(r1)]
	diff_list= [[first_list[i][j]-second_list[i][j] for j in range(c1)] for i in range(r1)]
	print("\nMatrix sum:\n", "\n".join("\t".join((f"{sum_list[i][j]}\t") for j in range(c1)) for i in range(r1)), 
		"\n\nMatrix differemce:\n", "\n".join("\t".join((f"{diff_list[i][j]}\t") for j in range(c2)) for i in range(r2)), sep='')
else:
	print("\n\nIncompatible dimensions provided!\nMatrix sum and difference not possible.", sep='')
if c1==r2:
	multiply_list= [[sum(first_list[i][k] * second_list[k][j] for k in range(c1)) for j in range(c1)] for i in range(r2)]
	print("\nMatrix product:\n", "\n".join("\t".join((f"{multiply_list[i][j]}\t") for j in range(c2)) for i in range(r1)), sep='')
else:
	print("\n\nIncompatible dimensions provided!\nMatrix multiplication not possible.", sep='')


