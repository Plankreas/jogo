#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
import random

''' -- Imagens -- '''

IMAGEM = carregar_imagem("./Kirby Sprites/SR1.png")         #Imagem para a Hit-Box do Herói
PLAT = retangulo(200,10,Cor(103, 133, 131))                 #Imagem para a Hit-Box da Plataforma
PLAT_IMG = carregar_imagem("./plat.png")                    #Imagem para a Plataforma
ENEMY = carregar_imagem("./Enemy Sprites/WR1.png")          #Imagem para a Hit-Box do Inimigo

FUNDO = carregar_imagem("./BG.png", 600, 600)               #Imagem para o fundo

MISC1 = carregar_imagem("./misc1.png")                      #Imagem decorativa
MISC2 = carregar_imagem("./misc2.png")                      #Imagem decorativa
MISC3 = carregar_imagem("./misc3.png")                      #Imagem decorativa


''' ---------- Sprites de animação do Herói ---------- '''

#Parado Direita
StandR = [carregar_imagem("./Kirby Sprites/SR1.png"),
         carregar_imagem("./Kirby Sprites/SR2.png"),
         carregar_imagem("./Kirby Sprites/SR3.png"),
         carregar_imagem("./Kirby Sprites/SR1.png"),
         carregar_imagem("./Kirby Sprites/SR1.png"),
         carregar_imagem("./Kirby Sprites/SR1.png"),
         carregar_imagem("./Kirby Sprites/SR1.png"),
         carregar_imagem("./Kirby Sprites/SR1.png"),
         carregar_imagem("./Kirby Sprites/SR1.png"),
         carregar_imagem("./Kirby Sprites/SR1.png"),
         carregar_imagem("./Kirby Sprites/SR1.png")]

#Parado Esquerda
StandL = [carregar_imagem("./Kirby Sprites/SL1.png"),
         carregar_imagem("./Kirby Sprites/SL2.png"),
         carregar_imagem("./Kirby Sprites/SL3.png"),
         carregar_imagem("./Kirby Sprites/SL1.png"),
         carregar_imagem("./Kirby Sprites/SL1.png"),
         carregar_imagem("./Kirby Sprites/SL1.png"),
         carregar_imagem("./Kirby Sprites/SL1.png"),
         carregar_imagem("./Kirby Sprites/SL1.png"),
         carregar_imagem("./Kirby Sprites/SL1.png"),
         carregar_imagem("./Kirby Sprites/SL1.png"),
         carregar_imagem("./Kirby Sprites/SL1.png")]

#Andando p/ Direita
WalkR = [carregar_imagem("./Kirby Sprites/WR1.png"),
         carregar_imagem("./Kirby Sprites/WR2.png"),
         carregar_imagem("./Kirby Sprites/WR3.png"),
         carregar_imagem("./Kirby Sprites/WR4.png"),
         carregar_imagem("./Kirby Sprites/WR5.png"),
         carregar_imagem("./Kirby Sprites/WR6.png"),
         carregar_imagem("./Kirby Sprites/WR7.png"),
         carregar_imagem("./Kirby Sprites/WR8.png")]

#Andando p/ Esquerda
WalkL = [carregar_imagem("./Kirby Sprites/WL1.png"),
         carregar_imagem("./Kirby Sprites/WL2.png"),
         carregar_imagem("./Kirby Sprites/WL3.png"),
         carregar_imagem("./Kirby Sprites/WL4.png"),
         carregar_imagem("./Kirby Sprites/WL5.png"),
         carregar_imagem("./Kirby Sprites/WL6.png"),
         carregar_imagem("./Kirby Sprites/WL7.png"),
         carregar_imagem("./Kirby Sprites/WL8.png")]

#Pulando p/ Direita
JumpR = [carregar_imagem("./Kirby Sprites/JR1.png"),
         carregar_imagem("./Kirby Sprites/JR2.png"),
         carregar_imagem("./Kirby Sprites/JR3.png")]

#Pulando p/ Esquerda
JumpL = [carregar_imagem("./Kirby Sprites/JL1.png"),
         carregar_imagem("./Kirby Sprites/JL2.png"),
         carregar_imagem("./Kirby Sprites/JL3.png")]

Scont = 0 #Contator de Animação parado
Wcont = 0 #Contador de Animação andando
Econt = 0 #Contador de Animação do inimigo


''' ---------- Sprites de animação do Inimigo ---------- '''

#Andando p/ Direita
WalkER = [carregar_imagem("./Enemy Sprites/WR1.png"),
          carregar_imagem("./Enemy Sprites/WR2.png"),
          carregar_imagem("./Enemy Sprites/WR3.png"),
          carregar_imagem("./Enemy Sprites/WR4.png")]

#Andando p/ Esquerda
WalkEL = [carregar_imagem("./Enemy Sprites/WL1.png"),
          carregar_imagem("./Enemy Sprites/WL2.png"),
          carregar_imagem("./Enemy Sprites/WL3.png"),
          carregar_imagem("./Enemy Sprites/WL4.png")]

#Caindo p/ Direita
FallER = carregar_imagem("./Enemy Sprites/FR.png")

#Caindo p/ Esquerda
FallEL = carregar_imagem("./Enemy Sprites/FL.png")


ALTURA, LARGURA = 600,600
tela = criar_tela_base(ALTURA, LARGURA)

