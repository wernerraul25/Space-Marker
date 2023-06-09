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
icone = pygame.image.load("icone.png")
icone = pygame.image.load("icone.png") #EU NÃO FAÇO IDEIA O POR QUÊ, MAS ASSIM APARECE O ICONE AUHSAUHSUASHS

#audio de fundo
audio_fundo = pygame.mixer.Sound("audio_espaco.mp3")
audio_fundo.play(-1) #fica em loop
audio_fundo.set_volume(0.2) #volume mais baixo

#nome e icone
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
pygame.display.set_icon(icone)

#fonte
fonte_estrela = pygame.font.Font(None,24)
fonte = pygame.font.Font(None,28)

#variáveis
running = True
posicao = (0,0)
nome = None
mostra_marcacao = True
contador = 0
contador2 = 0

#dicionarios
estrelas = {}

#funções
#função para salvar as posições em um arquivo json
def salva_posicao():
     with open("estrelas.json","w") as file:
          json.dump(estrelas,file)
#função para carregar as posições em um arquivo json
def carrega_posicao():
    global estrelas
    try:
        with open("estrelas.json","r") as file:
            estrelas = json.load(file)
    except:
        with open("estrelas.json","w") as file:
            json.dump(estrelas,file)
#função para excluir todas as posições da tela
def exclui_posicao():
     estrelas.clear()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salva_posicao()
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            salva_posicao()
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #só funciona com botão esquerdo do mouse
            posicao = pygame.mouse.get_pos()
            nome = simpledialog.askstring("Space", "Nome da Estrela:")
            if nome == "":
                nome = "Desconhecido"
                if "Desconhecido" in estrelas: #salva desconhecidos infinitos no dicionario, com o número de cada desconhecido do lado
                    contador = contador + 1
                    nome = "Desconhecido" + str(contador)
            elif nome in estrelas:
                contador2 = contador2 + 1
                nome = nome + str(contador2)
            elif nome: #vai que
                    nome = nome
            elif nome is None:
                    continue
            estrelas[nome]= posicao
            print(contador2)
            print(estrelas)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            salva_posicao()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            carrega_posicao()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            exclui_posicao()   #apaga da tela as marcações e limpa o dicionario

    #mostra na tela
    tela.blit(fundo, (0,0)) #fundo
    #pos_texto = tuple(valor - pos_diminuir for valor in (posicao)) #posição do texto acima da estrela

    #percorre as chaves(estrelas) do dicionário
    for chave in estrelas:
        posicao = estrelas[chave]
        pygame.draw.circle(tela,white,(posicao),5)
        nome_estrela = fonte_estrela.render(chave + str(posicao),True,white)
        tela.blit(nome_estrela,(posicao))

    #obter as chaves do dicionario
    chaves = list(estrelas.keys())

    #printa a linha
    for i in range(len(chaves)-1):
         chave_atual = chaves[i]
         chave_proximo = chaves[i + 1]
         ponto_atual = estrelas[chave_atual]
         proximo_ponto = estrelas[chave_proximo]
         pygame.draw.line(tela,white,ponto_atual,proximo_ponto)
    
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