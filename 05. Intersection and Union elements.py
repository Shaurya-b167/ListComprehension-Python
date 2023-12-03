n1= int(input("Enter the no. of integers to be stored in the first list: "))
n2= int(input("Enter the no. of integers to be stored in the second list: "))
print(f"\nEnter {n1} numbers for list 1 below: ")
first_list = [int(input(f"Enter Number {i+1}: ")) for i in range(n1)]
print(f"\nEnter {n2} numbers for list 2 below: ")
second_list = [int(input(f"Enter Number {i+1}: ")) for i in range(n2)]

intersection_list = list(set([elem for elem in first_list if elem in second_list]))
union_list= list(set(first_list+second_list))

print("\nFirst multi-set elements:\n", first_list, 
	"\nSecond multi-set elements:\n", second_list, sep='')
print("\nIntersection elements:\n", intersection_list, 
	"\nUnion set elements:\n", union_list, sep='')