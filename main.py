import pygame
from tkinter import simpledialog

pygame.init()


#tamanho tela
largura = 1280
altura = 720
tamanho = (largura,altura)
black = (0,0,0)
white = (255,255,255)

#imagens
fundo = pygame.image.load("fundo.jpg")

#nome e icone
pygame.display.set_caption("Space Marker")
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)

#fonte
fonte = pygame.font.Font(None,25)

#variáveis
running = True
pos = (0,0)
pos_diminuir = 30

item = ""

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
    tela.blit(fundo, (0,0))
    pos_texto = tuple(valor - pos_diminuir for valor in pos)
    texto_estrela = fonte.render(item,True,white)
    tela.blit(texto_estrela,(pos_texto))
    pygame.draw.circle(tela, white, (pos), 10)
    
    pygame.display.update()
    clock.tick(144)

pygame.quit()