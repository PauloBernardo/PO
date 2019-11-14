import random

class Node(object):
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVL_Tree(object):

    def insert(self, raiz, chave):

        # Passo 1 - Executa a inserção normal da Arvore Binaria
        if not raiz:
            return Node(chave)
        elif chave < raiz.valor:
            raiz.esquerda = self.insert(raiz.esquerda, chave)
        else:
            raiz.direita = self.insert(raiz.direita, chave)

        # Passo 2 - Atualiza a altura do antecesor
        raiz.altura = 1 + max(self.pegarAltura(raiz.esquerda),
                              self.pegarAltura(raiz.direita))

         # Passo 3 - Pega o balanceamento
        balanceamento = self.pegarBalanceamento(raiz)

        # Passo 4 - Verifica o balanceamento
        # Caso 1 - Rotacao simples direita
        if balanceamento > 1 and chave < raiz.esquerda.valor:
            return self.direitaRotacionar(raiz)

        # Caso 2 - Rotacao simples esquerda
        if balanceamento < -1 and chave > raiz.direita.valor:
            return self.esquerdaRotacionar(raiz)

        # Caso 3 - Rotacao dupla direita
        if balanceamento > 1 and chave > raiz.esquerda.valor:
            raiz.esquerda = self.esquerdaRotacionar(raiz.esquerda)
            return self.direitaRotacionar(raiz)

        # Caso 4 - Rotacao dupla esquerda
        if balanceamento < -1 and chave < raiz.direita.valor:
            raiz.direita = self.direitaRotacionar(raiz.direita)
            return self.esquerdaRotacionar(raiz)

        return raiz

    def search(self, raiz, chave):
        if raiz is None:
            return False
        elif raiz.valor == chave:
            return True
        elif raiz.valor > chave:
            return self.search(raiz.esquerda, chave)
        elif raiz.valor < chave:
            return self.search(raiz.direita, chave)
    
    def delete(self, raiz, chave):

        # Passo 1 - Executa o delete normal da Arvore Binaria
        if not raiz:
            return raiz

        elif chave < raiz.valor:
            raiz.esquerda = self.delete(raiz.esquerda, chave)

        elif chave > raiz.valor:
            raiz.direita = self.delete(raiz.direita, chave)

        else:
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp

            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp

            temp = self.pegarMinValueNode(raiz.direita)
            raiz.valor = temp.valor
            raiz.direita = self.delete(raiz.direita,
                                     temp.valor)

        if raiz is None:
            return raiz

        # Passo 2 - Atualiza a altura do antecesor
        raiz.altura = 1 + max(self.pegarAltura(raiz.esquerda),
                              self.pegarAltura(raiz.direita))

        # Passo 3 - Pega o balanceamento
        balanceamento = self.pegarBalanceamento(raiz)

        # Passo 4 - Verifica o balanceamento
        # Caso 1 - Rotacao simples direita 
        if balanceamento > 1 and self.pegarBalanceamento(raiz.esquerda) >= 0:
            return self.direitaRotacionar(raiz)

        # Caso 2 - Rotacao simples esquerda
        if balanceamento < -1 and self.pegarBalanceamento(raiz.direita) <= 0:
            return self.esquerdaRotacionar(raiz)

        # Caso 3 - Rotacao dupla direita
        if balanceamento > 1 and self.pegarBalanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.esquerdaRotacionar(raiz.esquerda)
            return self.direitaRotacionar(raiz)

        # Caso 4 - Rotacao dupla esquerda
        if balanceamento < -1 and self.pegarBalanceamento(raiz.direita) > 0:
            raiz.direita = self.direitaRotacionar(raiz.direita)
            return self.esquerdaRotacionar(raiz)

        return raiz

    def esquerdaRotacionar(self, z):

        y = z.direita
        T2 = y.esquerda

        # Faz a rotação
        y.esquerda = z
        z.direita = T2

        # Atualizar alturas
        z.altura = 1 + max(self.pegarAltura(z.esquerda),
                           self.pegarAltura(z.direita))
        y.altura = 1 + max(self.pegarAltura(y.esquerda),
                           self.pegarAltura(y.direita))

        # Retorna a nova raiz
        return y

    def direitaRotacionar(self, z):

        y = z.esquerda
        T3 = y.direita

        # Fazer a rotação
        y.direita = z
        z.esquerda = T3

        # Atualizar alturas
        z.altura = 1 + max(self.pegarAltura(z.esquerda),
                           self.pegarAltura(z.direita))
        y.altura = 1 + max(self.pegarAltura(y.esquerda),
                           self.pegarAltura(y.direita))

        # Retornar a nova raiz
        return y

    def pegarAltura(self, raiz):
        if not raiz:
            return 0

        return raiz.altura

    def pegarBalanceamento(self, raiz):
        if not raiz:
            return 0

        return self.pegarAltura(raiz.esquerda) - self.pegarAltura(raiz.direita)

    def pegarMinValueNode(self, raiz):
        if raiz is None or raiz.esquerda is None:
            return raiz

        return self.pegarMinValueNode(raiz.esquerda)

    def preOrder(self, raiz):

        if not raiz:
            return

        print("{0} ".format(raiz.valor), end="")
        self.preOrder(raiz.esquerda)
        self.preOrder(raiz.direita)


minhaArvore = AVL_Tree()
raiz = None
nums = list(range(100))
random.shuffle(nums) # [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    raiz = minhaArvore.insert(raiz, num)

# Preordem Traversal
print("Preordem Traversal depois do inserção -")
minhaArvore.preOrder(raiz)
print()

# Delete
chave = 10
raiz = minhaArvore.delete(raiz, chave)

# Preordem Traversal
print("Preordem Traversal depois da deleção -")
minhaArvore.preOrder(raiz)
print()

print(minhaArvore.search(raiz, 9))
print(minhaArvore.search(raiz, 6))
print(minhaArvore.search(raiz, 200))

