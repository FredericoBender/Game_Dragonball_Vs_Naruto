#encoding=utf-8
from graphics import *
import time,math,random
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
	imagem = (Image(Point(0,0), PNG + "SELECAO_X.png"))
	return imagem

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

def mapa_JOGO(x):  
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
  imagem.draw(janela)
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
  while True: 
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
      lista=[]
      lista.append(contX1/140)
      lista.append(contY1/140)
      lista.append(contX2/140)
      lista.append(contY2/140)
      P1_OK.undraw()
      P2_OK.undraw()
      imagem.undraw()
      return lista      #return dados x e y para saber qual personagem selecionado
       
def mapa(imagens,som):
  lista=[]
  X1=imagens[0]
  X2=imagens[1]
  X3=imagens[2]
  X4=imagens[3] 
  X1.draw(janela)
  lista.append(X1)
  X=0
  while True:
    x=janela.checkKey()
    if (x=="a") or (x=="A") or (x=="Left"):
      lista[0].undraw()
      del lista[0]
      X1.draw(janela)
      lista.append(X1)
      X=0
      
    if (x=="w") or (x=="W") or (x=="Up"):
      lista[0].undraw()
      del lista[0]
      X2.draw(janela)
      lista.append(X2)
      X=1
      
    if (x=="d") or (x=="D") or (x=="Right"):
      lista[0].undraw()
      del lista[0]
      X3.draw(janela)
      lista.append(X3)
      X=2
      
    if (x=="s") or (x=="S") or (x=="Down"):
      lista[0].undraw()
      del lista[0]
      X4.draw(janela)
      lista.append(X4)
      X=3
      
    if (x=="Return"):
      som[1].play()#########################################################################################
      lista[0].undraw()
      return X
    
    if (x=="Escape"):
      lista[0].undraw()
      return 4  
      
def opcoes(imagens,som):
  imagens[0].draw(janela)
  
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
          if (D>=2):
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
        return 4
  
def jogo(Z,info,musica,mapa): #Z== VIDAS e PONTOS, info== PERSONAGENS, musica==Musica do Mapa, mapa==Qual a ser desenhado
  mapa.draw(janela)
  info[0].draw(janela)        #Desenha as informaçoes
  info[1].draw(janela)        #Desenha a foto dos bonecos selecionados na direita e esquerda#
  info[2].draw(janela)        ###############################################################
  P1 = info[3]
  P2 = info[4]
  print P1
  print P2
  VIDA1 = Text(Point(-350,320),str(Z[0]) + " X")
  VIDA1.setSize(32) 
  VIDA1.setFill("white")                           ###DESENHA AS VIDAS
  VIDA1.draw(janela)
  
  DANO_P1 = Text(Point(-350,265),"0 %")            ###DESENHA AS VIDAS
  DANO_P1.setSize(32)
  DANO_P1.setFill("white") 
  DANO_P1.draw(janela)
  
  VIDA2 = Text(Point(580,320),str(Z[0]) + " X")    ###DESENHA O DANO
  VIDA2.setSize(32)
  VIDA2.setFill("white") 
  VIDA2.draw(janela)
  
  DANO_P2 = Text(Point(580,265),"0 %")             ###DESENHA O DANO
  DANO_P2.setSize(32)
  DANO_P2.setFill("white") 
  DANO_P2.draw(janela)
 
  update()
   
  musica.play()#############################################################################################
   
  vai3 = Image(Point(0,0), "Imagens/Efeitos_jogo/3.png")
  vai2 = Image(Point(0,0), "Imagens/Efeitos_jogo/2.png")
  vai1 = Image(Point(0,0), "Imagens/Efeitos_jogo/1.png")
  GO = Image(Point(0,0), "Imagens/Efeitos_jogo/GO.png")
 
  vai3.draw(janela)
  update()
  time.sleep(1)
  vai3.undraw()
  vai2.draw(janela)
  update()
  time.sleep(1)
  vai2.undraw()
  vai1.draw(janela)
  update()
  time.sleep(1)
  vai1.undraw()
  GO.draw(janela)
  update()
  time.sleep(1)
  GO.undraw()
  
  A1=-487
  B1=440
  while True:
    A1+=0.01
    B1+=0.01
    if A1==-290:
      A1-=0.01
      B1-=0.01
    ESPECIAL1= Rectangle(Point(-487,227),Point(A1,210))   #Point(-487,227),Point(-290,210)) especial player 1
    ESPECIAL1.setOutline("deep sky blue") 
    ESPECIAL1.setFill("deep sky blue")
    ESPECIAL1.draw(janela)  
    
    ESPECIAL2= Rectangle(Point(440,227),Point(B1,210))    #Point(440,227),Point(637,210)) especial player 2
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
    update()   
    
    ESPECIAL1.undraw()
    ESPECIAL2.undraw()
    A.undraw()
    B.undraw()     

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
del CARREGANDO

while True:
  sons[2].play(100)
  while Z==4:   #FAZ AS TELAS DE SELEÇÃO VOLTAREM
		while Y==4:
		  if x2!=0:
		    os.system("xset r off")
		    X = selecao(selecaoPersonagem,sons)
		  Y = mapa(mapas,sons) 
		  if Y==4:
		    x2=1   
		os.system("xset r on")  
		Z = opcoes(opcoesMenu,sons)
		if Z==4:
		  x2=0
		  Y=4
		
  del selecaoPersonagem              #DELETA IMAGENS ANTIGAS E CARREGA AS NOVAS
  del mapas
  del opcoesMenu
  del sons
  info = informacoes_JOGO(X)        ##############
  mapa = mapa_JOGO(Y)                #loading - 2 #
  musica = musica_JOGO(Y)             ##############              

  janela.ligar_Buffer()
  os.system("xset r off") 
 # jogo(Z,info,musica,mapa)

	
  del info                           #DELETA IMAGENS ANTIGAS E CARREGA AS NOVAS
  del musica
  del mapa
  selecaoPersonagem = selecao_inicial()     ##############
  mapas = mapas_iniciais()                   #loading - 3 #
  opcoes = opcoes_iniciais()                  ##############
  sons = sons_iniciais()                       ##############
  janela.desligar_Buffer()



