def power(base,exponent):
    if exponent==0:
        return 1
    elif exponent>0:
        return base*power(base,exponent-1)
    else:
        return 1/ power(base,-exponent)
n=int(input("Enter the base value: "))
d=int(input("Enter the exponent value: "))
print("The exponential value is ",power(n,d)) 