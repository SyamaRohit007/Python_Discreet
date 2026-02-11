values = [True,False]
# print("p \t  q \t  p v q")
# for p in values :
#     for q in values:
#         print(f"{p} \t {q} \t {p or q}")

def disjunction(p,q):
    return p or q
print("p \t  q \t  p v q")
for p in values:
    for q in values:
        print(f"{p} \t {q} \t {disjunction(p,q)}")
