def factorial(n):
	if(n==1):
		return 1
	else:
		return n*factorial(n-1)
n=int(input("enter the n value:"))
res=factorial(n)
print("factorial of",n,"is",res)

