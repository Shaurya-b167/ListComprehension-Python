from math import gcd

def is_prime(n):
	return n>1 and all(n%i!=0 for i in range(2, n//2+1))

n = int(input("Enter the no. of integers which are to be stored: "))
num_list = [int(input(f"Enter integer #{i+1}: ")) for i in range(n)]

prime_cnt= sum(is_prime(x) for x in num_list)
compo_cnt= sum(not is_prime(x) and x > 3 for x in num_list)
hcf= gcd(prime_cnt, compo_cnt)

print("\nPrime : Composite = ", prime_cnt//hcf, " : ", compo_cnt//hcf, sep='')