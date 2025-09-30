import pygame
from peca import Peca, Cavalo, Torre

class Tabuleiro():
    def __init__(self, tela):
        self.tela = tela
        self.linhas = 8
        self.colunas = 8
        self.tamanho = 70
        self.pecas = []
        self.__inicializar_pecas()

    def __inicializar_pecas(self):
        for l in range(2):
            for c in range(self.colunas):
                peca = Peca(l, c, "branco")
                preta = Peca(l+6, c, "preta")
                self.pecas.append(peca)
                self.pecas.append(preta)
            
            for c in range(self.colunas):
                if c in (1, 6):
                    cavalo_branco = Cavalo(l-1, c, "branco")
                    cavalo_preto = Cavalo(l+7, c, "preto")
                    self.pecas.append(cavalo_branco)
                    self.pecas.append(cavalo_preto)

            for c in range(self.colunas):
                if c in (0, 7):
                    torre_branca = Torre(l-1, c, "branco")
                    torre_preta = Torre(l+7, c, "preto")
                    self.pecas.append(torre_preta)
                    self.pecas.append(torre_branca)

    def desenhar(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                cor = None
                if (linha + coluna) % 2 == 0:
                    cor=(0,0,0)
                else:
                    cor=(255,255,255)
                
                x = coluna*self.tamanho
                y = linha*self.tamanho
                pygame.draw.rect(self.tela, cor, (x, y, self.tamanho, self.tamanho))

        for peca in self.pecas:
            peca.desenhar(self.tela,self.tamanho)
