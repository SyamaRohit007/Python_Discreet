values = [True,False]
print("p \t  q \t  p ^ q")
for p in values :
    for q in values:
        print(f"{p} \t {q} \t {p and q}")

def conjunction(p,q):
    return p and q
print("p \t  q \t  p ^ q")
for p in values:
    for q in values:
        print(f"{p} \t {q} \t {conjunction(p,q)}")