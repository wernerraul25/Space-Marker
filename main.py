import pygame
from tkinter import simpledialog
import json #para criar o arquivo

pygame.init()

#tamanho tela
largura = 1280
altura = 720
tamanho = (largura,altura)
black = (0,0,0)
white = (255,255,255)

#imagens
fundo = pygame.image.load("fundo.jpg")
icone = pygame.image.load("icone.png") #não aparece o icone

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
mostra_marcacao = True

#dicionarios
posicoes = {}

#funções
#função para salvar as posições em um arquivo json
def salva_posicao():
     with open("posicoes.json","w") as file:
          json.dump(posicoes,file)
#função para carregar as posições em um arquivo json
def carrega_posicao():
    global posicoes
    try:
        with open("posicoes.json","r") as file:
            posicoes = json.load(file)
    except:
        with open("posicoes.json","w") as file:
            json.dump(posicoes,file)
#função para excluir todas as posições da tela
def exclui_posicao():
     posicoes.clear()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #só funciona com botão esquerdo do mouse;)
                    x_y = pygame.mouse.get_pos()
                    nome_estrela = simpledialog.askstring("Space", "Nome da Estrela:")
                    if nome_estrela == "":
                        nome_estrela = "Desconhecido"
                    elif nome_estrela: #vai que
                         nome_estrela = nome_estrela
                    elif nome_estrela is None:
                         continue
                    posicoes[nome_estrela] = x_y
                    print(posicoes)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            salva_posicao()
            #salva_nome()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            carrega_posicao()
            #carrega_nome()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            exclui_posicao()   #apaga da tela as marcações e limpa o dicionario
            #exclui_nome()

    #mostra na tela
    tela.blit(fundo, (0,0)) #fundo
    pos_texto = tuple(valor - pos_diminuir for valor in (x_y)) #posição do texto acima da estrela

    #ele pega a chave do dicionario, por isso o erro
    #for chave in posicoes:
        #print(chave)
    
    #percorre as chaves(estrelas) do dicionário
    for chave in posicoes:
        posicao = posicoes[chave] #pega a posição de cada estrela(chave)
        pygame.draw.circle(tela,white,(posicao),5)

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