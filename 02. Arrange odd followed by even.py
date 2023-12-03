n1= int(input("Enter the no. of integers to be stored in the first list: "))
n2= int(input("Enter the no. of integers to be stored in the second list: "))
print(f"\nEnter {n1} numbers for list 1 below: ")
first_list = [int(input(f"Enter Number {i+1}: ")) for i in range(n1)]
print(f"\nEnter {n2} numbers for list 2 below: ")
second_list = [int(input(f"Enter Number {i+1}: ")) for i in range(n2)]

new_list = [num for i, num in enumerate(first_list+second_list) if num%2!=0] + [num for i, num in enumerate(first_list+second_list) if num%2==0]

print("\nThe list after arranging odd followed by even numbers:\n", new_list, sep='')