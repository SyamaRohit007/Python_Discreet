def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number :"))
if n<0:
    print("the factorial doesnt exist")
else:
    for i in range(1,n):
     print("the factorial of the number",i,"is",factorial(i))