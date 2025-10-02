import pygame

class Peca():
    def __init__(self, linha, coluna, cor):
        self.linha = linha
        self.coluna = coluna
        self.cor = cor
    
    def desenhar(self, tela, tamanho):
        x = self.coluna * tamanho + tamanho // 2
        y = self.linha * tamanho + tamanho // 2
        r = tamanho // 3
        cor = None
        if self.cor == 'branco':
            cor = (121, 180, 134)
        else:
            cor = (248, 180, 134)
        pygame.draw.circle(tela, cor, (x,y), r)

class Cavalo(Peca):
    def __init__(self, linha, coluna, cor):
        super().__init__(linha, coluna, cor)

    def desenhar(self, tela, tamanho):
        x = self.coluna * tamanho
        y = self.linha * tamanho
        if self.cor == 'branco':
            image = pygame.transform.scale(
                pygame.image.load('img/cavalo.png'),
                (tamanho, tamanho)
            )
        else:
            image = pygame.transform.scale(
                pygame.image.load('img/cavalo_preto.png'),
                (tamanho, tamanho)
            )
        tela.blit(image, (x, y))

class Torre(Peca):
    def __init__(self, linha, coluna, cor):
        super().__init__(linha, coluna, cor)

    def desenhar(self, tela, tamanho):
        x = self.coluna * tamanho 
        y = self.linha * tamanho 
        if self.cor == 'branco':
            image = pygame.transform.scale(
                pygame.image.load('img/torre.png'),
                (tamanho, tamanho)
            )
        else:
            image = pygame.transform.scale(
                pygame.image.load('img/torre_preta.png'),
                (tamanho, tamanho)
            )
        tela.blit(image, (x, y))

class Peao(Peca):
    def __init__(self, linha, coluna, cor):
        super().__init__(linha, coluna, cor)
    
    def desenhar(self, tela, tamanho):
        x = self.coluna * tamanho
        y = self.linha * tamanho
        if self.cor == 'branco':
            image = pygame.transform.scale(
                pygame.image.load('img/peao.png'),
                (tamanho, tamanho)
            )
        else:
            image = pygame.transform.scale(
                pygame.image.load('img/peao_preto.png'),
                (tamanho, tamanho)
            )
        tela.blit(image, (x, y))

class Bispo(Peca):
    def __init__(self, linha, coluna, cor):
        super().__init__(linha, coluna, cor)
    
    def desenhar(self, tela, tamanho):
        x = self.coluna * tamanho
        y = self.linha * tamanho
        if self.cor == 'branco':
            image = pygame.transform.scale(
                pygame.image.load('img/bispo.png'),
                (tamanho, tamanho)
            )
        else:
            image = pygame.transform.scale(
                pygame.image.load('img/bispo_preto.png'),
                (tamanho, tamanho)
            )
        tela.blit(image, (x, y))