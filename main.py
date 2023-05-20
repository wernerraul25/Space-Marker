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
fonte_estrela = pygame.font.Font(None,25)
fonte = pygame.font.Font(None,30)

#variáveis
running = True
posicao = (0,0)
pos_diminuir = 25
item = None

#dicionarios
estrelas = {}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
                posicao = pygame.mouse.get_pos()
                item = simpledialog.askstring("Space", "Nome da Estrela:")
                print(item)
                if item == None:
                    item = "Desconhecido" + str(posicao)
                estrelas[item] = posicao
                print(estrelas)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            running = False


    #mostra na tela
    tela.blit(fundo, (0,0)) #fundo
    pos_texto = tuple(valor - pos_diminuir for valor in posicao) #posição do texto acima da estrela
    texto_estrela = fonte_estrela.render(item,True,white) #cria o texto da estrela
    tela.blit(texto_estrela,(pos_texto)) #mostra o texto da estrela
    pygame.draw.circle(tela, white, (posicao), 5) #circulo

    #mostra os F10,F11,F12
    texto_f10 = fonte.render("Pressione F10 para salvar as marcações",True,white)
    texto_f11 = fonte.render("Pressione F11 para carregar as marcações salvas",True,white)
    texto_f12 = fonte.render("Pressione F12 para deletar as marcações",True,white)
    tela.blit(texto_f10,(10,10))
    tela.blit(texto_f11,(10,35))
    tela.blit(texto_f12,(10,60))
    
    pygame.display.update()
    clock.tick(144)

pygame.quit()