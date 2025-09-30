import pygame

# Inicializa o Pygame
pygame.init()

# Cria a janela
tela = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Triângulo e Quadrado")

# Define cores (R, G, B)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche o fundo de branco
    tela.fill(BRANCO)

    # --- Desenhos ---
    # Quadrado (x, y, largura, altura)
    pygame.draw.rect(tela, AZUL, (50, 50, 100, 100))

    # Triângulo (polígono com 3 pontos)
    pontos_triangulo = [(250, 50), (200, 150), (300, 150)]
    pygame.draw.polygon(tela, VERMELHO, pontos_triangulo)

    # Atualiza a tela
    pygame.display.flip()

# Finaliza
pygame.quit()