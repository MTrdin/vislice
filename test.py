#program, ki izpiše vsa praštevila do 200
def je_prastevilo(n):
    if n == 1:
        return False
    for a in range(2, a):
        if n% a == 0:
            return False
    return True

for i in range(2, 201):
    if je_prastevilo(a):
        print a
