import pygame
from tkinter import simpledialog

pygame.init()


#tamanho tela
largura = 600
altura = 400
tamanho = (largura,altura)
black = (0,0,0)
white = (255,255,255)


clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)

#nome e icone
pygame.display.set_caption("Space Marker")

#variáveis
running = True

#dicionarios
estrelas = {}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela: ")
            print(item)
            if item == None:
                item = "Desconhecido" + str(pos)
            estrelas[item] = pos  #arrumar a biblioteca
            print(estrelas)




    #mostra na tela
    tela.fill(black)
    
    pygame.display.update()
    clock.tick(144)

pygame.quit()