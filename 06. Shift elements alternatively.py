n= int(input("Enter the no. of numbers to be stored: "))
num_list = [int(input(f"Enter number #{i+1}: ")) for i in range(n)]

# Use only two conditions below to fix the code line.
new_list= [num_list[i if i==n-1 and n%2==1 else i+ (i%2)*-1 + ((i%2)-1)*-1] for i in range(n)]

print("\nGiven list:\n", num_list,
	"\n\nList after re-arranging:\n", new_list, sep='')