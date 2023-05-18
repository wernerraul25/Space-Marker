import pygame

pygame.init()


#tamanho tela
largura = 600
altura = 400
tamanho = (largura,altura)
black = (0,0,0)
white = (255,255,255)


clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Space Marker")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    tela.fill(black)
    
    pygame.display.update()
    clock.tick(144)

pygame.quit()