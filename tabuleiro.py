import pygame
from peca import Peca, Cavalo, Torre, Peao, Bispo

class Tabuleiro():
    def __init__(self, tela):
        self.tela = tela
        self.linhas = 8
        self.colunas = 8
        self.tamanho = 70
        self.pecas = []
        self.__inicializar_peao()
        self.__inicializar_torre()
        self.__inicializar_cavalo()
        self.__inicializar_bispo()

    def __inicializar_bispo(self):
        self.pecas.append(Bispo(0,2,"branco"))
        self.pecas.append(Bispo(0,5,"branco"))
        self.pecas.append(Bispo(7,2,"branco"))
        self.pecas.append(Bispo(7,5,"branco"))

    def __inicializar_cavalo(self):
        self.pecas.append(Cavalo(0,1,"branco"))
        self.pecas.append(Cavalo(0,6,"branco"))
        self.pecas.append(Cavalo(7,1,"preto"))
        self.pecas.append(Cavalo(7,6,"preto"))

    def __inicializar_torre(self):
        self.pecas.append(Torre(0,0,"branco"))
        self.pecas.append(Torre(0,7,"branco"))
        self.pecas.append(Torre(7,0,"preto"))
        self.pecas.append(Torre(7,7,"preto"))

    def __inicializar_peao(self):
        for c in range(self.colunas):
            peao = Peao(1, c, "branco")
            peao_preto = Peao(6, c, "preto")
            self.pecas.append(peao)
            self.pecas.append(peao_preto)

    def desenhar(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                cor = None
                if (linha + coluna) % 2 == 0:
                    cor=(155,55,0)
                else:
                    cor=(255,120,20)
                
                x = coluna*self.tamanho
                y = linha*self.tamanho
                pygame.draw.rect(self.tela, cor, (x, y, self.tamanho, self.tamanho))

        for peca in self.pecas:
            peca.desenhar(self.tela,self.tamanho)
