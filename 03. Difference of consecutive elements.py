n = int(input("Enter the no. of numbers to be stored in the list: "))
num_list = [float(input(f"Enter Number {i+1}: ")) for i in range(n)]

differences= [round(abs(num_list[i] - num_list[i+1]), 2) for i in range(n-1)]
max_index = differences.index(max(differences))

print(f"\n{'Index':10} {'Difference':10}\n",
	"\n".join(f"{i:<10} {diff:<10}" for i, diff in enumerate(differences)),
	f"\n\nMaximum difference: {differences[max_index]} at index {max_index}", sep='')
