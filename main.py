import pygame
from tabuleiro import Tabuleiro

pygame.init()
tela = pygame.display.set_mode((560,560))
pygame.display.set_caption("Xadrez")
tabuleiro = Tabuleiro(tela)
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False       
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            x,y = pygame.mouse.get_pos()
            tabuleiro.clicar(x,y)

        tabuleiro.desenhar()
        pygame.display.flip()
pygame.quit()