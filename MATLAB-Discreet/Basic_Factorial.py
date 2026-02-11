def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number :"))
if n<0:
    print("the factorial doesnt exist")
else:
    print("the factorial of the number",n,"is",factorial(n))