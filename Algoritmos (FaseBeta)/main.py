#encoding=utf-8
from graphics import *
import time,math,random,datetime
import pygame#####################################################################################################
pygame.init()#####################################################################################################
############ -- FUNÇOES -- #######################################################################################

def loading():
  CARREGANDO= Image(Point(0,0),"Imagens/Inicio/CARREGANDO.png")
  CARREGANDO.draw(janela)
  return CARREGANDO
  
def fundo_inicial():
  PNG = "Imagens/Inicio/"
  lista=[]
  lista.append(Image(Point(0,0), PNG + "1.png"))
  lista.append(Image(Point(0,0), PNG + "2.png"))
  lista.append(Image(Point(0,0), PNG + "3.png"))
  lista.append(Image(Point(0,0), PNG + "4.png"))
  lista.append(Image(Point(0,0), PNG + "5.png"))
  lista.append(Image(Point(0,0), PNG + "6.png"))
  lista.append(Image(Point(0,0), PNG + "7.png"))
  lista.append(Image(Point(0,0), PNG + "8.png"))
  lista.append(Image(Point(0,0), PNG + "9.png"))
  lista.append(Image(Point(0,0), PNG + "10.png"))
  lista.append(Image(Point(0,0), PNG + "11.png"))
  lista.append(Image(Point(0,0), PNG + "12.png"))
  lista.append(Image(Point(0,0), PNG + "13.png"))
  lista.append(Image(Point(0,0), PNG +  "14.png"))
  lista.append(Image(Point(0,0), PNG + "extra_1.png"))
  lista.append(Image(Point(0,0), PNG +  "extra_2.png"))
  lista.append(Image(Point(0,0), PNG + "extra_3.png"))
  lista.append(Image(Point(0,0), PNG + "start.png"))
  lista.append(Image(Point(-2000,0), PNG + "goku.png"))
  lista.append(Image(Point(2000,0), PNG + "naruto.png"))
  lista.append(Image(Point(-2000,0), PNG + "vegeta.png"))
  lista.append(Image(Point(2000,0), PNG + "sasuke.png"))
  lista.append(Image(Point(-2000,0), PNG + "majin_boo.png"))
  lista.append(Image(Point(2000,0), PNG + "itachi.png"))
  lista.append(Image(Point(-2000,0), PNG + "freeza.png"))
  lista.append(Image(Point(2000,0), PNG + "madara.png"))
  lista.append(Image(Point(0,0), PNG + "pronto.png"))
  return lista

def selecao_inicial():
  PNG="Imagens/Selecao_de_personagem/"
  PNG2="Imagens/Instrucoes/"
  lista=[]
  lista.append(Image(Point(0,0), PNG + "SELECAO_X.png"))
  lista.append(Image(Point(0,0), PNG2 + "1.png"))
  lista.append(Image(Point(0,0), PNG2 + "2.png"))
  lista.append(Image(Point(0,0), PNG2 + "3.png"))
  lista.append(Image(Point(0,0), PNG2 + "4.png"))
  lista.append(Image(Point(0,0), PNG2 + "5.png"))
  lista.append(Image(Point(0,0), PNG2 + "6.png"))
  lista.append(Image(Point(0,0), PNG2 + "7.png"))
  lista.append(Image(Point(0,0), PNG2 + "8.png"))
  lista.append(Image(Point(0,0), PNG2 + "9.png"))
  lista.append(Image(Point(0,0), PNG2 + "10.png"))
  lista.append(Image(Point(0,0), PNG2 + "11.png"))
  lista.append(Image(Point(0,0), PNG2 + "12.png"))
  lista.append(Image(Point(0,0), PNG2 + "13.png"))
  lista.append(Image(Point(0,0), PNG2 + "14.png"))
  lista.append(Image(Point(0,0), PNG2 + "15.png"))
  lista.append(Image(Point(0,0), PNG2 + "16.png"))
  lista.append(Image(Point(0,0), PNG2 + "17.png"))
  lista.append(Image(Point(0,0), PNG2 + "Instrucoes.png"))	
  return lista

def mapas_iniciais(): 
  PNG = "Imagens/Mapas/"
  lista=[]
  lista.append(Image(Point(0,0), PNG + "mapa1.png"))
  lista.append(Image(Point(0,0), PNG + "mapa2.png"))
  lista.append(Image(Point(0,0), PNG + "mapa3.png"))
  lista.append(Image(Point(0,0), PNG + "mapa4.png"))
  return lista
  
def opcoes_iniciais():
  PNG="Imagens/Opcoes/"
  lista=[]
  lista.append(Image(Point(0,0), PNG + "REGRAS.png"))
  lista.append(Image(Point(0,0), PNG + "PRONTO.png"))
  return lista

def sons_iniciais():
  OGG="Musicas/"
  lista=[]
  lista.append(pygame.mixer.Sound(OGG +  "ABERTURA.ogg"))#############################################################
  lista.append(pygame.mixer.Sound(OGG + "ACTIVE.ogg"))################################################################
  lista.append(pygame.mixer.Sound(OGG + "SELECAO.ogg"))###############################################################
  return lista
  
  
  
  
  
def informacoes_JOGO(x):
  PNG = "Imagens/Informacoes/"
  lista=[]
  lista.append(Image(Point(0,0), PNG + "Informacoes.png"))
  
  if (x[0]==0 and x[1]==0):
  	lista.append(Image(Point(0,0), PNG + "GOKU.png"))
  elif (x[0]==1 and x[1]==0):
  	lista.append(Image(Point(0,0), PNG + "VEGETA.png"))
  elif (x[0]==0 and x[1]==-1): 
  	lista.append(Image(Point(0,0), PNG + "MAJIN_BOO.png"))
  elif (x[0]==1 and x[1]==-1):
  	lista.append(Image(Point(0,0), PNG + "FREEZA.png"))
 
  if (x[2]==0 and x[3]==0):
  	lista.append(Image(Point(0,0), PNG + "NARUTO.png"))
  elif (x[2]==1 and x[3]==0):
  	lista.append(Image(Point(0,0), PNG + "SASUKE.png"))
  elif (x[2]==0 and x[3]==-1):
 		lista.append(Image(Point(0,0), PNG + "MADARA.png"))
  elif (x[2]==1 and x[3]==-1):
 		lista.append(Image(Point(0,0), PNG + "ITACHI.png"))


  	
  if (x[0]==0 and x[1]==0):
  	lista.append("Goku/")
  elif (x[0]==1 and x[1]==0):
  	lista.append("Vegeta/")
  elif (x[0]==0 and x[1]==-1): 
  	lista.append("Majin_boo/")
  elif (x[0]==1 and x[1]==-1):
  	lista.append("Freeza/")
 
  if (x[2]==0 and x[3]==0):
  	lista.append("Naruto/")
  elif (x[2]==1 and x[3]==0):
  	lista.append("Sasuke/")
  elif (x[2]==0 and x[3]==-1):
 		lista.append("Madara/")
  elif (x[2]==1 and x[3]==-1):
 		lista.append("Itachi/")

  return lista

def mapa_no_jogo(x):  
  PNG = "Imagens/Mapas/"
  if (x==0):
    mapa = Image(Point(0,0), PNG +  "LAVA_X.png")
  elif (x==1):
    mapa = Image(Point(0,0), PNG + "GELO_X.png")
  elif (x==2):
    mapa = Image(Point(0,0), PNG + "FLORESTA_X.png")
  else:
    mapa = Image(Point(0,0), PNG + "DESERTO_X.png")
  return mapa
  	
def musica_JOGO(x):###################################################################################################
  OGG = "Musicas/"
  if (x==0):
  	musica = pygame.mixer.Sound(OGG + "BATALHA_LAVA.ogg")#############################################################
  elif (x==1):
  	musica = pygame.mixer.Sound(OGG + "BATALHA_GELO.ogg")#############################################################
  elif (x==2):
  	musica = pygame.mixer.Sound(OGG + "BATALHA_FLORESTA.ogg")#########################################################
  else:
  	musica = pygame.mixer.Sound(OGG + "BATALHA_DESERTO.ogg")##########################################################
  return musica
  
  
  


def inicio(imagens,som):
  som[0].play(100)####################################################################################################
  time.sleep(1)
  X=0
  while (X<6):
    imagens[X].draw(janela)
    update()
    imagens[X].undraw()
    X=X+1
  imagens[6].draw(janela)
  X=8
  while (X<13):
    imagens[X].draw(janela)
    update()
    imagens[X].undraw()
    X=X+1
  imagens[13].draw(janela)
  update()
  time.sleep(0.2)
 
  imagens[25].draw(janela)
  imagens[24].draw(janela)
  imagens[23].draw(janela)
  imagens[22].draw(janela)
  imagens[21].draw(janela)
  imagens[20].draw(janela)
  imagens[19].draw(janela)
  imagens[18].draw(janela)
  update()
    
  for i in range(50):
    imagens[18].move(40,0)
    imagens[19].move(-40,0)
    update()
 
  for i in range(50):
    imagens[20].move(40,0)
    imagens[21].move(-40,0)
    update()
    
  for i in range(50):
    imagens[22].move(40,0)
    imagens[23].move(-40,0)
    update()
    
  for i in range(40):
    imagens[24].move(50,0)
    imagens[25].move(-50,0)
    update() 
    
  time.sleep(0.5)
  imagens[26].draw(janela)
  update()
  imagens[18].undraw()
  imagens[19].undraw()
  imagens[20].undraw()
  imagens[21].undraw()
  imagens[22].undraw()
  imagens[23].undraw()
  imagens[24].undraw()
  imagens[25].undraw()
  imagens[6].undraw()
  imagens[13].undraw()
  
  time.sleep(1)
  cont2=12000
  cont3=0
  while True:
    cont2=cont2+1
    cont3=cont3+1
    if (cont2%24000==0):
        imagens[17].draw(janela)
        update()
    if (cont3%24000==0):    
        imagens[17].undraw()
    
    x=random.randint(0,40000)
    if (x<1):
      imagens[14].draw(janela)
      time.sleep(0.03)
      update()
      imagens[15].draw(janela)
      time.sleep(0.03)
      update()
      imagens[16].draw(janela)
      time.sleep(0.03)
      update()
      imagens[16].undraw()
      time.sleep(0.03)
      imagens[15].undraw()
      time.sleep(0.03)
      imagens[14].undraw()      
      
    A = janela.checkKey()
    if (A!=""):     
      som[0].stop()#########################################################################################
      som[1].play()#########################################################################################
      imagens[17].undraw()
      imagens[26].undraw()
      break
      
def selecao(imagem,som):
  PNG="Imagens/Selecao_de_personagem/"
  imagem[0].draw(janela)
  P1 = Image(Point(0,0), PNG + "P1_UNREADY.png")
  P2 = Image(Point(0,0), PNG + "P2_UNREADY.png")
  P1.draw(janela)
  P2.draw(janela)
  update() 
  contX1=0
  contY1=0
  contX2=0
  contY2=0
  LOCK1=1
  LOCK2=1
  contador=0
  contador2=1
  lista1=[]
  while True: 
  
    contador+=1
    def APAGA(APAGAR):
      if (APAGAR!=[]):
        APAGAR[0].undraw()
        del APAGAR[0]      

    APAGA(lista1)
    imagem[contador2].draw(janela)
    lista1.append(imagem[contador2])
    if (contador%3==1):  
      contador2+=1
      if (contador2==18):
        contador2=1
    mouse = janela.checkMouse()
    if (mouse!=None):
      mouseX , mouseY =  mouse.getX() , mouse.getY() 
      if (mouseX>-568)  and  (mouseX<-440) and (mouseY>-78) and (mouseY<82):
        imagem[18].draw(janela)
        while True:
          LETRA = janela.checkKey()
          mouse = janela.checkMouse()
          if (LETRA!="") or (mouse!=None):
            imagem[18].undraw()
            break
        
    x = janela.checkKey()
    if (x=="space"): ##lock player1
      
      LOCK1=LOCK1+1
      if (LOCK1%2==0):
       	som[1].play()#######################################################################################
        P1_OK = Image(Point(contX1,contY1), PNG + "P1_READY.png")
        P1_OK.draw(janela)
        P1.undraw()
    
      else:
        P1.draw(janela)
        P1_OK.undraw()

    elif (x=="Return"):## lock player2
    
      LOCK2=LOCK2+1
      if (LOCK2%2==0):
      	som[1].play()#######################################################################################
        P2_OK = Image(Point(contX2,contY2), PNG + "P2_READY.png")
        P2_OK.draw(janela)
        P2.undraw()
        
      else:
       P2.draw(janela)
       P2_OK.undraw()

    elif (x=="d") or (x=="D"):  ##PLAYER 1
      if (LOCK1%2==0):
        continue
      elif (contX1==140):
        P1.move(-140,0)
        contX1=0
      else:
        contX1=contX1+140
       	P1.move(140,0)
        
    elif (x=="a") or (x=="A"):
      if (LOCK1%2==0):
        continue
      elif (contX1==0):
        P1.move(140,0)
        contX1=140
      else:
        contX1=contX1-140
       	P1.move(-140,0)
        
    elif (x=="s") or (x=="S"):
      if (LOCK1%2==0):
        continue
      elif (contY1==-140):
        P1.move(0,140)
        contY1=0
      else:
        contY1=contY1-140
        P1.move(0,-140)
        
    elif (x=="w") or (x=="W"):
      if (LOCK1%2==0):
        continue
      elif (contY1==-140):
        P1.move(0,140)
        contY1=0
      else:
        contY1=contY1-140
        P1.move(0,-140)
        
    elif (x=="Right"):         ##PLAYER2
      if (LOCK2%2==0):
        continue
      elif (contX2==140):
        P2.move(-140,0)
        contX2=0
      else:
        contX2=contX2+140
        P2.move(140,0)
        
    elif (x=="Left"):
      if (LOCK2%2==0):
        continue
      elif (contX2==0):
        P2.move(140,0)
        contX2=140
      else:
        contX2=contX2-140
       	P2.move(-140,0)
        
    elif (x=="Down"):
      if (LOCK2%2==0):
        continue
      elif (contY2==-140):
        P2.move(0,140)
        contY2=0
      else:
        contY2=contY2-140
        P2.move(0,-140)
        
    elif (x=="Up"):
      if (LOCK2%2==0):
        continue
      elif (contY2==-140):
        P2.move(0,140)
        contY2=0
      else:
        contY2=contY2-140
        P2.move(0,-140)
        
    elif (LOCK1%2==0 and LOCK2%2==0):
      APAGA(lista1)
      lista=[]
      lista.append(contX1/140)
      lista.append(contY1/140)
      lista.append(contX2/140)
      lista.append(contY2/140)
      P1_OK.undraw()
      P2_OK.undraw()
      imagem[0].undraw()
      return lista      #return dados x e y para saber qual personagem selecionado
       