EDX = 2 #Velocidade de caminhada do inimigo
DX = 5  #Velocidade de caminhada do Herói
G = 1   #Gravidade


''' ----------- Metade do tamanho da imagem p/ HitBox ----------- '''
METADE_L_HERO = largura_imagem(IMAGEM) // 2
METADE_A_HERO = altura_imagem(IMAGEM) // 2
METADE_L_ENEMY = largura_imagem(ENEMY) // 2
METADE_A_ENEMY = altura_imagem(ENEMY) // 2
METADE_L_PLAT = largura_imagem(PLAT) // 2
METADE_A_PLAT = altura_imagem(PLAT) // 2

''' ----------- Não deixa o herói passar do limite de acordo com a hitbox dele ----------- '''
LIMITE_ESQUERDO = METADE_L_HERO
LIMITE_DIREITO = LARGURA - METADE_L_HERO
LIMITE_CIMA = METADE_A_HERO
LIMITE_BAIXO = ALTURA - METADE_A_HERO

CHAO = LIMITE_BAIXO     #Limite do "buraco" que gera Game Over caso caia
COLIDE = False          #Boolean que diz se o inimigo está em cima de uma plataforma ou não

''' ----------- Boolean que aponta a direção que o herói está olhando ----------- '''
Right = True
Left = False









'''================================================================================================'''
''' ==================================== [DEFINIÇÃO DE DADOS] ====================================='''
'''================================================================================================'''


Hero = definir_estrutura("hero", "x, y, dx, dy", mutavel=True)
''' Hero pode ser formado da seguinte forma: Hero(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[LIMITE_CIMA, LIMITE_BAIXO],
                                                    Int[-LARGURA, +LARGURA], Int[-ALTURA, + ALTURA])
interp. representa a posição do herói no eixo x e y, e sua velocidade e direção (dx e dy)
'''
#EXEMPLOS:
HERO_INICIAL = Hero(LARGURA//2, ALTURA//2, 0, 0)

##TEMPLATE
'''
def fn_para_hero(hero):
    ... hero.x
        hero.y
        hero.dx
        hero.dy
'''


Enemy = definir_estrutura("enemy", "x, y, dx, dy, dz", mutavel=True)
''' Enemy pode ser formado da seguinte forma: Enemy(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[LIMITE_CIMA, LIMITE_BAIXO],
                                                    Int[-LARGURA, +LARGURA], Int[-ALTURA, + ALTURA], Int[0,1])
interp. representa a posição do inimigo no eixo x e y, e sua velocidade e direção (dx e dy)
'''
#EXEMPLOS:
ENEMY_INICIAL = Enemy(LARGURA//2, 0 - ALTURA // 2, 0, 0, 1)

##TEMPLATE
'''
def fn_para_enemy(enemy):
    ... enemy.x
        enemy.y
        enemy.dx
        enemy.dy
        enemy.dz
'''

#Exemplos:
L_ENEMY_1 = [ENEMY_INICIAL]
INIMIGOS = [Enemy(LARGURA // 2, 0 - ALTURA // 2, 0, 0, 1)]
'''
#template
def fn_para_lista(lista):
    if lista.vazia:
        return ...
    else:
        ... lista.primeiro
            fn_para_lista(lista.resto)
'''

Plat = definir_estrutura("plat", "x, y", mutavel=True)
''' Plat pode ser formado da seguinte forma: Plat(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[LIMITE_CIMA, LIMITE_BAIXO])
interp. representa a posição da plataforma no eixo x e y
'''
#EXEMPLOS:
PLAT_INICIAL = Plat(LARGURA//2, (ALTURA//2 + ALTURA //4))

##TEMPLATE
'''
def fn_para_plat(plat):
    ... plat.x
        plat.y
'''

#Exemplos:
L_PLAT_1 = [PLAT_INICIAL]
PLATAFORMAS = [
    Plat((LARGURA // 2), (ALTURA // 4)-25),
    Plat((LARGURA // 6), (ALTURA // 2)-25),
    Plat((LARGURA - LARGURA // 6), (ALTURA // 2)-25),
    Plat((LARGURA // 2), (ALTURA // 2 + ALTURA // 4)-25),
    Plat((LARGURA - LARGURA // 6), (ALTURA)-25),
    Plat((LARGURA // 6), (ALTURA)-25)]

'''
#template
def fn_para_lista(lista):
    if lista.vazia:
        return ...
    else:
        ... lista.primeiro
            fn_para_lista(lista.resto)
'''

Jogo = definir_estrutura("Jogo", "hero, inimigos, plataformas, game_over, tempo_inimigos, pontos", mutavel=True)
''' Jogo pode ser formado assim: Jogo(Hero, ListaInimigos, ListaPlataformas, Boolean, Int, Int+)
interp. representa o jogo todo com um herói, zero ou mais inimigos, e plataformas. O campo game_over indica se o jogo está acabado ou não.
'''
#EXEMPLOS:
JOGO_INICIAL = Jogo(HERO_INICIAL, INIMIGOS, PLATAFORMAS, False, 0, 0)

##TEMPLATE
'''
def fn_para_jogo(jogo):
    ... jogo.hero
        jogo.inimigos
        jogo.plataformas
        jogo.game_over
        jogo.tempo_inimigos
        jogo.pontos
'''