from Algo_Dichotomie import *

class Bateau:
    def __init__(self,nom,masse,coque):
        self.__nom = nom
        self.__masse = masse
        self.__coque = coque
        self.__mesh = mesh.Mesh.from_file(self.__coque)

    def getNom(self):
        return self.__nom
    def getPoids(self):
        return (self.__masse * 9.81)
    def getCoque(self):
        return self.__coque
    def getMesh(self):
        return self.__mesh

    def translaZ(self,choixtransla):
        for i in self.__mesh.vectors:
            for y in i:
                y[2] = y[2] + choixtransla

# #Tests
# tonnerre = Bateau("PetitTonerre",100,'Cylindrical__HULL.stl')
# print(CalculF(tonnerre.getMesh().vectors[0],9.81))
# print(CalculF([[0,0,0],[1,0,0],[0,1,0]],9.81))
# print(CalculF([[0,0,-1],[1,0,-1],[0,1,-1]],9.81)) #On s'attends a pression/2

# #Test calcul DS
# a = [1,0,0]
# b = [0,1,0]
# print(CalculPousseeArchimede(tonnerre,0))
# print(CalculDS(a,b))
