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
        self.primeiro_movimento = True

    def mover(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.primeiro_movimento = False

    def movimentos_validos(self, matriz):
        movimentos = []
        linhas = len(matriz)
        colunas = len(matriz[0])

        direcao = 1 if self.cor == 'branco' else -1

        frente_l = self.linha + direcao
        frente_c = self.coluna

        if 0 <= frente_l < linhas:
            if matriz[frente_l][frente_c] is None:
                movimentos.append((frente_l, frente_c))
                duas_frentes_l = self.linha + 2 * direcao
                if self.primeiro_movimento and 0 <= duas_frentes_l < linhas:
                    if matriz[duas_frentes_l][frente_c] is None:
                        movimentos.append((duas_frentes_l, frente_c))
                        
        
        for dc in (-1, 1):
            diag_l = self.linha + direcao
            diag_c = self.coluna + dc
            if 0 <= diag_l < linhas and 0 <= diag_c < colunas:
                alvo = matriz[diag_l][diag_c]
                if alvo is not None and alvo.cor != self.cor:
                    movimentos.append((diag_l, diag_c))
    
        return movimentos
    
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

class Rei(Peca):
    def __init__(self, linha, coluna, cor):
        super().__init__(linha, coluna, cor)

    def desenhar(self, tela, tamanho):
        x = self.coluna * tamanho
        y = self.linha * tamanho
        if self.cor == 'branco':
            image = pygame.transform.scale(
                pygame.image.load('img/rei.png'),
                (tamanho, tamanho)
            )
        else:
            image = pygame.transform.scale(
                pygame.image.load('img/rei_preto.png'),
                (tamanho, tamanho)
            )
        tela.blit(image, (x, y))

class Rainha(Peca):
    def __init__(self, linha, coluna, cor):
        super().__init__(linha, coluna, cor)

    def desenhar(self, tela, tamanho):
        x = self.coluna * tamanho
        y = self.linha * tamanho
        if self.cor == 'branco':
            image = pygame.transform.scale(
                pygame.image.load('img/rainha.png'),
                (tamanho, tamanho)
            )
        else:
            image = pygame.transform.scale(
                pygame.image.load('img/rainha_preta.png'),
                (tamanho, tamanho)
            )
        tela.blit(image, (x, y))