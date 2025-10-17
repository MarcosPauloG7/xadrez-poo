import pygame
from peca import Cavalo, Torre, Peao, Bispo, Rei, Rainha

class Tabuleiro():
    def __init__(self, tela):
        self.tela = tela
        self.linhas = 8
        self.colunas = 8
        self.tamanho = 70
        self.pecas = []
        self.turno_atual = "branco"
        self.peca_selecionada = None
        self.matriz = self.__inicializar_matriz()
        self.__inicializar_peao()
        self.__inicializar_torre()
        self.__inicializar_cavalo()
        self.__inicializar_bispo()
        self.__inicializar_rei_rainha()

    def __inicializar_matriz(self):
        return [
            [None for _ in range(self.colunas)]
            for _ in range(self.linhas)
        ]
    
    def __inicializar_rei_rainha(self):
        # Rei
        self.adicionar_pecas(Rei(0,4,"branco"))
        self.adicionar_pecas(Rei(7,4,"preto"))

        # Rainha
        self.adicionar_pecas(Rainha(0,3,"branco"))
        self.adicionar_pecas(Rainha(7,3,"preto"))

    def __inicializar_bispo(self):
        self.adicionar_pecas(Bispo(0,2,"branco"))
        self.adicionar_pecas(Bispo(0,5,"branco"))
        self.adicionar_pecas(Bispo(7,2,"preto"))
        self.adicionar_pecas(Bispo(7,5,"preto"))

    def __inicializar_cavalo(self):
        self.adicionar_pecas(Cavalo(0,1,"branco"))
        self.adicionar_pecas(Cavalo(0,6,"branco"))
        self.adicionar_pecas(Cavalo(7,1,"preto"))
        self.adicionar_pecas(Cavalo(7,6,"preto"))

    def __inicializar_torre(self):
        self.adicionar_pecas(Torre(0,0,"branco"))
        self.adicionar_pecas(Torre(0,7,"branco"))
        self.adicionar_pecas(Torre(7,0,"preto"))
        self.adicionar_pecas(Torre(7,7,"preto"))

    def __inicializar_peao(self):
        for c in range(self.colunas):
            peao = Peao(1, c, "branco")
            peao_preto = Peao(6, c, "preto")
            self.pecas.append(peao)
            self.pecas.append(peao_preto)
            self.matriz[1][c] = peao
            self.matriz[6][c] = peao_preto

    def clicar(self, pixel_x, pixel_y):
        x = pixel_y // self.tamanho
        y = pixel_x // self.tamanho
        peca = self.matriz[x][y]

        if not self.peca_selecionada and peca:
            if peca.cor == self.turno_atual:
                self.peca_selecionada = peca
                self.movimentos_possiveis = peca.movimentos_validos(self.matriz)
        elif self.peca_selecionada:
            if peca and peca.cor == self.turno_atual:
                self.peca_selecionada = peca
                self.movimentos_possiveis = peca.movimentos_validos(self.matriz)
            else :
                destino = (x,y)
                if hasattr(self, 'movimentos_possiveis') and destino in self.movimentos_possiveis:
                    linha = self.peca_selecionada.linha
                    coluna = self.peca_selecionada.coluna
                    if peca: 
                        self.pecas.remove(peca)
                    self.matriz[linha][coluna] = None

                    if hasattr(self.peca_selecionada, 'mover'):
                        self.peca_selecionada.mover(x,y)
                    else:
                        self.peca_selecionada.linha = x
                        self.peca_selecionada.coluna = y
                    
                    self.matriz[x][y] = self.peca_selecionada

                    if isinstance(self.matriz[x][y], Peao):
                        if (self.matriz[x][y].cor == 'branco' and x == 7) or (self.matriz[x][y].cor == 'preto' and x == 0):
                            cor = self.matriz[x][y].cor
                            self.pecas.remove(self.matriz[x][y])
                            nova_rainha = Rainha(x, y, cor)
                            self.adicionar_pecas(nova_rainha)

                    self.peca_selecionada = None
                    self.movimentos_possiveis = []
                    self.trocar_turno()
                else:
                    self.peca_selecionada = None
                    self.movimentos_possiveis = []
        
    
    def trocar_turno(self):
        if self.turno_atual == "branco":
            self.turno_atual = "preto"
        else:
            self.turno_atual = "branco"
    
    def adicionar_pecas(self, peca):
        self.pecas.append(peca)
        self.matriz[peca.linha][peca.coluna] = peca


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
        
        if self.peca_selecionada:
            linha = self.peca_selecionada.linha
            coluna = self.peca_selecionada.coluna
            x = coluna * self.tamanho
            y = linha * self. tamanho
            pygame.draw.rect(self.tela, (0, 255, 0),(x, y, self.tamanho, self.tamanho), 5)

        if hasattr(self, 'movimentos_possiveis'):
            for (ml, mc) in self.movimentos_possiveis:
                cx = mc * self.tamanho + self.tamanho // 2
                cy = ml * self.tamanho + self.tamanho // 2
                pygame.draw.circle(self.tela, (50, 50, 255), (cx, cy), 8)

        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                peca = self.matriz[linha][coluna]
                if peca:
                    peca.desenhar(self.tela, self.tamanho)