def mapa(imagens,som,voltar):
  lista=[]
  X1=imagens[0]
  X2=imagens[1]
  X3=imagens[2]
  X4=imagens[3] 
  X1.draw(janela)
  voltar.draw(janela)
  lista.append(X1)
  X=0
  while True:
    x=janela.checkKey()
    if (x=="a") or (x=="A") or (x=="Left"):
      lista[0].undraw()
      del lista[0]
      X1.draw(janela)
      if (voltar!=None):
        voltar.undraw()
      voltar.draw(janela)
      lista.append(X1)
      X=0
      
    if (x=="w") or (x=="W") or (x=="Up"):
      lista[0].undraw()
      del lista[0]
      X2.draw(janela)
      if (voltar!=None):
        voltar.undraw()
      voltar.draw(janela)
      lista.append(X2)
      X=1
      
    if (x=="d") or (x=="D") or (x=="Right"):
      lista[0].undraw()
      del lista[0]
      X3.draw(janela)
      if (voltar!=None):
        voltar.undraw()
      voltar.draw(janela)
      lista.append(X3)
      X=2
      
    if (x=="s") or (x=="S") or (x=="Down"):
      lista[0].undraw()
      del lista[0]
      X4.draw(janela)
      if (voltar!=None):
        voltar.undraw()
      voltar.draw(janela)
      lista.append(X4)
      X=3
      
    if (x=="Return"):
      som[1].play()#########################################################################################
      lista[0].undraw()
      voltar.undraw()
      return X
    
    if (x=="Escape"):
      lista[0].undraw()
      voltar.undraw()
      return 4  
      
def opcoes(imagens,som,voltar):
  imagens[0].draw(janela)
  voltar.draw(janela)
  SELECIONADO=Rectangle(Point(213,100),Point(332,50))
  SELECIONADO.setWidth(4)
  SELECIONADO.setOutline("gray")
  SELECIONADO.setFill("white")
  SELECIONADO.draw(janela)
  
  VIDA= Text(Point(272,75),"5")
  VIDA.setSize(36)
  VIDA.draw(janela)
  
  DANO= Text(Point(272,-175),"1.0")
  DANO.setSize(36)
  DANO.draw(janela)
  
  update()
  CONT=0
  V=5     #VIDAS
  D=1.0   #DANO
  X1=75
  B=0
  while True:
    A=janela.checkKey() 
    if (CONT==0): 
      if (A=="w") or (A=="W") or (A=="Up"):
        if (X1==75):
          SELECIONADO.move(0,-250)
          X1=-175
        else:
          SELECIONADO.move(0,250)
          X1=75
        
      if (A=="s") or (A=="S") or (A=="Down"):   
        if (X1==-175):
          SELECIONADO.move(0,250)
          X1=75
        else:
          SELECIONADO.move(0,-250)
          X1=-175
      
      
      if (A=="a") or (A=="A") or (A=="Left"):  
        if (X1==75):#VIDA
          if (V==3):
            continue
          else:
            VIDA.undraw()
            V=V-1
            VIDA= Text(Point(272,75), str(V))
            VIDA.setSize(36)
            VIDA.draw(janela)
            update()
        else:        #DANO
          if (D<=1):
            continue
          else:
            DANO.undraw()
            D=D-0.1
            DANO= Text(Point(272,-175), str(D))
            DANO.setSize(36)
            DANO.draw(janela)
            update()
     
      if (A=="d") or (A=="D") or (A=="Right"):
        if (X1==75):#VIDA
          if (V==20):
            continue
          else:
            VIDA.undraw()
            V=V+1
            VIDA= Text(Point(272,75), str(V))
            VIDA.setSize(36)
            VIDA.draw(janela)
            update()
        else:         #DANO
          if (D>=2.5):
            continue
          else:
            DANO.undraw()
            D=D+0.1
            DANO= Text(Point(272,-175), str(D))
            DANO.setSize(36)
            DANO.draw(janela)
            update()
           
    if (A=="Return"):
      B=B+1
      if (B==1):
        imagens[1].draw(janela)
        CONT=1
      if (B==2):
        som[1].play()#######################################################################################
        lista=[V,D]
        time.sleep(1)
        imagens[0].undraw()
        imagens[1].undraw()
        SELECIONADO.undraw()
        DANO.undraw()
        VIDA.undraw()
        voltar.undraw()
        som[2].stop()#######################################################################################
        return lista
    
    if (A=="Escape"):
      CONT=0
      if (B==1):
        imagens[1].undraw()
        B=B-1
      else:
        B=0
        imagens[0].undraw()
        SELECIONADO.undraw()
        DANO.undraw()
        VIDA.undraw()
        voltar.undraw()
        return 4
  
def Vencedor(VENCEDOR,info):
  P1 = info[3]
  P2 = info[4]
  SOM = pygame.mixer.Sound("Musicas/ACTIVE.ogg")
  MUSICA = pygame.mixer.Sound("Musicas/FIM.ogg")
  SAIR = Image(Point(0,0), "Imagens/Inicio/start.png")
  
  if (VENCEDOR=="P1"):
    fundo = Image(Point(0,0), "Imagens/Tela_de_vitoria/P1_WIN.png")
  elif (VENCEDOR=="P2"):
    fundo = Image(Point(0,0), "Imagens/Tela_de_vitoria/P2_WIN.png")
  

  if (P1=="Goku/"):
  	PLAYER1 = Image(Point(-2000,0), "Imagens/Tela_de_vitoria/Goku.png")
  elif (P1=="Vegeta/"):
    PLAYER1 = Image(Point(-2000,0), "Imagens/Tela_de_vitoria/Vegeta.png")
  elif (P1=="Majin_boo/"):
    PLAYER1 = Image(Point(-2000,0), "Imagens/Tela_de_vitoria/Majin_boo.png")
  elif (P1=="Freeza/"):
    PLAYER1 = Image(Point(-2000,0), "Imagens/Tela_de_vitoria/Freeza.png")
 
 
  if (P2=="Naruto/"):
    PLAYER2 = Image(Point(2000,0), "Imagens/Tela_de_vitoria/Naruto.png")
  elif (P2=="Sasuke/"):
    PLAYER2 = Image(Point(2000,0), "Imagens/Tela_de_vitoria/Sasuke.png")
  elif (P2=="Madara/"):
    PLAYER2 = Image(Point(2000,0), "Imagens/Tela_de_vitoria/Madara.png")
  elif (P2=="Itachi/"):
    PLAYER2 = Image(Point(2000,0), "Imagens/Tela_de_vitoria/Itachi.png")
 
  MUSICA.play(-1)
  fundo.draw(janela)
  PLAYER1.draw(janela)
  PLAYER2.draw(janela)
  update()
  
  for i in range(100):
    PLAYER1.move(20,0)
    PLAYER2.move(-20,0)
    update()
    
  time.sleep(3) 
  cont1=10000
  cont2=0
  while True:
    cont1+=1
    cont2+=1
    if (cont1%20000==0):
      SAIR.draw(janela)
      update()
    if (cont2%20000==0):    
      SAIR.undraw()  
    X = janela.checkKey()
    update()
    if (X!=""):
      SOM.play()
      SAIR.undraw()
      MUSICA.stop()
      return
  
  
