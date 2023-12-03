n1= int(input("Enter the no. of integers to be stored in the first list: "))
n2= int(input("Enter the no. of integers to be stored in the second list: "))
print(f"\nEnter {n1} numbers for list 1 below: ")
first_list = [int(input(f"Enter Number {i+1}: ")) for i in range(n1)]
print(f"\nEnter {n2} numbers for list 2 below: ")
second_list = [int(input(f"Enter Number {i+1}: ")) for i in range(n2)]

common_list = sorted([num for i, num in enumerate(first_list+second_list) if num in first_list and num in second_list])
uncommon_list = sorted([num for i, num in enumerate(first_list+second_list) if first_list.count(num)==0 or second_list.count(num)==0])

print("\nCommon elements::\n", common_list, 
	"\nUncommon elements:\n", uncommon_list, sep='')