n = int(input("Enter the no. of numbers to be stored in the list: "))
num_list = [float(input(f"Enter integer #{i+1}: ")) for i in range(n)]

if all(num_list[i]>=num_list[i+1] for i in range(n-1)):
	print("\nNumbers are arranged in descending order.", sep='')
elif all(num_list[i]<=num_list[i+1] for i in range(n-1)):
	print("\nNumbers are arranged in ascending order.", sep='')
else:
	print("\nNumbers are NOT arranged in any order.", sep='')