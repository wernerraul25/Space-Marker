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
icone = pygame.image.load("icone.png")

#audio de fundo
audio_fundo = pygame.mixer.Sound("audio_espaco.mp3")
audio_fundo.play(-1) #fica em loop
audio_fundo.set_volume(0.6) #volume mais baixo

#nome e icone
pygame.display.set_caption("Space Marker")
pygame.display.set_icon(icone) #motivo desconhecido não aparece o icone
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)

#fonte
fonte_estrela = pygame.font.Font(None,24)
fonte = pygame.font.Font(None,30)

#variáveis
running = True
x_y = (0,0)
pos_diminuir = 25
nome_estrela = None
nome_estrela_tela = []
mostra_marcacao = True
posicoes = []

#dicionarios
estrelas = {}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #só funciona com botão esquerdo do mouse;)
                    x_y = pygame.mouse.get_pos()
                    nome_estrela = simpledialog.askstring("Space", "Nome da Estrela:")
                    '''if nome_estrela == "":
                        nome_estrela_tela = "Desconhecido" + str(x_y)
                        nome_estrela = "Desconhecido"
                    elif nome_estrela is not None:
                        nome_estrela_tela = nome_estrela  + str(x_y)
                    estrelas[nome_estrela] = x_y
                    posicoes.append(x_y)
                    print(posicoes)'''
                    if nome_estrela == "":
                         nome_estrela = "Desconhecido"
                         posicoes.append(x_y)
                         estrelas[nome_estrela] = posicoes[-1]
                    elif nome_estrela is not None:
                         posicoes.append(x_y)
                         estrelas[nome_estrela] = posicoes[-1]
                    nome_estrela_tela = nome_estrela + str(posicoes[-1])
                    print(estrelas)
                         
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            mostra_marcacao = False   #apaga da tela as marcações e limpa o dicionario
            estrelas = {}
            print(estrelas)

    #mostra na tela
    tela.blit(fundo, (0,0)) #fundo
    pos_texto = tuple(valor - pos_diminuir for valor in x_y) #posição do texto acima da estrela
    
    if mostra_marcacao: #se deletar o dicionario, apaga as marcações da tela
        for estrela, posicao in estrelas.items():
            texto_estrela = fonte.render(estrela, True, white)
            tela.blit(texto_estrela, pos_texto)
            pygame.draw.circle(tela, white, (x_y), 5) #circulo
        '''texto_estrela = fonte_estrela.render(str(nome_estrela_tela),True,white) #cria o texto da estrela
        tela.blit(texto_estrela,pos_texto) #mostra o texto da estrela
        pygame.draw.circle(tela, white, (x_y), 5) #circulo'''
    
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