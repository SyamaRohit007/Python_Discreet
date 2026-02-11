values = [True,False]
print("p \t  q \t  p => q")
for p in values :
    for q in values:
        print(f"{p} \t {q} \t {not p or q}")

def conditional(p,q):
    return not p or q
print("p \t  q \t  p => q")
for p in values:
    for q in values:
        print(f"{p} \t {q} \t {conditional(p,q)}")