import pygame

class Peca():
    def __init__(self, linha, coluna, cor):
        self.linha = linha
        self.coluna = coluna
        self.cor = cor
    
    def desenhar(self, tela, tamanho):
        x = self.coluna*tamanho + tamanho // 2
        y = self.linha*tamanho + tamanho // 2
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
        x = self.coluna*tamanho + tamanho // 2
        y = self.linha*tamanho + tamanho // 2
        r = tamanho // 3
        cor = None
        if self.cor == 'branco':
            cor = (121, 180, 134)
        else:
            cor = (248, 180, 134)
        pontas_triangulo = [
            (x, y - r),
            (x - r, y + r),
            (x + r, y + r)
        ]
        pygame.draw.polygon(tela, cor, pontas_triangulo)

class Torre(Peca):
    def __init__(self, linha, coluna, cor):
        super().__init__(linha, coluna, cor)

    def desenhar(self, tela, tamanho):
        x = self.coluna*tamanho + tamanho // 2
        y = self.linha*tamanho + tamanho // 2
        r = tamanho // 3
        cor = None
        if self.cor == 'branco':
            cor = (121, 180, 134)
        else:
            cor = (248, 180, 134)

        lado = int(tamanho * 0.6)
        rect = pygame.Rect(0,0, lado, lado)
        rect.center = (x,y)
        pygame.draw.rect(tela, cor, rect)