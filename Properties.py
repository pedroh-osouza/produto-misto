import numpy as np
from random import randint

class Properties:
    def __init__(self, vetor1, vetor2, vetor3):
        self.vetor1 = vetor1
        self.vetor2 = vetor2
        self.vetor3 = vetor3
        self.produtoMisto = self.setProdutoMisto()
    
    def setProdutoMisto(self):
        produtoVetorial = np.cross(self.vetor1, self.vetor2)

        produtoMisto = np.dot(produtoVetorial, self.vetor3)

        return produtoMisto

    def one(self): # produto misto é o valor de (u.v).w, esse valor é igual a determiante da sua  matriz
        matriz = np.array([self.vetor1, self.vetor2, self.vetor3])
        determinante = round(np.linalg.det(matriz), 1)

        if(self.produtoMisto == determinante): return True
        return False

    def two(self): # (u.v).w é igual a 0 se e somente se for linearmente dependente.
        ld = False
        li = False

        matriz = np.array([self.vetor1, self.vetor2, self.vetor3])
        determinante = np.linalg.det(matriz)
        if(determinante == 0): ld = True
        if(determinante != 0): li = True

        if(ld == True and determinante == 0 and self.produtoMisto == 0): return "Linearmente Dependente"
        if(li == True and determinante != 0 and self.produtoMisto != 0): return "Linearmente Independente"
        return False

    def three(self): #
        produtoMistoInverso = - (np.dot(np.cross(self.vetor2, self.vetor1), self.vetor3))

        if(self.produtoMisto == produtoMistoInverso): return True
        return False

    def four(self): # SE PRODUTO VETORILA DE (U.V).W É IGUAL DE (W.U).V POR EXEMPLO.
        produtoMisto312 = np.dot(np.cross(self.vetor3, self.vetor1), self.vetor2)
        produtoMisto312 = np.dot(np.cross(self.vetor2, self.vetor3), self.vetor1)

        if(self.produtoMisto == produtoMisto312 == produtoMisto312): return True
        return False

    def five(self): #
        a = randint(0, 9)
        b = randint(0, 9)
        c = randint(0, 9)

        produtoMisto1 = np.dot(np.cross((a*self.vetor1), (b*self.vetor2)), (c*self.vetor3))
        produtoMisto2 = a * b * c * (np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3))

        if(produtoMisto1 == produtoMisto2): return True
        return False

    def six(self): # O PRODDUTO MISTO DE (U+U.V).W É = A (U.V).W.2
        #Vetor 1
        produtoMisto1 = np.dot(np.cross(self.vetor1 * 2, self.vetor2), self.vetor3)
        produtoMisto2 = np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3) * 2

        #Vetor 2
        produtoMisto3 = np.dot(np.cross(self.vetor1, self.vetor2 * 2), self.vetor3)
        produtoMisto4 = np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3) * 2

        #Vetor 2
        produtoMisto5 = np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3 * 2)
        produtoMisto6 = np.dot(np.cross(self.vetor1, self.vetor2), self.vetor3) * 2

        if((produtoMisto1 == produtoMisto2) and (produtoMisto3 == produtoMisto4) and (produtoMisto5 == produtoMisto6)): return True
        return False

    def seven(self):
        return self.produtoMisto

    def eight(self):
        if(self.produtoMisto > 0): return 'Base Positiva'
        return 'Base Negativa'