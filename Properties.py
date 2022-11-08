import numpy as np
from random import randint

class Properties:
    def __init__(self, vetor1, vetor2, vetor3):
        self.vetor1 = vetor1
        self.vetor2 = vetor2
        self.vetor3 = vetor3
    
    def one(self):
        matriz = np.array([self.vetor1, self.vetor2, self.vetor3])
        determinante = np.linalg.det(matriz)
        
        produtoMisto = np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3)
        
        if(produtoMisto == determinante): return True
        return False

    def two(self):
        ld = False
        li = False

        produtoMisto = np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3)

        matriz = np.array([self.vetor1, self.vetor2, self.vetor3])
        determinante = np.linalg.det(matriz)
        if(determinante == 0): ld = True
        if(determinante != 0): li = True

        if(ld == True and determinante == 0): return True
        if(li == True and determinante != 0): return True
        return False

    def three(self):
        produtoMisto1 = np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3)

        produtoMisto2 = - (np.dot(np.cross(self.vetor2, self.vetor1), self.vetor3))

        if(produtoMisto1 == produtoMisto2): return True
        return False

    def four(self):
        produtoMisto1 = np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3)
        produtoMisto2 = np.dot(np.cross(self.vetor3, self.vetor1), self.vetor2)
        produtoMisto3 = np.dot(np.cross(self.vetor2, self.vetor3), self.vetor1)

        if(produtoMisto1 == produtoMisto2 == produtoMisto3): return True
        return False

    def five(self):
        a = randint(0, 9)
        b = randint(0, 9)
        c = randint(0, 9)
        

        print(a)
        print(self.vetor1)
        print(a * self.vetor1)

        # produtoMisto1 = np.dot(np.cross((a*self.vetor1), (b*self.vetor2)), (c*self.vetor3))

        # produtoMisto2 = a * b * c * (np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3))

        # print(produtoMisto1)
    def six(self):
        print(self.vetor)
    def seven(self):
        print(self.vetor)
    def eight(self):
        print(self.vetor)