def jogo(Z,info,musica,mapa): #Z== VIDAS e PONTOS, info== PERSONAGENS, musica==Musica do Mapa, mapa==Qual a ser desenhado 
  FIM = Image(Point(0,0), "Imagens/Efeitos_jogo/GAME.png")
  TRES = pygame.mixer.Sound("Musicas/Efeitos_sonoros/3.ogg")
  DOIS = pygame.mixer.Sound("Musicas/Efeitos_sonoros/2.ogg")
  UM = pygame.mixer.Sound("Musicas/Efeitos_sonoros/1.ogg")
  GOO = pygame.mixer.Sound("Musicas/Efeitos_sonoros/GO.ogg")
  FIM_DE_JOGO = pygame.mixer.Sound("Musicas/Efeitos_sonoros/GAME.ogg")
  def efeitos():
    lista=[]
    PNG="Imagens/Efeitos_jogo/"
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_1.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_2.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_3.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_4.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_5.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_6.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_7.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_1.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_2.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_3.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_4.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_5.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_6.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_7.png"))
    lista.append(Image(Point(650,0), PNG + "Aura1_P1.png"))
    lista.append(Image(Point(650,0), PNG + "Aura2_P1.png"))  
    return lista

  def efeitos2():
    lista=[]
    PNG="Imagens/Efeitos_jogo/"
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_1.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_2.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_3.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_4.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_5.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_6.png"))
    lista.append(Image(Point(-650,0), PNG + "explosao_direita_7.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_1.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_2.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_3.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_4.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_5.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_6.png"))
    lista.append(Image(Point(650,0), PNG + "explosao_esquerda_7.png"))
    lista.append(Image(Point(650,0), PNG + "Aura1_P2.png"))
    lista.append(Image(Point(650,0), PNG + "Aura2_P2.png"))
    return lista  
    
  def Abre_Sprites(PERSONAGEM,qual):   # x = anchor x, y = anchor y, qual= qual funcao executar
    lista=[]
    def Parado_Direita(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Parado_Direita/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Parado_Direita/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Parado_Direita/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Parado_Direita/4.png"))
      return lista
       
    def Parado_Esquerda(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Parado_Esquerda/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Parado_Esquerda/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Parado_Esquerda/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Parado_Esquerda/4.png"))
      return lista
      
    def Move_Direita(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Move_Direita/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Move_Direita/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Move_Direita/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Move_Direita/4.png"))
      return lista
      
    def Move_Esquerda(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Move_Esquerda/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Move_Esquerda/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Move_Esquerda/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Move_Esquerda/4.png"))
      return lista
    
    def Pulo_Direita(PERSONAGEM,lista):     
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Pulo_Direita/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Pulo_Direita/2.png"))
      return lista
      
    def Pulo_Esquerda(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Pulo_Esquerda/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Pulo_Esquerda/2.png"))
      return lista
    
    def Soco_Direita(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita/4.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita/5.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita/6.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita/7.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita/8.png"))
      return lista
      
    def Soco_Esquerda(PERSONAGEM,lista):  
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda/4.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda/5.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda/6.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda/7.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda/8.png"))
      return lista
    
    def Soco_Direita_Carregado(PERSONAGEM,lista):  
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita_Carregado/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita_Carregado/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita_Carregado/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita_Carregado/4.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Direita_Carregado/5.png"))
      return lista
      
    def Soco_Esquerda_Carregado(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda_Carregado/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda_Carregado/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda_Carregado/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda_Carregado/4.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Soco_Esquerda_Carregado/5.png"))
      return lista
      
    def Habilidade_Direita(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/4.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/5.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/6.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/7.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/8.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/9.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/10.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/K1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/K2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/K3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/K4.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/K5.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/K6.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Direita/K7.png"))
      return lista
      
    def Habilidade_Esquerda(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/4.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/5.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/6.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/7.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/8.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/9.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/10.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/K1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/K2.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/K3.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/K4.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/K5.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/K6.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Habilidade_Esquerda/K7.png"))
      return lista
    
    def Golpeado_Direita(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Golpeado_Direita/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Golpeado_Direita/2.png"))
      return lista
      
    def Golpeado_Esquerda(PERSONAGEM,lista):
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Golpeado_Esquerda/1.png"))
      lista.append(Image(Point(0,0),"Imagens/Sprites/" + str(PERSONAGEM) + "Golpeado_Esquerda/2.png"))
      return lista
    

       
    if (qual==0):
      lista = Parado_Direita(PERSONAGEM,lista)
    elif (qual==1):
      lista = Parado_Esquerda(PERSONAGEM,lista)
    elif (qual==2):
      lista = Move_Direita(PERSONAGEM,lista)   
    elif (qual==3):
      lista = Move_Esquerda(PERSONAGEM,lista)   
    elif (qual==4):
      lista = Pulo_Direita(PERSONAGEM,lista)  
    elif (qual==5):
      lista = Pulo_Esquerda(PERSONAGEM,lista)
    elif (qual==6):
      lista = Soco_Direita(PERSONAGEM,lista)  
    elif (qual==7):
      lista = Soco_Esquerda(PERSONAGEM,lista)   
    elif (qual==8):
      lista = Soco_Direita_Carregado(PERSONAGEM,lista)   
    elif (qual==9):
      lista = Soco_Esquerda_Carregado(PERSONAGEM,lista)
    elif (qual==10):
      lista = Habilidade_Direita(PERSONAGEM,lista)   
    elif (qual==11):
      lista = Habilidade_Esquerda(PERSONAGEM,lista)
    elif (qual==12):
      lista = Golpeado_Direita(PERSONAGEM,lista)   
    elif (qual==13):
      lista = Golpeado_Esquerda(PERSONAGEM,lista)     

    return lista

  P1 = info[3]
  P2 = info[4]
  mapa.draw(janela)
  info[0].draw(janela)        #Desenha as informaçoes
  info[1].draw(janela)        #Desenha a foto dos bonecos selecionados na direita e esquerda#
  info[2].draw(janela)        ###############################################################
  
  VIDA_P1 = Text(Point(-350,320),str(Z[0]) + " X")
  VIDA_P1.setSize(32) 
  VIDA_P1.setFill("white")                           ###DESENHA AS VIDAS
  VIDA_P1.draw(janela)
  
  Dano_P1 = Text(Point(-350,265),"0 %")            ###DESENHA AS VIDAS
  Dano_P1.setSize(32)
  Dano_P1.setFill("white") 
  Dano_P1.draw(janela)
  
  VIDA_P2 = Text(Point(580,320),str(Z[0]) + " X")    ###DESENHA O DANO
  VIDA_P2.setSize(32)
  VIDA_P2.setFill("white") 
  VIDA_P2.draw(janela)
  
  Dano_P2 = Text(Point(580,265),"0 %")             ###DESENHA O DANO
  Dano_P2.setSize(32)
  Dano_P2.setFill("white") 
  Dano_P2.draw(janela)
   
  VIDAS_P1 = Z[0]
  VIDAS_P2 = Z[0]
  MULTIPLICADOR = Z[1]
  
  update()
  
  MoveX = 3             ## 
  velocidadeX = 3       ##
  efeitos=efeitos()     ##  Variaveis para ambos os PLAYERS
  efeitos2=efeitos2()   ##
  contPAUSE=0           ##     
  contadorGLOBAL=0      ##
  contSOCO_P1=0         ##
  contSOCO_P2=0         ##  
  A1=-487
  B1=440


  lado_P1  = "direita"      ##  
  X_P1 = 0                  ##
  X2_P1=0                   ##
  ALTURA_P1=1.7             ##
  PULO_P1=False             ##  VARIAVEIS_P1
  FORA_DA_TELA_P1=False     ##
  FORAX_P1=0.5              ##
  contEFEITO_P1=0           ##
  MORTO_P1=False            ##
  AGUARDE_P1=False          ##
  contAGUARDE_P1=0          ##
  APAGAR_P1=[]              ##
  APAGAR_EFEITOS_P1=[]      ##
  X3_P1=0                   ##
  SOCO_P1=False             ##
  X4_P1=14                  ##
  SOCO_CARREGADO_P1=False   ##
  SOCO_NORMAL_P1=False      ##
  X5_P1=0                   ##
  X6_P1=0                   ##
  UM_SOCO_P1=False          ##
  SOQUE_P1=False            ##
  DANO_P1=0                 ##
  GOLPEADO_DIREITA_P1=False ##
  GOLPEADO_ESQUERDA_P1=False##
  contHIT_P1=0              ##
  PARAMETRO_P1=1.5          ##
  HABILIDADE_P1=False       ##
  X7_P1=0                   ##
  COLISAO_P1=False          ##
  APAGAR_HABILIDADE_P1=[]   ##
  contHAB_P1=0              ##
  X8_P1=0                   ##
  HITBOX_DIREITA_P1=False   ## 
  HITBOX_ESQUERDA_P1=False  ##
  PODER_P1=False            ##
  lado_atual_P1="direita"   ## 


  lado_P2  = "esquerda"     ##  
  X_P2 = 0                  ##
  X2_P2=0                   ##
  ALTURA_P2=1.7             ##
  PULO_P2=False             ##  VARIAVEIS_P2
  FORA_DA_TELA_P2=False     ##
  FORAX_P2=0.5              ##
  contEFEITO_P2=0           ##
  MORTO_P2=False            ##
  AGUARDE_P2=False          ##
  contAGUARDE_P2=0          ##
  APAGAR_P2=[]              ##
  APAGAR_EFEITOS_P2=[]      ##
  X3_P2=0                   ##
  SOCO_P2=False             ##
  X4_P2=14                  ##
  SOCO_CARREGADO_P2=False   ##
  SOCO_NORMAL_P2=False      ##
  X5_P2=0                   ##
  X6_P2=0                   ##  
  UM_SOCO_P2=False          ##
  SOQUE_P2=False            ##
  DANO_P2=0                 ##
  GOLPEADO_DIREITA_P2=False ##
  GOLPEADO_ESQUERDA_P2=False##
  contHIT_P2=0              ##
  PARAMETRO_P2=1.5          ##
  HABILIDADE_P2=False       ##
  X7_P2=0                   ##
  COLISAO_P2=False          ##
  APAGAR_HABILIDADE_P2=[]   ##
  contHAB_P2=0              ##
  X8_P2=0                   ##
  HITBOX_DIREITA_P2=False   ##
  HITBOX_ESQUERDA_P2=False  ##
  PODER_P2=False            ##   
  lado_atual_P2="direita"   ##
   

  vai3 = Image(Point(0,0), "Imagens/Efeitos_jogo/3.png")
  vai2 = Image(Point(0,0), "Imagens/Efeitos_jogo/2.png")
  vai1 = Image(Point(0,0), "Imagens/Efeitos_jogo/1.png")
  GO = Image(Point(0,0), "Imagens/Efeitos_jogo/GO.png")
  
  musica.play(-1)#############################################################################################
   
  Parado_Direita_P1 =                 Abre_Sprites(P1,0)
  Parado_Esquerda_P1 =                Abre_Sprites(P1,1)
  Move_Direita_P1 =                   Abre_Sprites(P1,2)   
  Move_Esquerda_P1 =                  Abre_Sprites(P1,3)  
  Pulo_Direita_P1 =                   Abre_Sprites(P1,4)  
  Pulo_Esquerda_P1 =                  Abre_Sprites(P1,5)
  Soco_Direita_P1 =                   Abre_Sprites(P1,6)  
  Soco_Esquerda_P1 =                  Abre_Sprites(P1,7) 
  Soco_Direita_Carregado_P1 =         Abre_Sprites(P1,8)   
  Soco_Esquerda_Carregado_P1 =        Abre_Sprites(P1,9)
  Habilidade_Direita_P1 =             Abre_Sprites(P1,10)   
  Habilidade_Esquerda_P1 =             Abre_Sprites(P1,11)
  Golpeado_Direita_P1 =               Abre_Sprites(P1,12)   
  Golpeado_Esquerda_P1 =              Abre_Sprites(P1,13) 
   

  Parado_Direita_P2 =                 Abre_Sprites(P2,0)
  Parado_Esquerda_P2 =                Abre_Sprites(P2,1)
  Move_Direita_P2 =                   Abre_Sprites(P2,2)   
  Move_Esquerda_P2 =                  Abre_Sprites(P2,3)  
  Pulo_Direita_P2 =                   Abre_Sprites(P2,4)  
  Pulo_Esquerda_P2 =                  Abre_Sprites(P2,5)
  Soco_Direita_P2 =                   Abre_Sprites(P2,6)  
  Soco_Esquerda_P2 =                  Abre_Sprites(P2,7) 
  Soco_Direita_Carregado_P2 =         Abre_Sprites(P2,8)   
  Soco_Esquerda_Carregado_P2 =        Abre_Sprites(P2,9)
  Habilidade_Direita_P2 =             Abre_Sprites(P2,10)   
  Habilidade_Esquerda_P2 =             Abre_Sprites(P2,11)
  Golpeado_Direita_P2 =               Abre_Sprites(P2,12)   
  Golpeado_Esquerda_P2 =              Abre_Sprites(P2,13) 

  Parado_Direita_P1[0].draw(janela)         ##
  Parado_Direita_P1[0].move(-450,-265)      ##  POSICAO INICIAL_P1     
  PosicaoX_P1 , PosicaoY_P1 = -450 , -265   ##
  APAGAR_P1.append(Parado_Direita_P1[0])    ##


  Parado_Esquerda_P2[0].draw(janela)        ##
  Parado_Esquerda_P2[0].move(450,-265)      ##  POSICAO INICIAL_P2     
  PosicaoX_P2 , PosicaoY_P2 = 450 , -265    ##
  APAGAR_P2.append(Parado_Esquerda_P2[0])   ##
  
  ESPECIAL1= Rectangle(Point(-487,227),Point(A1,210))
  ESPECIAL1.setOutline("deep sky blue") 
  ESPECIAL1.setFill("deep sky blue")
  ESPECIAL2= Rectangle(Point(440,227),Point(B1,210))
  ESPECIAL2.setOutline("deep sky blue")
  ESPECIAL2.setFill("deep sky blue")
  ESPECIAL1.draw(janela) 
  ESPECIAL2.draw(janela)
  X3 = (0.507614213 * (A1+487))
  X4 = (0.507614213 * (B1-440))
  X3=int(math.ceil(X3))
  X4=int(math.ceil(X4))
  A = Text(Point(-389,218), str(X3) + "%")
  B = Text(Point(538,218), str(X4) + "%")
  A.draw(janela)
  B.draw(janela)
  update()
 


  vai3.draw(janela)
  TRES.play()
  update()
  time.sleep(1)
  vai3.undraw()
  vai2.draw(janela)
  DOIS.play()
  update()
  time.sleep(1)
  vai2.undraw()
  vai1.draw(janela)
  UM.play()
  update()
  time.sleep(1)
  vai1.undraw()
  GO.draw(janela)
  GOO.play()
  update()
  time.sleep(1)
  GO.undraw()
  del TRES
  del DOIS
  del UM
  del GOO
  
  if (P1=="Goku/") or (P1=="Majin_boo/") or (P1=="Freeza/"):
    FATOR_DO_P1=0.657
    MAXIMO_P1=300
  if (P1=="Vegeta/"):
    FATOR_DO_P1=1.315
    MAXIMO_P1=150
  if (P2=="Itachi/") or (P2=="Sasuke/") or (P2=="Madara/"):
    FATOR_DO_P2=1.315
    MAXIMO_P2=150
  if (P2=="Naruto/"):
    FATOR_DO_P2=1.315
    MAXIMO_P2=150
  
  while 1:
    contadorGLOBAL+=1
    contHAB_P1+=1
    contHAB_P2+=1
    starttime = datetime.datetime.now()
    
    def apagar_sprites_P1(APAGAR):
      if (APAGAR!=[]):
        APAGAR[0].undraw()
        del APAGAR[0]
        
    def apagar_sprites_P2(APAGAR):
      if (APAGAR!=[]):
        APAGAR[0].undraw()
        del APAGAR[0]
    
    def apagar_efeitos_P1(APAGAR):
      if (APAGAR!=[]):
        APAGAR[0].undraw()
        del APAGAR[0]
    
    def apagar_efeitos_P2(APAGAR):
      if (APAGAR!=[]):
        APAGAR[0].undraw()
        del APAGAR[0]  
    
    def apagar_habilidade_P1(APAGAR):
      if (APAGAR!=[]):
        APAGAR[0].undraw()
        del APAGAR[0]
    
    def apagar_habilidade_P2(APAGAR):
      if (APAGAR!=[]):
        APAGAR[0].undraw()
        del APAGAR[0]
        
    update()
    apagar_sprites_P1(APAGAR_P1)
    apagar_sprites_P2(APAGAR_P2)
    apagar_efeitos_P1(APAGAR_EFEITOS_P1)
    apagar_efeitos_P1(APAGAR_EFEITOS_P2)
    apagar_habilidade_P1(APAGAR_HABILIDADE_P1)
    apagar_habilidade_P2(APAGAR_HABILIDADE_P2)
    teclas =janela.checkKey_Buffer()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  ############################################ --- MOVIMENTACAO_P1 --- ################################################## 

    if ((("d" not in teclas) and ("a" not in teclas)) or (("a" in teclas) and ("d" in teclas))) and (lado_P1=="direita"): #Parado para Direita
      Parado_Direita_P1[X_P1].draw(janela) 
      anchor_P1 = Parado_Direita_P1[X_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Parado_Direita_P1[X_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      APAGAR_P1.append(Parado_Direita_P1[X_P1])  
      if (contadorGLOBAL%45)==1:
        X_P1+=1
        if (X_P1==len(Parado_Direita_P1)):
          X_P1=0               
            
    elif ((("d" not in teclas) and ("a" not in teclas)) or (("a" in teclas) and ("d" in teclas))) and (lado_P1=="esquerda"):#Parado para Esquerda                
      Parado_Esquerda_P1[X_P1].draw(janela) 
      anchor_P1 = Parado_Esquerda_P1[X_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Parado_Esquerda_P1[X_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      APAGAR_P1.append(Parado_Esquerda_P1[X_P1])        
      if (contadorGLOBAL%45)==1:
        X_P1+=1
        if (X_P1==len(Parado_Esquerda_P1)):
          X_P1=0
          

    elif ("d" in teclas) and (AGUARDE_P1==False) and (SOCO_P1==False) and (SOCO_CARREGADO_P1==False)  and (GOLPEADO_DIREITA_P1==False) and (GOLPEADO_ESQUERDA_P1==False) and (GOLPEADO_DIREITA_P1==False) and (MORTO_P1==False) and (COLISAO_P1==False) and (HABILIDADE_P1==False): #Move para Direita
      lado_P1="direita"  
      Move_Direita_P1[X_P1].draw(janela) 
      anchor_P1 = Move_Direita_P1[X_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Move_Direita_P1[X_P1].move( PosicaoX_P1 + MoveX - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      PosicaoX_P1+=MoveX
      APAGAR_P1.append(Move_Direita_P1[X_P1])
      if (contadorGLOBAL%45)==1:
        X_P1+=1
        if (X_P1==len(Move_Direita_P1)):
          X_P1=0          
          
    elif ("a" in teclas) and (AGUARDE_P1==False) and (SOCO_P1==False) and (SOCO_CARREGADO_P1==False) and (GOLPEADO_DIREITA_P1==False) and (GOLPEADO_ESQUERDA_P1==False) and (GOLPEADO_DIREITA_P1==False) and (MORTO_P1==False) and (COLISAO_P1==False) and (HABILIDADE_P1==False): #Move para Esquerda
      lado_P1="esquerda"
      Move_Esquerda_P1[X_P1].draw(janela) 
      anchor_P1 = Move_Esquerda_P1[X_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Move_Esquerda_P1[X_P1].move( PosicaoX_P1 - MoveX - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      PosicaoX_P1-=MoveX
      APAGAR_P1.append(Move_Esquerda_P1[X_P1])
      if (contadorGLOBAL%45)==1:
        X_P1+=1
        if (X_P1==len(Move_Esquerda_P1)):
          X_P1=0         

  ##################################################### --- PULO_P1 --- ################################################    
   
    if ("w" in teclas) and (SOCO_P1==False) and (SOCO_CARREGADO_P1==False) and (SOCO_NORMAL_P1==False) and (GOLPEADO_ESQUERDA_P1==False) and (GOLPEADO_DIREITA_P1==False) and (COLISAO_P1==False) and (HABILIDADE_P1==False): #PULO     
      if (PULO_P1==False):
        PULO_P1=True
        ALTURA_P1=1.7
        UM_SOCO_P1=True
    if (PULO_P1==True) and (lado_P1=="direita"):
      if ("v" in teclas) and (UM_SOCO_P1==True):
        SOQUE_P1=True
        UM_SOCO_P1=False
      apagar_sprites_P1(APAGAR_P1)
      Pulo_Direita_P1[X2_P1].draw(janela)
      anchor_P1 =  Pulo_Direita_P1[X2_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Pulo_Direita_P1[X2_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      if (contadorGLOBAL%3==1): 
        ALTURA_P1-=0.06
        MoveY_P1= 9*(ALTURA_P1**2)
        if (ALTURA_P1<=0):
          MoveY_P1=-MoveY_P1  
        Pulo_Direita_P1[X2_P1].move( 0 , MoveY_P1 )
        PosicaoY_P1 = PosicaoY_P1 + MoveY_P1
        if ("a" in teclas): 
          lado_P1="esquerda"
          Pulo_Direita_P1[X2_P1].move(-MoveX,0)
        if ("d" in teclas): 
          lado_P1="direita"
          Pulo_Direita_P1[X2_P1].move(MoveX,0)   
      APAGAR_P1.append(Pulo_Direita_P1[X2_P1])     
      if (PosicaoY_P1<=-264.9):
        PosicaoY_P1=-265
        ALTURA_P1=1.7
        PULO_P1=False
        X2_P1=0

    if (PULO_P1==True) and (lado_P1=="esquerda"):
      if ("v" in teclas) and (UM_SOCO_P1==True):
        SOQUE_P1=True
        UM_SOCO_P1=False
      apagar_sprites_P1(APAGAR_P1)
      Pulo_Esquerda_P1[X2_P1].draw(janela)
      anchor_P1 =  Pulo_Esquerda_P1[X2_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Pulo_Esquerda_P1[X2_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      if (contadorGLOBAL%3==1): 
        ALTURA_P1-=0.06
        MoveY_P1= 9*(ALTURA_P1**2)
        if (ALTURA_P1<=0):
          MoveY_P1=-MoveY_P1  
        Pulo_Esquerda_P1[X2_P1].move( 0 , MoveY_P1 )
        PosicaoY_P1 = PosicaoY_P1 + MoveY_P1
        if ("a" in teclas): 
          lado_P1="esquerda"
          Pulo_Esquerda_P1[X2_P1].move(-MoveX,0)  
        if ("d" in teclas): 
          lado_P1="direita"
          Pulo_Esquerda_P1[X2_P1].move(MoveX,0)     
      APAGAR_P1.append(Pulo_Esquerda_P1[X2_P1])     
      if (PosicaoY_P1<=-264.9):
        PosicaoY_P1=-265
        ALTURA_P1=1.7
        PULO_P1=False
        X2_P1=0      
              
    if (ALTURA_P1<-0.4):
      X2_P1=1
      
  #################################################### --- SOCO_P1 --- ##############################################  

    if ("v" in teclas) and (PULO_P1==False) and (GOLPEADO_DIREITA_P1==False) and (GOLPEADO_ESQUERDA_P1==False) and (COLISAO_P1==False) and (HABILIDADE_P1==False): 
      if (SOCO_P1==False):  
        SOCO_P1=True
        contSOCO_P1=0
    if (SOCO_P1==True) and (lado_P1=="direita"): 
      if ("v" in teclas): 
        contSOCO_P1+=1
      apagar_sprites_P1(APAGAR_P1)    
      Soco_Direita_P1[X3_P1].draw(janela)
      XX = Soco_Direita_P1[X3_P1].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Direita_P1[X3_P1].move(PosicaoX_P1 - Xx , PosicaoY_P1 - Yy) 
      APAGAR_P1.append(Soco_Direita_P1[X3_P1])
      if (contSOCO_P1>150):
        efeitos[X4_P1].draw(janela)
        XX = efeitos[X4_P1].getAnchor()
        Xx = XX.getX()
        Yy = XX.getY()
        efeitos[X4_P1].move(PosicaoX_P1 - Xx -20 , PosicaoY_P1 - Yy + 20) 
        APAGAR_EFEITOS_P1.append(efeitos[X4_P1])
        if (contadorGLOBAL%20==1):
          X4_P1+=1
          if (X4_P1==16):
            X4_P1=14
            
    if (SOCO_P1==True) and (lado_P1=="esquerda"): 
      if ("v" in teclas): 
        contSOCO_P1+=1
      apagar_sprites_P1(APAGAR_P1)    
      Soco_Esquerda_P1[X3_P1].draw(janela)
      XX = Soco_Esquerda_P1[X3_P1].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Esquerda_P1[X3_P1].move(PosicaoX_P1 - Xx , PosicaoY_P1 - Yy) 
      APAGAR_P1.append(Soco_Esquerda_P1[X3_P1])
      if (contSOCO_P1>150):
        efeitos[X4_P1].draw(janela)
        XX = efeitos[X4_P1].getAnchor()
        Xx = XX.getX()
        Yy = XX.getY()
        efeitos[X4_P1].move(PosicaoX_P1 - Xx, PosicaoY_P1 - Yy + 20) 
        APAGAR_EFEITOS_P1.append(efeitos[X4_P1])
        if (contadorGLOBAL%20==1):
          X4_P1+=1
          if (X4_P1==16):
            X4_P1=14


    if ("v" not in teclas) and (SOCO_P1==True):
      SOCO_P1=False
      if (contSOCO_P1>150):
        contSOCO_P1=420
        SOCO_CARREGADO_P1=True
      else:
        SOCO_NORMAL_P1=True
        
    if (SOCO_CARREGADO_P1==True) and (lado_P1=="direita"):
      apagar_sprites_P1(APAGAR_P1)
      Soco_Direita_Carregado_P1[X5_P1].draw(janela)
      XX = Soco_Direita_Carregado_P1[X5_P1].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Direita_Carregado_P1[X5_P1].move(PosicaoX_P1 - Xx, PosicaoY_P1 - Yy)   
      APAGAR_P1.append(Soco_Direita_Carregado_P1[X5_P1]) 
      if (contadorGLOBAL%14==1):
        X5_P1+=1
        if (X5_P1==5):
          X5_P1=0
          SOCO_CARREGADO_P1=False


    if (SOCO_CARREGADO_P1==True) and (lado_P1=="esquerda"):
      apagar_sprites_P1(APAGAR_P1)
      Soco_Esquerda_Carregado_P1[X5_P1].draw(janela)
      XX = Soco_Esquerda_Carregado_P1[X5_P1].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Esquerda_Carregado_P1[X5_P1].move(PosicaoX_P1 - Xx, PosicaoY_P1 - Yy)   
      APAGAR_P1.append(Soco_Esquerda_Carregado_P1[X5_P1]) 
      if (contadorGLOBAL%14==1):
        X5_P1+=1
        if (X5_P1==5):
          X5_P1=0
          SOCO_CARREGADO_P1=False

    
    elif ((SOCO_NORMAL_P1==True) or (SOQUE_P1==True)) and (lado_P1=="direita"):      
      apagar_sprites_P1(APAGAR_P1)
      Soco_Direita_P1[X6_P1].draw(janela)
      XX = Soco_Direita_P1[X6_P1].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Direita_P1[X6_P1].move(PosicaoX_P1 - Xx, PosicaoY_P1 - Yy)   
      APAGAR_P1.append(Soco_Direita_P1[X6_P1]) 
      if (contadorGLOBAL%14==1):
        X6_P1+=1
        if (X6_P1==4) or (X6_P1==8):
          SOCO_NORMAL_P1=False
          SOQUE_P1=False   
          if (X6_P1==8):
            X6_P1=0                               
          
    elif ((SOCO_NORMAL_P1==True) or (SOQUE_P1==True)) and (lado_P1=="esquerda"):
      apagar_sprites_P1(APAGAR_P1)
      Soco_Esquerda_P1[X6_P1].draw(janela)
      XX = Soco_Esquerda_P1[X6_P1].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Esquerda_P1[X6_P1].move(PosicaoX_P1 - Xx, PosicaoY_P1 - Yy)   
      APAGAR_P1.append(Soco_Esquerda_P1[X6_P1]) 
      if (contadorGLOBAL%14==1):
        X6_P1+=1
        if (X6_P1==4) or (X6_P1==8):
          SOCO_NORMAL_P1=False
          SOQUE_P1=False
          if (X6_P1==8):
            X6_P1=0

  #################################################### --- colisao_P1 --- ############################################ 

    if  ((SOCO_NORMAL_P1==True) or (SOQUE_P1==True)) and (lado_P1=="direita"):
      if (((PosicaoX_P1-20)<=(PosicaoX_P2) and ((PosicaoX_P2-PosicaoX_P1)<=92)) and ((PosicaoY_P2-PosicaoY_P1)<90 and (PosicaoY_P2-PosicaoY_P1)>-55)):                                
        GOLPEADO_DIREITA_P2=True               
        contSOCO_P2=0
        
    if  ((SOCO_NORMAL_P1==True) or (SOQUE_P1==True)) and (lado_P1=="esquerda"):
      if (((PosicaoX_P1+20)>=(PosicaoX_P2) and ((PosicaoX_P2-PosicaoX_P1)>=-92)) and ((PosicaoY_P2-PosicaoY_P1)<90 and (PosicaoY_P2-PosicaoY_P1)>-55)):                                    
        GOLPEADO_ESQUERDA_P2=True
        contSOCO_P2=0
        
    if  (SOCO_CARREGADO_P1==True)  and (lado_P1=="direita"):
      if (((PosicaoX_P1-40)<=(PosicaoX_P2) and ((PosicaoX_P2-PosicaoX_P1)<=100)) and ((PosicaoY_P2-PosicaoY_P1)<90 and (PosicaoY_P2-PosicaoY_P1)>-85)):                                    
        GOLPEADO_DIREITA_P2=True
        contSOCO_P2=0
      
    if  (SOCO_CARREGADO_P1==True) and (lado_P1=="esquerda"):
      if (((PosicaoX_P1+40)>=(PosicaoX_P2) and ((PosicaoX_P2-PosicaoX_P1)>=-100)) and ((PosicaoY_P2-PosicaoY_P1)<90 and (PosicaoY_P2-PosicaoY_P1)>-85)):                                    
        GOLPEADO_ESQUERDA_P2=True
        contSOCO_P2=0
        
  ###################################################### --- FORA_DA_TELA_P1 --- ######################################

    if (MORTO_P1==True):
      if(FORA_P1!=None):
        FORA_P1.undraw() 
     
    if (PosicaoX_P1<-680) or (PosicaoX_P1>680):
      if (FORA_DA_TELA_P1==False) and (PosicaoX_P1<-650):
        FORA_DA_TELA_P1=True
        FORA_P1 = Image(Point(-580,PosicaoY_P1),"Imagens/Efeitos_jogo/P1_Esquerda.png")
        FORA_P1.draw(janela)
      elif (FORA_DA_TELA_P1==False) and (PosicaoX_P1>650):
        FORA_DA_TELA_P1=True
        FORA_P1 = Image(Point(580,PosicaoX_P1),"Imagens/Efeitos_jogo/P1_Direita.png")
        FORA_P1.draw(janela)
    if (FORA_DA_TELA_P1==True) and ((PosicaoX_P1>680) or (PosicaoX_P1<-680)):  
      FORAY_P1=FORA_P1.getAnchor()
      FORAY_P1=FORAY_P1.getY()
      FORA_P1.move(FORAX_P1,PosicaoY_P1 - FORAY_P1)
      if (contadorGLOBAL%60==1):
        FORAX_P1=-FORAX_P1
    elif (FORA_DA_TELA_P1==True) and (PosicaoX_P1<680) and (PosicaoX_P1>-680):
      FORA_DA_TELA_P1=False
      if (FORA_P1!=None):
        FORA_P1.undraw()
        
  ###################################################### --- MORTO_P1 --- ############################################
    
    if (PosicaoX_P1<-1000) or (PosicaoX_P1>1000):
      if (MORTO_P1==False):
        MORTO_P1=True
        DANO_P1=0 ##########################################################
        Y_MORTO_P1 = PosicaoY_P1
        
    if (MORTO_P1==True) and (PosicaoX_P1<-1000) and (AGUARDE_P1==False):
      efeitos[contEFEITO_P1].draw(janela)
      YY_P1 = efeitos[contEFEITO_P1].getAnchor()
      YYY_P1 = YY_P1.getY()
      efeitos[contEFEITO_P1].move(0,Y_MORTO_P1 - YYY_P1)   
      APAGAR_EFEITOS_P1.append(efeitos[contEFEITO_P1])   
      if (contadorGLOBAL%15==1):
        contEFEITO_P1+=1
        if (contEFEITO_P1>=6):
          MORTO_P1=False
          AGUARDE_P1=True
          contEFEITO_P1=0    
          VIDAS_P1-=1
          
    elif (MORTO_P1==True) and (PosicaoX_P1>1000) and (AGUARDE_P1==False):
      efeitos[7 + contEFEITO_P1].draw(janela)
      YY_P1 = efeitos[7 + contEFEITO_P1].getAnchor()
      YYY_P1 = YY_P1.getY()
      efeitos[7 + contEFEITO_P1].move(0,Y_MORTO_P1 - YYY_P1)    
      APAGAR_EFEITOS_P1.append(efeitos[7 + contEFEITO_P1])   
      if (contadorGLOBAL%15==1):
        contEFEITO_P1+=1
        if (contEFEITO_P1>=6):
          MORTO_P1=False
          AGUARDE_P1=True
          contEFEITO_P1=0
          VIDAS_P1-=1
          
    if (AGUARDE_P1==True):
      contAGUARDE_P1+=1
      if (contAGUARDE_P1>500):
        MORTO_P1=False
        contAGUARDE_P1=0
        PosicaoX_P1=-300
        PosicaoY_P1=-265
        lado_P1="direita"
        AGUARDE_P1=False  

  ################################################################################################################# 
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        
   
  #################################################### --- MOVIMENTACAO_P2 --- #######################################

    if ((("Right" not in teclas) and ("Left" not in teclas)) or (("Right" in teclas) and ("Left" in teclas))) and (lado_P2=="direita"): #Parado para Direita  
      Parado_Direita_P2[X_P2].draw(janela) 
      anchor_P2 = Parado_Direita_P2[X_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Parado_Direita_P2[X_P2].move( PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )
      APAGAR_P2.append(Parado_Direita_P2[X_P2])  
      if (contadorGLOBAL%45)==1:
        X_P2+=1
        if (X_P2==len(Parado_Direita_P2)):
          X_P2=0
                       
    elif ((("Right" not in teclas) and ("Left" not in teclas)) or (("Right" in teclas) and ("Left" in teclas))) and (lado_P2=="esquerda"):#Parado para Esquerda                 
      Parado_Esquerda_P2[X_P2].draw(janela) 
      anchor_P2 = Parado_Esquerda_P2[X_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Parado_Esquerda_P2[X_P2].move( PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )
      APAGAR_P2.append(Parado_Esquerda_P2[X_P2])        
      if (contadorGLOBAL%45)==1:
        X_P2+=1
        if (X_P2==len(Parado_Esquerda_P2)):
          X_P2=0  


    elif ("Right" in teclas) and (AGUARDE_P2==False) and (SOCO_P2==False) and (SOCO_CARREGADO_P2==False) and (GOLPEADO_ESQUERDA_P2==False) and (GOLPEADO_DIREITA_P2==False) and (MORTO_P2==False) and (HABILIDADE_P2==False): #Move para Direita
      lado_P2="direita" 
      Move_Direita_P2[X_P2].draw(janela) 
      anchor_P2 = Move_Direita_P2[X_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Move_Direita_P2[X_P2].move( PosicaoX_P2 + MoveX - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )
      PosicaoX_P2+=MoveX
      APAGAR_P2.append(Move_Direita_P2[X_P2])
      if (contadorGLOBAL%45)==1:
        X_P2+=1
        if (X_P2==len(Move_Direita_P2)):
          X_P2=0 
               
    elif ("Left" in teclas) and (AGUARDE_P2==False) and (SOCO_P2==False) and (SOCO_CARREGADO_P2==False) and (GOLPEADO_ESQUERDA_P2==False) and (GOLPEADO_DIREITA_P2==False) and (MORTO_P2==False) and (HABILIDADE_P2==False): #Move para Esquerda
      lado_P2="esquerda"
      Move_Esquerda_P2[X_P2].draw(janela) 
      anchor_P2 = Move_Esquerda_P2[X_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Move_Esquerda_P2[X_P2].move( PosicaoX_P2 - MoveX - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )
      PosicaoX_P2-=MoveX
      APAGAR_P2.append(Move_Esquerda_P2[X_P2])
      if (contadorGLOBAL%45)==1:
        X_P2+=1
        if (X_P2==len(Move_Esquerda_P2)):
          X_P2=0 
           
  ##################################################### --- PULO_P2 --- ########################################## 

    if ("Up" in teclas) and (SOCO_P2==False) and (SOCO_CARREGADO_P2==False) and (SOCO_NORMAL_P2==False) and (GOLPEADO_ESQUERDA_P2==False) and (GOLPEADO_DIREITA_P2==False) and (HABILIDADE_P2==False):  #PULO     
      if (PULO_P2==False):
        PULO_P2=True
        ALTURA_P2=1.7
        UM_SOCO_P2=True

    if (PULO_P2==True) and (lado_P2=="direita"):
      if ("p" in teclas) and (UM_SOCO_P2==True):
        SOQUE_P2=True
        UM_SOCO_P2=False
      apagar_sprites_P2(APAGAR_P2)
      Pulo_Direita_P2[X2_P2].draw(janela)
      anchor_P2 =  Pulo_Direita_P2[X2_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Pulo_Direita_P2[X2_P2].move( PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )
      if (contadorGLOBAL%3==1): 
        ALTURA_P2-=0.06
        MoveY_P2= 9*(ALTURA_P2**2)
        if (ALTURA_P2<=0):
          MoveY_P2=-MoveY_P2  
        Pulo_Direita_P2[X2_P2].move( 0 , MoveY_P2 )
        PosicaoY_P2 = PosicaoY_P2 + MoveY_P2
        if ("Left" in teclas): 
          lado_P2="esquerda"
          Pulo_Direita_P2[X2_P2].move(-MoveX,0)
        if ("Right" in teclas): 
          lado_P2="direita"
          Pulo_Direita_P2[X2_P2].move(MoveX,0)    
      APAGAR_P2.append(Pulo_Direita_P2[X2_P2])     
      if (PosicaoY_P2<=-264.9):
        PosicaoY_P2=-265
        ALTURA_P2=1.5
        PULO_P2=False
        X2_P2=0

    if (PULO_P2==True) and (lado_P2=="esquerda"):
      if ("p" in teclas) and (UM_SOCO_P2==True):
        SOQUE_P2=True
        UM_SOCO_P2=False 
     
      apagar_sprites_P2(APAGAR_P2)
      Pulo_Esquerda_P2[X2_P2].draw(janela)
      anchor_P2 =  Pulo_Esquerda_P2[X2_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Pulo_Esquerda_P2[X2_P2].move( PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )
      if (contadorGLOBAL%3==1): 
        ALTURA_P2-=0.06
        MoveY_P2= 9*(ALTURA_P2**2)
        if (ALTURA_P2<=0):
          MoveY_P2=-MoveY_P2  
        Pulo_Esquerda_P2[X2_P2].move( 0 , MoveY_P2 )
        PosicaoY_P2 = PosicaoY_P2 + MoveY_P2
        if ("Left" in teclas): 
          lado_P2="esquerda"
          Pulo_Esquerda_P2[X2_P2].move(-MoveX,0)       
        if ("Right" in teclas): 
          lado_P2="direita"
          Pulo_Esquerda_P2[X2_P2].move(MoveX,0)    
      APAGAR_P2.append(Pulo_Esquerda_P2[X2_P2])     
      if (PosicaoY_P2<=-264.9):
        PosicaoY_P2=-265
        ALTURA_P2=1.7
        PULO_P2=False
        X2_P2=0      
            
    if (ALTURA_P2<-0.4):
      X2_P2=1
      
  #################################################### --- SOCO_P2 --- ############################################   
    
    if ("p" in teclas) and (PULO_P2==False) and (GOLPEADO_DIREITA_P2==False) and (GOLPEADO_ESQUERDA_P2==False): 
      if (SOCO_P2==False) and (HABILIDADE_P2==False):  
        SOCO_P2=True
        contSOCO_P2=0
    if (SOCO_P2==True) and (lado_P2=="direita"): 
      if ("p" in teclas): 
        contSOCO_P2+=1
      apagar_sprites_P2(APAGAR_P2)    
      Soco_Direita_P2[X3_P2].draw(janela)
      XX = Soco_Direita_P2[X3_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Direita_P2[X3_P2].move(PosicaoX_P2 - Xx , PosicaoY_P2 - Yy) 
      APAGAR_P2.append(Soco_Direita_P2[X3_P2])
      if (contSOCO_P2>150):
        efeitos2[X4_P2].draw(janela)
        XX = efeitos2[X4_P2].getAnchor()
        Xx = XX.getX()
        Yy = XX.getY()
        efeitos2[X4_P2].move(PosicaoX_P2 - Xx -20 , PosicaoY_P2 - Yy + 20) 
        APAGAR_EFEITOS_P2.append(efeitos2[X4_P2])
        if (contadorGLOBAL%20==1):
          X4_P2+=1
          if (X4_P2==16):
            X4_P2=14
            
    if (SOCO_P2==True) and (lado_P2=="esquerda"): 
      if ("p" in teclas): 
        contSOCO_P2+=1
      apagar_sprites_P2(APAGAR_P2)    
      Soco_Esquerda_P2[X3_P2].draw(janela)
      XX = Soco_Esquerda_P2[X3_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Esquerda_P2[X3_P2].move(PosicaoX_P2 - Xx , PosicaoY_P2 - Yy) 
      APAGAR_P2.append(Soco_Esquerda_P2[X3_P2])
      if (contSOCO_P2>150):
        efeitos2[X4_P2].draw(janela)
        XX = efeitos2[X4_P2].getAnchor()
        Xx = XX.getX()
        Yy = XX.getY()
        efeitos2[X4_P2].move(PosicaoX_P2 - Xx, PosicaoY_P2 - Yy + 20) 
        APAGAR_EFEITOS_P2.append(efeitos2[X4_P2])
        if (contadorGLOBAL%20==1):
          X4_P2+=1
          if (X4_P2==16):
            X4_P2=14


    if ("p" not in teclas) and (SOCO_P2==True):
      SOCO_P2=False
      if (contSOCO_P2>150):
        contSOCO_P2=420
        SOCO_CARREGADO_P2=True
      else:
        SOCO_NORMAL_P2=True
    
    if (SOCO_CARREGADO_P2==True) and (lado_P2=="direita"):
      apagar_sprites_P2(APAGAR_P2)
      Soco_Direita_Carregado_P2[X5_P2].draw(janela)
      XX = Soco_Direita_Carregado_P2[X5_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Direita_Carregado_P2[X5_P2].move(PosicaoX_P2 - Xx, PosicaoY_P2 - Yy)   
      APAGAR_P2.append(Soco_Direita_Carregado_P2[X5_P2]) 
      if (contadorGLOBAL%14==1):
        X5_P2+=1
        if (X5_P2==5):
          X5_P2=0
          SOCO_CARREGADO_P2=False

    if (SOCO_CARREGADO_P2==True) and (lado_P2=="esquerda"):
      apagar_sprites_P2(APAGAR_P2)
      Soco_Esquerda_Carregado_P2[X5_P2].draw(janela)
      XX = Soco_Esquerda_Carregado_P2[X5_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Esquerda_Carregado_P2[X5_P2].move(PosicaoX_P2 - Xx, PosicaoY_P2 - Yy)   
      APAGAR_P2.append(Soco_Esquerda_Carregado_P2[X5_P2]) 
      if (contadorGLOBAL%14==1):
        X5_P2+=1
        if (X5_P2==5):
          X5_P2=0
          SOCO_CARREGADO_P2=False
    
    elif (SOCO_NORMAL_P2==True) and (lado_P2=="direita"):
      apagar_sprites_P2(APAGAR_P2)
      Soco_Direita_P2[X6_P2].draw(janela)
      XX = Soco_Direita_P2[X6_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Direita_P2[X6_P2].move(PosicaoX_P2 - Xx, PosicaoY_P2 - Yy)   
      APAGAR_P2.append(Soco_Direita_P2[X6_P2]) 
      if (contadorGLOBAL%14==1):
        X6_P2+=1
        if (X6_P2==4) or (X6_P2==8):
          SOCO_NORMAL_P2=False
          if (X6_P2==8):
            X6_P2=0 
          
    elif (SOCO_NORMAL_P2==True) and (lado_P2=="esquerda"):
      apagar_sprites_P2(APAGAR_P2)
      Soco_Esquerda_P2[X6_P2].draw(janela)
      XX = Soco_Esquerda_P2[X6_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Esquerda_P2[X6_P2].move(PosicaoX_P2 - Xx, PosicaoY_P2 - Yy)   
      APAGAR_P2.append(Soco_Esquerda_P2[X6_P2]) 
      if (contadorGLOBAL%14==1):
        X6_P2+=1
        if (X6_P2==4) or (X6_P2==8):
          SOCO_NORMAL_P2=False
          if (X6_P2==8):
            X6_P2=0
      
      
    elif ((SOCO_NORMAL_P2==True) or (SOQUE_P2==True)) and (lado_P2=="direita"):
      apagar_sprites_P2(APAGAR_P2)
      Soco_Direita_P2[X6_P2].draw(janela)
      XX = Soco_Direita_P2[X6_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Direita_P2[X6_P2].move(PosicaoX_P2 - Xx, PosicaoY_P2 - Yy)   
      APAGAR_P2.append(Soco_Direita_P2[X6_P2]) 
      if (contadorGLOBAL%14==1):
        X6_P2+=1
        if (X6_P2==4) or (X6_P2==8): 
          SOCO_NORMAL_P2=False
          SOQUE_P2=False
          if (X6_P2==8):
            X6_P2=0 
          
    elif ((SOCO_NORMAL_P2==True) or (SOQUE_P2==True)) and (lado_P2=="esquerda"):
   
      apagar_sprites_P2(APAGAR_P2)
      Soco_Esquerda_P2[X6_P2].draw(janela)
      XX = Soco_Esquerda_P2[X6_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Soco_Esquerda_P2[X6_P2].move(PosicaoX_P2 - Xx, PosicaoY_P2 - Yy)   
      APAGAR_P2.append(Soco_Esquerda_P2[X6_P2]) 
      if (contadorGLOBAL%14==1):
        X6_P2+=1
        if (X6_P2==4) or (X6_P2==8):
          SOCO_NORMAL_P2=False
          SOQUE_P2=False
          if (X6_P2==8):
            X6_P2=0

  #################################################### --- colisao_P2 --- ########################################### 

    if  ((SOCO_NORMAL_P2==True) or (SOQUE_P2==True)) and (lado_P2=="direita"):
      if (((PosicaoX_P2-20)<=(PosicaoX_P1) and ((PosicaoX_P1-PosicaoX_P2)<=92)) and ((PosicaoY_P1-PosicaoY_P2)<90 and (PosicaoY_P1-PosicaoY_P2)>-55)):                                
        GOLPEADO_DIREITA_P1=True               
        contSOCO_P1=0
        
    if  ((SOCO_NORMAL_P2==True) or (SOQUE_P2==True)) and (lado_P2=="esquerda"):
      if (((PosicaoX_P2+20)>=(PosicaoX_P1) and ((PosicaoX_P1-PosicaoX_P2)>=-92)) and ((PosicaoY_P1-PosicaoY_P2)<90 and (PosicaoY_P1-PosicaoY_P2)>-55)):                                    
        GOLPEADO_ESQUERDA_P1=True
        contSOCO_P1=0
        
    if  (SOCO_CARREGADO_P2==True)  and (lado_P2=="direita"):
      if (((PosicaoX_P2-40)<=(PosicaoX_P1) and ((PosicaoX_P1-PosicaoX_P2)<=100)) and ((PosicaoY_P1-PosicaoY_P2)<90 and (PosicaoY_P1-PosicaoY_P2)>-85)):                                    
        GOLPEADO_DIREITA_P1=True
        contSOCO_P1=0
        
    if  (SOCO_CARREGADO_P2==True) and (lado_P2=="esquerda"):
      if (((PosicaoX_P2+40)>=(PosicaoX_P1) and ((PosicaoX_P1-PosicaoX_P2)>=-100)) and ((PosicaoY_P1-PosicaoY_P2)<90 and (PosicaoY_P1-PosicaoY_P2)>-85)):                                    
        GOLPEADO_ESQUERDA_P1=True
        contSOCO_P1=0
        
  ###################################################### --- FORA_DA_TELA_P2 --- ###################################
   
    if (MORTO_P2==True):
      if(FORA_P2!=None):
        FORA_P2.undraw() 
     
    if (PosicaoX_P2<-680) or (PosicaoX_P2>680):
      if (FORA_DA_TELA_P2==False) and (PosicaoX_P2<-650):
        FORA_DA_TELA_P2=True
        FORA_P2 = Image(Point(-580,PosicaoY_P2),"Imagens/Efeitos_jogo/P2_Esquerda.png")
        FORA_P2.draw(janela)
      elif (FORA_DA_TELA_P2==False) and (PosicaoX_P2>650):
        FORA_DA_TELA_P2=True
        FORA_P2 = Image(Point(580,PosicaoX_P2),"Imagens/Efeitos_jogo/P2_Direita.png")
        FORA_P2.draw(janela)
    if (FORA_DA_TELA_P2==True) and ((PosicaoX_P2>680) or (PosicaoX_P2<-680)):  
      FORAY_P2=FORA_P2.getAnchor()
      FORAY_P2=FORAY_P2.getY()
      FORA_P2.move(FORAX_P2,PosicaoY_P2 - FORAY_P2)
      if (contadorGLOBAL%60==1):
        FORAX_P2=-FORAX_P2
    elif (FORA_DA_TELA_P2==True) and (PosicaoX_P2<680) and (PosicaoX_P2>-680):
      FORA_DA_TELA_P2=False
      if (FORA_P2!=None):
        FORA_P2.undraw()
        
  ###################################################### --- MORTO_P2 --- ###########################################

    if (PosicaoX_P2<-1000) or (PosicaoX_P2>1000):
      if (MORTO_P2==False):
        MORTO_P2=True
        DANO_P2=0 ##########################################################
        Y_MORTO_P2 = PosicaoY_P2
        
    if (MORTO_P2==True) and (PosicaoX_P2<-1000) and (AGUARDE_P2==False):
      efeitos2[contEFEITO_P2].draw(janela)
      YY_P2 = efeitos2[contEFEITO_P2].getAnchor()
      YYY_P2 = YY_P2.getY()
      efeitos2[contEFEITO_P2].move(0,Y_MORTO_P2 - YYY_P2)   
      APAGAR_EFEITOS_P2.append(efeitos2[contEFEITO_P2])   
      if (contadorGLOBAL%15==1):
        contEFEITO_P2+=1
        if (contEFEITO_P2>=6):
          MORTO_P2=False
          AGUARDE_P2=True
          contEFEITO_P2=0    
          VIDAS_P2-=1
          
    elif (MORTO_P2==True) and (PosicaoX_P2>1000) and (AGUARDE_P2==False):
      efeitos2[7 + contEFEITO_P2].draw(janela)
      YY_P2 = efeitos2[7 + contEFEITO_P2].getAnchor()
      YYY_P2 = YY_P2.getY()
      efeitos2[7 + contEFEITO_P2].move(0,Y_MORTO_P2 - YYY_P2)    
      APAGAR_EFEITOS_P2.append(efeitos2[7 + contEFEITO_P2])   
      if (contadorGLOBAL%15==1):
        contEFEITO_P2+=1
        if (contEFEITO_P2>=7):
          MORTO_P2=False
          AGUARDE_P2=True
          contEFEITO_P2=0
          VIDAS_P2-=1
          
    if (AGUARDE_P2==True):
      contAGUARDE_P2+=1
      if (contAGUARDE_P2>500):
        MORTO_P2=False
        contAGUARDE_P2=0
        PosicaoX_P2=300
        PosicaoY_P2=-265
        lado_P2="esquerda"
        AGUARDE_P2=False
             
  ################################################################################################################
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  ################################## --- HABILIDADE P1 (Goku, Majin_Boo,Freeza) --- ###############################

    if ("b" in teclas) and (contHAB_P1>300) and (GOLPEADO_DIREITA_P1==False) and (GOLPEADO_ESQUERDA_P1==False) and (PULO_P1==False) and ((P1=="Goku/") or (P1=="Freeza/") or (P1=="Majin_boo/")) and (MORTO_P1==False):
      HABILIDADE_P1=True
      
    if (HABILIDADE_P1==True) and (COLISAO_P1==False) and (lado_P1=="direita") and (P1!="Vegeta/"): 
      apagar_sprites_P1(APAGAR_P1)
      Habilidade_Direita_P1[X7_P1].draw(janela) 
      anchor_P1 = Habilidade_Direita_P1[X7_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Direita_P1[X7_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      APAGAR_P1.append(Habilidade_Direita_P1[X7_P1])        
      if (contadorGLOBAL%12)==1:
        X7_P1+=1
        if (X7_P1==9):
          COLISAO_P1=True 
      
    if (HABILIDADE_P1==True) and (COLISAO_P1==False) and (lado_P1=="esquerda") and (P1!="Vegeta/"): 
      apagar_sprites_P1(APAGAR_P1)
      Habilidade_Esquerda_P1[X7_P1].draw(janela) 
      anchor_P1 = Habilidade_Esquerda_P1[X7_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Esquerda_P1[X7_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      APAGAR_P1.append(Habilidade_Esquerda_P1[X7_P1])        
      if (contadorGLOBAL%12)==1:
        X7_P1+=1
        if (X7_P1==9):
          COLISAO_P1=True
          
          
    
    if (COLISAO_P1==True) and (lado_P1=="esquerda") and (P1!="Vegeta/"):  
      apagar_sprites_P1(APAGAR_P1)
      Habilidade_Esquerda_P1[7].draw(janela) 
      anchor_P1 = Habilidade_Esquerda_P1[7].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Esquerda_P1[7].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      APAGAR_P1.append(Habilidade_Esquerda_P1[7]) 
      Habilidade_Esquerda_P1[X7_P1].draw(janela) 
      anchor_P1 = Habilidade_Esquerda_P1[X7_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Esquerda_P1[X7_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      APAGAR_HABILIDADE_P1.append(Habilidade_Esquerda_P1[X7_P1])        
      if (contadorGLOBAL%10)==1:
        X7_P1+=1
        if (X7_P1==len(Habilidade_Esquerda_P1)):
          X7_P1=0
          COLISAO_P1=False
          HABILIDADE_P1=False
          contHAB_P1=0   
    
    if (COLISAO_P1==True) and (lado_P1=="direita") and (P1!="Vegeta/"):  
      apagar_sprites_P1(APAGAR_P1)
      Habilidade_Direita_P1[7].draw(janela) 
      anchor_P1 = Habilidade_Direita_P1[7].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Direita_P1[7].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      APAGAR_P1.append(Habilidade_Direita_P1[7]) 
      Habilidade_Direita_P1[X7_P1].draw(janela) 
      anchor_P1 = Habilidade_Direita_P1[X7_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Direita_P1[X7_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )
      APAGAR_HABILIDADE_P1.append(Habilidade_Direita_P1[X7_P1])        
      if (contadorGLOBAL%10)==1:
        X7_P1+=1
        if (X7_P1==len(Habilidade_Direita_P1)):
          X7_P1=0
          COLISAO_P1=False
          HABILIDADE_P1=False
          contHAB_P1=0
    
    if (GOLPEADO_DIREITA_P1==True) or (GOLPEADO_ESQUERDA_P1==True) and (P1!="Vegeta/"):#SE TOMAR HIT CANCELA A habilidade
       COLISAO_P1=False
       HABILIDADE_P1=False
       X7_P1=0
       contHAB_P1=0
  #################################################### --- colisao --- ############################################
    
    if  (COLISAO_P1==True) and (lado_P1=="direita") and (P1!="Vegeta/"):
      if ((PosicaoX_P1)<=(PosicaoX_P2)) and ((PosicaoX_P2-(PosicaoX_P1+(250*(X7_P1-9))))<0 ) and ((PosicaoY_P2-PosicaoY_P1)<90):                                
        GOLPEADO_DIREITA_P2=True               
        contSOCO_P2=0
        contSOCO_P1=300
    elif  (COLISAO_P1==True) and (lado_P1=="esquerda") and (P1!="Vegeta/"):
      if ((PosicaoX_P1)>=(PosicaoX_P2)) and ((PosicaoX_P2-(PosicaoX_P1-(250*(X7_P1-9))))>0 ) and ((PosicaoY_P2-PosicaoY_P1)<90):                                
        GOLPEADO_ESQUERDA_P2=True               
        contSOCO_P2=0
        contSOCO_P1=300    
  #################################################################################################################
        
  ######################################## --- HABILIDADE_P1 (Vegeta) - ###########################################

    if ("b" in teclas) and (contHAB_P1>150) and (GOLPEADO_DIREITA_P1==False) and (GOLPEADO_ESQUERDA_P1==False) and (PULO_P1==False) and (P1=="Vegeta/") and (MORTO_P1==False):
      if (HABILIDADE_P1==False):
        HABILIDADE_P1=True
        lado_atual_P1=lado_P1
    if (HABILIDADE_P1==True) and (COLISAO_P1==False) and (lado_atual_P1=="direita")  and (P1=="Vegeta/"):
      apagar_sprites_P1(APAGAR_P1)
      Habilidade_Direita_P1[X7_P1].draw(janela) 
      anchor_P1 = Habilidade_Direita_P1[X7_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Direita_P1[X7_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )    
      APAGAR_P1.append(Habilidade_Direita_P1[X7_P1])        
      if (contadorGLOBAL%18)==1:
        X7_P1+=1
        if (X7_P1==5):
          PODER_P1=True      
        if (X7_P1==7):
          HABILIDADE_P1=False
          contHAB_P1=0
          X7_P1=0
          
    if (PODER_P1==True) and (lado_atual_P1=="direita")  and (P1=="Vegeta/"):
      APAGAR_HABILIDADE_P1.append(Habilidade_Direita_P1[10+X8_P1])           
      Habilidade_Direita_P1[10 + X8_P1].draw(janela) 
      anchor_P1 = Habilidade_Direita_P1[10 + X8_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Direita_P1[10 + X8_P1].move(PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )  
      if (contadorGLOBAL%12)==1:
        X8_P1+=1
        if  X8_P1==4:
          HITBOX_DIREITA_P1=True
          PODER_P1=False
                
    if (HITBOX_DIREITA_P1==True) and (lado_atual_P1=="direita")  and (P1=="Vegeta/"):
      contHAB_P1-=1
      apagar_habilidade_P1(APAGAR_HABILIDADE_P1)
      APAGAR_HABILIDADE_P1.append(Habilidade_Direita_P1[13])           
      Habilidade_Direita_P1[13].draw(janela) 
      anchor_P1 = Habilidade_Direita_P1[13].getAnchor()
      BOLAX_P1 = anchor_P1.getX()
      Habilidade_Direita_P1[13].move( 8 , 0 ) 
      if (BOLAX_P1>1000):
        HITBOX_DIREITA_P1=False 
        X8_P1=0 
  #ESQUERDA
    if (HABILIDADE_P1==True) and (COLISAO_P1==False) and (lado_atual_P1=="esquerda")  and (P1=="Vegeta/"):
      apagar_sprites_P1(APAGAR_P1)
      Habilidade_Esquerda_P1[X7_P1].draw(janela) 
      anchor_P1 = Habilidade_Esquerda_P1[X7_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Esquerda_P1[X7_P1].move( PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )    
      APAGAR_P1.append(Habilidade_Esquerda_P1[X7_P1])        
      if (contadorGLOBAL%18)==1:
        X7_P1+=1
        if (X7_P1==5):
          PODER_P1=True      
        if (X7_P1==7):
          HABILIDADE_P1=False
          contHAB_P1=0
          X7_P1=0
          
    if (PODER_P1==True) and (lado_atual_P1=="esquerda")  and (P1=="Vegeta/"):
      APAGAR_HABILIDADE_P1.append(Habilidade_Esquerda_P1[10+X8_P1])           
      Habilidade_Esquerda_P1[10 + X8_P1].draw(janela) 
      anchor_P1 = Habilidade_Esquerda_P1[10 + X8_P1].getAnchor()
      anchorX_P1 , anchorY_P1 = anchor_P1.getX() , anchor_P1.getY()
      Habilidade_Esquerda_P1[10 + X8_P1].move(PosicaoX_P1 - anchorX_P1 , PosicaoY_P1 - anchorY_P1 )  
      if (contadorGLOBAL%12)==1:
        X8_P1+=1
        if  X8_P1==4:
          HITBOX_ESQUERDA_P1=True
          PODER_P1=False
                
    if (HITBOX_ESQUERDA_P1==True) and (lado_atual_P1=="esquerda")  and (P1=="Vegeta/"):
      contHAB_P1-=1
      apagar_habilidade_P1(APAGAR_HABILIDADE_P1)
      APAGAR_HABILIDADE_P1.append(Habilidade_Esquerda_P1[13])           
      Habilidade_Esquerda_P1[13].draw(janela) 
      anchor_P1 = Habilidade_Esquerda_P1[13].getAnchor()
      BOLAX_P1 = anchor_P1.getX()
      Habilidade_Esquerda_P1[13].move( -8 , 0 ) 
      if (BOLAX_P1<-1000):
        HITBOX_ESQUERDA_P1=False 
        X8_P1=0 
    
    if ((GOLPEADO_DIREITA_P1==True) or (GOLPEADO_ESQUERDA_P1==True)) and (P1=="Vegeta/"):#SE TOMAR HIT CANCELA A habilidade
      PODER_P1=False
      HABILIDADE_P1=False
      X7_P1=0
      X8_P1=0
      contHAB_P1=0    
  ######################################################### --- colisao --- #########################################

    if (HITBOX_DIREITA_P1==True) and (P1=="Vegeta/"):  
      if ((BOLAX_P1+100)>(PosicaoX_P2)) and ((BOLAX_P1-5)<(PosicaoX_P2)) and (PosicaoY_P2<-165):                                
        GOLPEADO_DIREITA_P2=True     
        contHAB_P1=0
        HITBOX_DIREITA_P1=False 
        X8_P1=0
        contSOCO_P2=0
        contSOCO_P1=300
    if (HITBOX_ESQUERDA_P1==True) and (P1=="Vegeta/"):  
      if ((BOLAX_P1+5)>(PosicaoX_P2)) and ((BOLAX_P1-100)<(PosicaoX_P2)) and (PosicaoY_P2<-165):                                
        GOLPEADO_ESQUERDA_P2=True     
        contHAB_P1=0
        HITBOX_ESQUERDA_P1=False 
        X8_P1=0
        contSOCO_P2=0
        contSOCO_P1=300
        
  ################################################################################################################## 





























  ############################################### --- HABILIDADE P2_NARUTO --- ####################################
    
    if ("o" in teclas) and (contHAB_P2>150) and (GOLPEADO_DIREITA_P2==False) and (GOLPEADO_ESQUERDA_P2==False) and (PULO_P2==False) and (P2=="Naruto/") and (MORTO_P2==False):
      HABILIDADE_P2=True
      
    if (HABILIDADE_P2==True) and (COLISAO_P2==False) and (lado_P2=="direita") and (P2=="Naruto/"): 
      apagar_sprites_P2(APAGAR_P2)
      Habilidade_Direita_P2[X7_P2].draw(janela) 
      anchor_P2 = Habilidade_Direita_P2[X7_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Habilidade_Direita_P2[X7_P2].move( PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )
      if (X7_P2>7):
        Habilidade_Direita_P2[X7_P2].move( 0 , 30 )
      APAGAR_P2.append(Habilidade_Direita_P2[X7_P2])        
      if (contadorGLOBAL%10)==1:
        X7_P2+=1
        if (X7_P2==16):
          HABILIDADE_P2=False
          X7_P2=0
          contHAB_P2=0
    
    if (HABILIDADE_P2==True) and (COLISAO_P2==False) and (lado_P2=="esquerda") and (P2=="Naruto/"): 
      apagar_sprites_P2(APAGAR_P2)
      Habilidade_Esquerda_P2[X7_P2].draw(janela) 
      anchor_P2 = Habilidade_Esquerda_P2[X7_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Habilidade_Esquerda_P2[X7_P2].move( PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )
      if (X7_P2>7):
        Habilidade_Esquerda_P2[X7_P2].move( 0 , 30 )
      APAGAR_P2.append(Habilidade_Esquerda_P2[X7_P2])        
      if (contadorGLOBAL%10)==1:
        X7_P2+=1
        if (X7_P2==16):
          HABILIDADE_P2=False
          X7_P2=0
          contHAB_P2=0

    if (GOLPEADO_DIREITA_P2==True) or (GOLPEADO_ESQUERDA_P2==True) and (P2=="Naruto/"):#SE TOMAR HIT CANCELA A habilidade
       HABILIDADE_P2=False
       X7_P2=0
       contHAB_P2=0
       
  #################################################### --- colisao --- ###########################################  

    if (X7_P2>6) and (lado_P2=="direita") and (PosicaoX_P2)<=(PosicaoX_P1) and ((PosicaoX_P1-PosicaoX_P2)<=180) and ((PosicaoY_P1-PosicaoY_P2)<150) and ((PosicaoY_P1-PosicaoY_P2)>-150) and  (P2=="Naruto/"):                                
        GOLPEADO_DIREITA_P1=True               
        contSOCO_P1=0
        contSOCO_P2=450
    if (X7_P2>6) and (lado_P2=="esquerda") and (PosicaoX_P2+20)>=(PosicaoX_P1) and (PosicaoX_P1-PosicaoX_P2)>=-180 and ((PosicaoY_P1-PosicaoY_P2)<150) and ((PosicaoY_P1-PosicaoY_P2)>-150) and  (P2=="Naruto/"):
        GOLPEADO_ESQUERDA_P1=True
        contSOCO_P1=0
        contSOCO_P2=450               
  ################################################################################################################
        
  ######################################## --- HABILIDADE_P2 (Sasuke , Itachi, Madara) - ########################

    if ("o" in teclas) and (contHAB_P2>150) and (GOLPEADO_DIREITA_P2==False) and (GOLPEADO_ESQUERDA_P2==False) and (PULO_P2==False) and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")) and (MORTO_P2==False):
      if (HABILIDADE_P2==False):
        HABILIDADE_P2=True
        lado_atual_P2=lado_P2
    if (HABILIDADE_P2==True) and (COLISAO_P2==False) and (lado_atual_P2=="direita")  and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")):
      apagar_sprites_P2(APAGAR_P2)
      Habilidade_Direita_P2[X7_P2].draw(janela) 
      anchor_P2 = Habilidade_Direita_P2[X7_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Habilidade_Direita_P2[X7_P2].move( PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )    
      APAGAR_P2.append(Habilidade_Direita_P2[X7_P2])        
      if (contadorGLOBAL%18)==1:
        X7_P2+=1
        if (X7_P2==5):
          PODER_P2=True      
        if (X7_P2==7):
          HABILIDADE_P2=False
          contHAB_P2=0
          X7_P2=0
          
    if (PODER_P2==True) and (lado_atual_P2=="direita")  and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")):
      APAGAR_HABILIDADE_P2.append(Habilidade_Direita_P2[10+X8_P2])           
      Habilidade_Direita_P2[10 + X8_P2].draw(janela) 
      anchor_P2 = Habilidade_Direita_P2[10 + X8_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Habilidade_Direita_P2[10 + X8_P2].move(PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )  
      if (contadorGLOBAL%12)==1:
        X8_P2+=1
        if  X8_P2==4:
          HITBOX_DIREITA_P2=True
          PODER_P2=False
                
    if (HITBOX_DIREITA_P2==True) and (lado_atual_P2=="direita") and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")):
      contHAB_P2-=1
      apagar_habilidade_P2(APAGAR_HABILIDADE_P2)
      APAGAR_HABILIDADE_P2.append(Habilidade_Direita_P2[13])           
      Habilidade_Direita_P2[13].draw(janela) 
      anchor_P2 = Habilidade_Direita_P2[13].getAnchor()
      BOLAX_P2 = anchor_P2.getX()
      Habilidade_Direita_P2[13].move( 8 , 0 ) 
      if (BOLAX_P2>1000):
        HITBOX_DIREITA_P2=False 
        X8_P2=0 
  #ESQUERDA
    if (HABILIDADE_P2==True) and (COLISAO_P2==False) and (lado_atual_P2=="esquerda") and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")):
      apagar_sprites_P2(APAGAR_P2)
      Habilidade_Esquerda_P2[X7_P2].draw(janela) 
      anchor_P2 = Habilidade_Esquerda_P2[X7_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Habilidade_Esquerda_P2[X7_P2].move( PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )    
      APAGAR_P2.append(Habilidade_Esquerda_P2[X7_P2])        
      if (contadorGLOBAL%18)==1:
        X7_P2+=1
        if (X7_P2==5):
          PODER_P2=True      
        if (X7_P2==7):
          HABILIDADE_P2=False
          contHAB_P2=0
          X7_P2=0
          
    if (PODER_P2==True) and (lado_atual_P2=="esquerda")  and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")):
      APAGAR_HABILIDADE_P2.append(Habilidade_Esquerda_P2[10+X8_P2])           
      Habilidade_Esquerda_P2[10 + X8_P2].draw(janela) 
      anchor_P2 = Habilidade_Esquerda_P2[10 + X8_P2].getAnchor()
      anchorX_P2 , anchorY_P2 = anchor_P2.getX() , anchor_P2.getY()
      Habilidade_Esquerda_P2[10 + X8_P2].move(PosicaoX_P2 - anchorX_P2 , PosicaoY_P2 - anchorY_P2 )  
      if (contadorGLOBAL%12)==1:
        X8_P2+=1
        if  X8_P2==4:
          HITBOX_ESQUERDA_P2=True
          PODER_P2=False
                
    if (HITBOX_ESQUERDA_P2==True) and (lado_atual_P2=="esquerda")  and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")):
      contHAB_P2-=1
      apagar_habilidade_P2(APAGAR_HABILIDADE_P2)
      APAGAR_HABILIDADE_P2.append(Habilidade_Esquerda_P2[13])           
      Habilidade_Esquerda_P2[13].draw(janela) 
      anchor_P2 = Habilidade_Esquerda_P2[13].getAnchor()
      BOLAX_P2 = anchor_P2.getX()
      Habilidade_Esquerda_P2[13].move( -8 , 0 ) 
      if (BOLAX_P2<-1000):
        HITBOX_ESQUERDA_P2=False 
        X8_P2=0 
    
    if (GOLPEADO_DIREITA_P2==True) or (GOLPEADO_ESQUERDA_P2==True) and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")):#SE TOMAR HIT CANCELA A habilidade
      PODER_P2=False
      HABILIDADE_P2=False
      X7_P2=0
      X8_P2=0
      contHAB_P2=0
        
  ######################################################### --- colisao --- #####################################

    if (HITBOX_DIREITA_P2==True) and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")):  
      if ((BOLAX_P2+100)>(PosicaoX_P1)) and ((BOLAX_P2-5)<(PosicaoX_P1)) and (PosicaoY_P1<-165):                                
        GOLPEADO_DIREITA_P1=True     
        contHAB_P2=0
        HITBOX_DIREITA_P2=False 
        X8_P2=0
        contSOCO_P1=0
        contSOCO_P2=300
    if (HITBOX_ESQUERDA_P2==True) and ((P2=="Sasuke/") or (P2=="Itachi/") or (P2=="Madara/")):  
      if ((BOLAX_P2+5)>(PosicaoX_P1)) and ((BOLAX_P2-100)<(PosicaoX_P1)) and (PosicaoY_P1<-165):                                
        GOLPEADO_ESQUERDA_P1=True     
        contHAB_P2=0
        HITBOX_ESQUERDA_P2=False 
        X8_P2=0
        contSOCO_P1=0
        contSOCO_P2=300
        
  ##############################################################################################################      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  ############################################# --- GOLPEADO_P1 --- ################################################

    if (GOLPEADO_DIREITA_P1==True):    
      apagar_sprites_P1(APAGAR_P1)   
      if (contadorGLOBAL%50==1):
        contHIT_P1+=1 
        if contHIT_P1>1:
          contHIT_P1=1
      Golpeado_Direita_P1[contHIT_P1].draw(janela)
      XX = Golpeado_Direita_P1[contHIT_P1].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Golpeado_Direita_P1[contHIT_P1].move(PosicaoX_P1 - Xx , PosicaoY_P1 - Yy)   
      Golpeado_Direita_P1[contHIT_P1].move(((1+(DANO_P1/11))*(1+(contSOCO_P2/130)))/PARAMETRO_P1 , 0)
      PosicaoX_P1=PosicaoX_P1 + (((1+(DANO_P1/11))*(1+(contSOCO_P2/130)))/PARAMETRO_P1)
      PARAMETRO_P1=PARAMETRO_P1+0.15
      if (((((1+(DANO_P1/11))*(1+(contSOCO_P2/130)))/PARAMETRO_P1)<3) and (contHIT_P1==1)):
        DANO_P1+= int((2 * (1+(contSOCO_P2/130))) * MULTIPLICADOR)
        GOLPEADO_DIREITA_P1=False  
        PARAMETRO_P1=1.5
        APAGAR_P1.append(Golpeado_Direita_P1[contHIT_P1])  
        apagar_sprites_P1(APAGAR_P1)   
        contHIT_P1=0
      APAGAR_P1.append(Golpeado_Direita_P1[contHIT_P1])

    elif (GOLPEADO_ESQUERDA_P1==True):    
      apagar_sprites_P1(APAGAR_P1)   
      if (contadorGLOBAL%50==1):
        contHIT_P1+=1 
        if contHIT_P1>1:
          contHIT_P1=1
      Golpeado_Esquerda_P1[contHIT_P1].draw(janela)
      XX = Golpeado_Esquerda_P1[contHIT_P1].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Golpeado_Esquerda_P1[contHIT_P1].move(PosicaoX_P1 - Xx , PosicaoY_P1 - Yy)   
      Golpeado_Esquerda_P1[contHIT_P1].move(((1+(DANO_P1/11))*(1+(contSOCO_P2/130)))/PARAMETRO_P1 , 0)
      PosicaoX_P1=PosicaoX_P1 - (((1+(DANO_P1/11))*(1+(contSOCO_P2/130)))/PARAMETRO_P1)
      PARAMETRO_P1=PARAMETRO_P1+0.15
      if (((((1+(DANO_P1/11))*(1+(contSOCO_P2/130)))/PARAMETRO_P1)<3) and (contHIT_P1==1)):
        DANO_P1+= int((2 * (1+(contSOCO_P2/130))) * MULTIPLICADOR)
        GOLPEADO_ESQUERDA_P1=False  
        PARAMETRO_P1=1.5
        APAGAR_P1.append(Golpeado_Esquerda_P1[contHIT_P1])  
        apagar_sprites_P1(APAGAR_P1)   
        contHIT_P1=0
      APAGAR_P1.append(Golpeado_Esquerda_P1[contHIT_P1]) 
      
  ############################################# --- GOLPEADO_P2 --- ###############################################
    
    if (GOLPEADO_DIREITA_P2==True):    
      apagar_sprites_P2(APAGAR_P2)   
      if (contadorGLOBAL%50==1):
        contHIT_P2+=1 
        if contHIT_P2>1:
          contHIT_P2=1
      Golpeado_Direita_P2[contHIT_P2].draw(janela)
      XX = Golpeado_Direita_P2[contHIT_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Golpeado_Direita_P2[contHIT_P2].move(PosicaoX_P2 - Xx , PosicaoY_P2 - Yy)   
      Golpeado_Direita_P2[contHIT_P2].move(((1+(DANO_P2/11))*(1+(contSOCO_P1/130)))/PARAMETRO_P2 , 0)
      PosicaoX_P2=PosicaoX_P2 + (((1+(DANO_P2/11))*(1+(contSOCO_P1/130)))/PARAMETRO_P2)
      PARAMETRO_P2=PARAMETRO_P2+0.15
      if (((((1+(DANO_P2/11))*(1+(contSOCO_P1/130)))/PARAMETRO_P2)<3) and (contHIT_P2==1)):
        DANO_P2+= int((2 * (1+(contSOCO_P1/130))) * MULTIPLICADOR)
        GOLPEADO_DIREITA_P2=False  
        PARAMETRO_P2=1.5
        APAGAR_P2.append(Golpeado_Direita_P2[contHIT_P2])  
        apagar_sprites_P2(APAGAR_P2)   
        contHIT_P2=0
      APAGAR_P2.append(Golpeado_Direita_P2[contHIT_P2])

    elif (GOLPEADO_ESQUERDA_P2==True):    
      apagar_sprites_P2(APAGAR_P2)   
      if (contadorGLOBAL%50==1):
        contHIT_P2+=1 
        if contHIT_P2>1:
          contHIT_P2=1
      Golpeado_Esquerda_P2[contHIT_P2].draw(janela)
      XX = Golpeado_Esquerda_P2[contHIT_P2].getAnchor()
      Xx = XX.getX()
      Yy = XX.getY()
      Golpeado_Esquerda_P2[contHIT_P2].move(PosicaoX_P2 - Xx , PosicaoY_P2 - Yy)   
      Golpeado_Esquerda_P2[contHIT_P2].move(((1+(DANO_P2/11))*(1+(contSOCO_P1/130)))/PARAMETRO_P2 , 0)
      PosicaoX_P2=PosicaoX_P2 - (((1+(DANO_P2/11))*(1+(contSOCO_P1/130)))/PARAMETRO_P2)
      PARAMETRO_P2=PARAMETRO_P2+0.15
      if (((((1+(DANO_P2/11))*(1+(contSOCO_P1/130)))/PARAMETRO_P2)<3) and (contHIT_P2==1)):
        DANO_P2+= int((2 * (1+(contSOCO_P1/130))) * MULTIPLICADOR)
        GOLPEADO_ESQUERDA_P2=False  
        PARAMETRO_P2=1.5
        APAGAR_P2.append(Golpeado_Esquerda_P2[contHIT_P2])  
        apagar_sprites_P2(APAGAR_P2)   
        contHIT_P2=0
      APAGAR_P2.append(Golpeado_Esquerda_P2[contHIT_P2])   
       
  ###############################################################################################################      
             
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
           
    if contadorGLOBAL%40==1: #ATUALIZA OS DADOS DO JOGADOR
      VIDA_P1.undraw() 
      VIDA_P2.undraw()
      Dano_P1.undraw() 
      Dano_P2.undraw()    
         
      VIDA_P1 = Text(Point(-350,320), str(VIDAS_P1) + " X")
      VIDA_P1.setSize(32) 
      VIDA_P1.setFill("white")                          
      VIDA_P1.draw(janela)

      VIDA_P2 = Text(Point(580,320), str(VIDAS_P2) + " X")    
      VIDA_P2.setSize(32)
      VIDA_P2.setFill("white") 
      VIDA_P2.draw(janela)
      
            
      Dano_P1 = Text(Point(-350,265), str(DANO_P1) + " %")           
      Dano_P1.setSize(32)
      Dano_P1.setFill("white") 
      Dano_P1.draw(janela)
     
      Dano_P2 = Text(Point(580,265), str(DANO_P2) + " %")            
      Dano_P2.setSize(32)
      Dano_P2.setFill("white") 
      Dano_P2.draw(janela)
     
      if (VIDAS_P1==0) and (contAGUARDE_P1>20): #PLAYER 1 PERDEU
        FIM.draw(janela)
        FIM_DE_JOGO.play()
        del FIM_DE_JOGO
        update()
        time.sleep(2)
        FIM.undraw()
        mapa.undraw()
        info[0].undraw()     
        info[1].undraw()        
        info[2].undraw() 
        Dano_P1.undraw()
        Dano_P2.undraw()
        VIDA_P1.undraw()
        VIDA_P2.undraw()    
        apagar_sprites_P1(APAGAR_P1)
        apagar_sprites_P2(APAGAR_P2)
        apagar_efeitos_P1(APAGAR_EFEITOS_P1)
        apagar_efeitos_P1(APAGAR_EFEITOS_P2)
        apagar_habilidade_P1(APAGAR_HABILIDADE_P1)
        apagar_habilidade_P2(APAGAR_HABILIDADE_P2)  
        musica.stop()
        return "P2"
      
      elif (VIDAS_P2==0) and (contAGUARDE_P2>20): #PLAYER 2 PERDEU
        FIM.draw(janela)
        FIM_DE_JOGO.play()
        del FIM_DE_JOGO
        update()
        time.sleep(2)
        FIM.undraw()
        mapa.undraw()
        info[0].undraw()     
        info[1].undraw()        
        info[2].undraw() 
        Dano_P1.undraw()
        Dano_P2.undraw()
        VIDA_P1.undraw()
        VIDA_P2.undraw()    
        apagar_sprites_P1(APAGAR_P1)
        apagar_sprites_P2(APAGAR_P2)
        apagar_efeitos_P1(APAGAR_EFEITOS_P1)
        apagar_efeitos_P1(APAGAR_EFEITOS_P2)
        apagar_habilidade_P1(APAGAR_HABILIDADE_P1)
        apagar_habilidade_P2(APAGAR_HABILIDADE_P2)  
        musica.stop()
        return "P1"
     
     


    
    if (contHAB_P1<MAXIMO_P1):
      A1=(contHAB_P1*FATOR_DO_P1)-487      

    if (contHAB_P2<MAXIMO_P2):
      B1=(contHAB_P2*FATOR_DO_P2)+440

    if (contadorGLOBAL%25==1):         
      ESPECIAL1.undraw()
      ESPECIAL2.undraw()
      A.undraw()
      B.undraw()
      ESPECIAL1= Rectangle(Point(-487,227),Point(A1+1,210))   #Point(-487,227),Point(-290,210)) especial player 1
      ESPECIAL1.setOutline("deep sky blue") 
      ESPECIAL1.setFill("deep sky blue")
      ESPECIAL1.draw(janela)  
    
      ESPECIAL2= Rectangle(Point(440,227),Point(B1+1,210))    #Point(440,227),Point(637,210)) especial player 2
      ESPECIAL2.setOutline("deep sky blue")
      ESPECIAL2.setFill("deep sky blue")
      ESPECIAL2.draw(janela)
    
      X3 = (0.507614213 * (A1+487))
      X4 = (0.507614213 * (B1-440))
      X3=int(math.ceil(X3))
      X4=int(math.ceil(X4))
      A = Text(Point(-389,218), str(X3) + "%")
      B = Text(Point(538,218), str(X4) + "%")
      A.draw(janela)
      B.draw(janela)

  ############################################## --- SAÍDA , PAUSE E TIMING --- ################################   
   
    contPAUSE+=1
    if ("Escape" in teclas): #esse contPAUSE -1 impede ele de entrar instantaneamente no pause de novo
          contPAUSE-=1
    if ("Escape" in teclas) and contPAUSE>10: 
      pause = Image(Point(0,0),"Imagens/Efeitos_jogo/pause.png")
      pause.draw(janela)
      contPAUSE=0
      while True:
        if ("Delete" in teclas):  
          os.system("xset r on")
          janela.close()
        teclas = janela.checkKey_Buffer()
        update()
        contPAUSE+=1
        if ("Escape" in teclas): #esse contPAUSE -1 impede ele de sair instantaneamente do pause
          contPAUSE-=1
        if contPAUSE>10:
          teclas = janela.checkKey_Buffer()
          update()
          if ("Escape" in teclas):
            contPAUSE=0
            pause.undraw()
            break
    
    if ("Delete" in teclas):  
      os.system("xset r on")
      janela.close()

    t_final = datetime.datetime.now()
    fator_tempo = float((t_final-starttime).microseconds)/1000
    durma= 0.002 / fator_tempo  # +/- 200FPS
    time.sleep(durma)
    
  ####################################### --- Frederico Bender Tiggemann --- ####################################  
    
    
    
  

############ -- VARIAVEIS -- #################################################################################

Z=4
Y=4
x2=1

############ -- PROGRAMAÇAO -- ###############################################################################

PNG="Imagens/Inicio/"
janela=GraphWin("Dragonball VS Naruto",1300,710,autoflush=False)
janela.setCoords(-650,-355,650,355)

FundoVelho = Image(Point(0,0), PNG + "fundo.png")
FundoVelho.draw(janela)


CARREGANDO = loading()
update()

fundo = fundo_inicial()                  ##############
selecaoPersonagem = selecao_inicial()     ##############
mapas = mapas_iniciais()                   #loading - 1 #
opcoesMenu = opcoes_iniciais()              ##############
sons = sons_iniciais()                       ##############
                                 
CARREGANDO.undraw()
update()

inicio(fundo,sons)

FundoVelho.undraw()
del fundo

while True:
  voltar = Image(Point(0,0),"Imagens/Instrucoes/volta.png")
  sons[2].play(-1)
  CARREGANDO.undraw()
  update() 
  FundoVelho.undraw()
 
  while Z==4:   #FAZ AS TELAS DE SELEÇÃO VOLTAREM
		while Y==4:
		  if x2!=0:
		    os.system("xset r off")
		    X = selecao(selecaoPersonagem,sons)
		  Y = mapa(mapas,sons,voltar) 
		  if Y==4:
		    x2=1   
		os.system("xset r on")  
		Z = opcoes(opcoesMenu,sons,voltar)
		if Z==4:
		  x2=0
		  Y=4

  del voltar
  del selecaoPersonagem              #DELETA IMAGENS ANTIGAS E CARREGA AS NOVAS
  del opcoesMenu
  del sons
  info = informacoes_JOGO(X)        ##############
  mapinha = mapa_no_jogo(Y)          #loading - 2 #
  musica = musica_JOGO(Y)             ##############              

  janela.ligar_Buffer()
  os.system("xset r off") 
  VITORIOSO = jogo(Z,info,musica,mapinha)
  janela.desligar_Buffer()
  Vencedor(VITORIOSO,info)
  
  janela.close()
  janela=GraphWin("Dragonball VS Naruto",1300,710,autoflush=False)
  janela.setCoords(-650,-355,650,355)
  
  FundoVelho.draw(janela)
  CARREGANDO = loading()
  update()
  
  del info            #DELETA IMAGENS ANTIGAS E CARREGA AS NOVAS
  del musica
 
  selecaoPersonagem = selecao_inicial()     ##############
  mapas = mapas_iniciais()                   #loading - 3 #
  opcoesMenu = opcoes_iniciais()              ##############
  sons = sons_iniciais()                       ##############
   
  Z=4
  Y=4
  x2=1
