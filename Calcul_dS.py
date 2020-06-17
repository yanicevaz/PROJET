#Produit Vectoriel en dimension 3
def CalculDS(A,B):
    resultat = []
    for i in range(3):
        resultat.append(0.5*(A[(i+1) % 3]*B[(i+2) % 3] - A[(i+2) % 3]*B[(i+1) % 3]))
    return resultat

# test
# A = [1, 2, 0]
# B = [3, 1, 2]
# C = CalculDS(A,B)
# print(C)
