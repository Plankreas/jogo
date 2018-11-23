#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
import random

IMAGEM = circulo(25,Cor(96, 219, 150))
PLAT = retangulo(200,35,Cor(96, 219, 211))


StandR = [carregar_imagem("./SR1.png"),
         carregar_imagem("./SR2.png"),
         carregar_imagem("./SR3.png"),
         carregar_imagem("./SR4.png"),
         carregar_imagem("./SR1.png"),
         carregar_imagem("./SR1.png"),
         carregar_imagem("./SR1.png"),
         carregar_imagem("./SR1.png"),
         carregar_imagem("./SR1.png"),
         carregar_imagem("./SR1.png"),
         carregar_imagem("./SR1.png")]

StandL = [carregar_imagem("./SL1.png"),
         carregar_imagem("./SL2.png"),
         carregar_imagem("./SL3.png"),
         carregar_imagem("./SL4.png"),
         carregar_imagem("./SL1.png"),
         carregar_imagem("./SL1.png"),
         carregar_imagem("./SL1.png"),
         carregar_imagem("./SL1.png"),
         carregar_imagem("./SL1.png"),
         carregar_imagem("./SL1.png"),
         carregar_imagem("./SL1.png")]

WalkR = [carregar_imagem("./WR1.png"),
         carregar_imagem("./WR2.png"),
         carregar_imagem("./WR3.png"),
         carregar_imagem("./WR4.png"),
         carregar_imagem("./WR5.png"),
         carregar_imagem("./WR6.png"),
         carregar_imagem("./WR7.png"),
         carregar_imagem("./WR8.png")]

WalkL = [carregar_imagem("./WL1.png"),
         carregar_imagem("./WL2.png"),
         carregar_imagem("./WL3.png"),
         carregar_imagem("./WL4.png"),
         carregar_imagem("./WL5.png"),
         carregar_imagem("./WL6.png"),
         carregar_imagem("./WL7.png"),
         carregar_imagem("./WL8.png")]

JumpR = [carregar_imagem("./JR1.png"),
         carregar_imagem("./JR2.png"),
         carregar_imagem("./JR3.png")]

JumpR3 = carregar_imagem("JR3.png")
JumpL3 = carregar_imagem("JL3.png")

JumpL = [carregar_imagem("./JL1.png"),
         carregar_imagem("./JL2.png"),
         carregar_imagem("./JL3.png")]
'''
Cai = []
'''

Scont = 0
Wcont = 0




ALTURA, LARGURA = 600,600
tela = criar_tela_base(ALTURA, LARGURA)

DX = 5
G = 1

METADE_L_HERO = largura_imagem(IMAGEM) // 2
METADE_A_HERO = altura_imagem(IMAGEM) // 2
METADE_L_ENEMY = largura_imagem(IMAGEM) // 2
METADE_A_ENEMY = altura_imagem(IMAGEM) // 2
METADE_L_PLAT = largura_imagem(PLAT) // 2
METADE_A_PLAT = altura_imagem(PLAT) // 2


LIMITE_ESQUERDO = METADE_L_HERO
LIMITE_DIREITO = LARGURA - METADE_L_HERO
LIMITE_CIMA = METADE_A_HERO
LIMITE_BAIXO = ALTURA - METADE_A_HERO

CHAO = LIMITE_BAIXO
COLIDE = False

Right = True
Left = False

'''================================================================================================'''
''' ==================================== [DEFINIÇÃO DE DADOS] ====================================='''
'''================================================================================================'''


Hero = definir_estrutura("hero", "x, y, dx, dy", mutavel=True)
''' Hero pode ser formado da seguinte forma: Hero(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[-LARGURA, +LARGURA])
interp. representa a posição do herói no eixo x e y, e sua velocidadee direção (dx e dy)
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

Plat = definir_estrutura("plat", "x, y", mutavel=True)
''' Plat pode ser formado da seguinte forma: Plat(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[-LARGURA, +LARGURA])
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

Jogo = definir_estrutura("Jogo", "hero, plat", mutavel=True)
''' Jogo pode ser formado assim: Jogo(Hero, ListaEnemy, Boolean, Int+)
interp. representa o jogo todo com um herói e zero ou mais inimigos. O campo game_over indica se o jogo está acabado ou não.
'''
#EXEMPLOS:
JOGO_INICIAL = Jogo(HERO_INICIAL, PLAT_INICIAL)

##TEMPLATE
'''
def fn_para_jogo(jogo):
    ... jogo.hero
        jogo.enemy
        jogo.game_over
'''

'''================================================================================================'''
''' ========================================== [FUNÇÕES] =========================================='''
'''================================================================================================'''


''' ------------ [DESENHA] ------------'''

'''
desenha_jogo: Jogo -> Imagem
Desenha todos os elementos do jogo de acordo com o estado atual
'''
def desenha_jogo(jogo):
    desenha_plat(jogo.plat)
    desenha_hero(jogo.hero)
    '''if (not jogo.game_over):
        desenha_hero(jogo.hero)
        desenha_enemies(jogo.enemy)
    else:
        desenha_game_over()'''


'''
desenha_hero: Hero -> Imagem
Desenha o herói'''
def desenha_hero(hero):
    '''colocar_imagem(IMAGEM, tela, hero.x, hero.y)'''
    global Scont
    global Wcont

    if Scont + 1 >= 66:
        Scont = 0
    if hero.dy == 0 and hero.dx == 0 and Right:
        colocar_imagem(StandR[Scont // 6], tela, hero.x, hero.y)
        Scont += 1
    if hero.dy == 0 and hero.dx == 0 and Left:
        colocar_imagem(StandL[Scont // 6], tela, hero.x, hero.y)
        Scont += 1

    if Wcont + 1 >= 48:
        Wcont = 0
    if hero.dy == 0 and hero.dx != 0 and Right:
        colocar_imagem(WalkR[Wcont // 6], tela, hero.x, hero.y)
        Wcont += 1
    if hero.dy == 0 and hero.dx != 0 and Left:
        colocar_imagem(WalkL[Wcont // 6], tela, hero.x, hero.y)
        Wcont += 1

    if (not COLIDE) and hero.dy < 0 and Right:
        colocar_imagem(JumpR[0], tela, hero.x, hero.y)
    if (not COLIDE) and hero.dy >= 0 and hero.dy <= 10 and Right:
        colocar_imagem(JumpR[1], tela, hero.x, hero.y)
    if (not COLIDE) and hero.dy > 10 and Right:
        colocar_imagem(JumpR[2], tela, hero.x, hero.y)

    if (not COLIDE) and hero.dy < 0 and Left:
        colocar_imagem(JumpL[0], tela, hero.x, hero.y)
    if (not COLIDE) and hero.dy >= 0 and hero.dy <= 10 and Left:
        colocar_imagem(JumpL[1], tela, hero.x, hero.y)
    if (not COLIDE) and hero.dy > 10 and Left:
        colocar_imagem(JumpL[2], tela, hero.x, hero.y)

'''
desenha_plat: Plat -> Imagem
Desenha a plataforma'''
def desenha_plat(plat):
    colocar_imagem(PLAT, tela, plat.x, plat.y)


''' ------------ [MOVE] ------------'''
'''
mover_tudo: Jogo -> Jogo
Produz o próximo estado do jogo 
'''
def mover_tudo(jogo):
    global COLIDE
    if colide_plat(jogo.hero, jogo.plat):
        COLIDE = True
        jogo.hero.dy = 0
    if (not colide_plat(jogo.hero, jogo.plat)):
            COLIDE = False
    mover_hero(jogo.hero)
    return jogo

'''
mover_hero: Hero -> Hero
Move o Herói
'''
def mover_hero(hero):
    global COLIDE
    pulo = False
    cont = 10


    hero.x = hero.x + hero.dx
    hero.y = hero.y + hero.dy

    if hero.x > LIMITE_DIREITO:
        hero.x = LIMITE_DIREITO
    elif hero.x < LIMITE_ESQUERDO:
        hero.x = LIMITE_ESQUERDO

    elif hero.y < LIMITE_CIMA:
        hero.dy = -hero.dy
        return hero

    if COLIDE:
        hero.dy = 0
    else:
        hero.dy += G
        if not(pulo):
                pulo = True
        else:
            if cont >= -10:
                hero.dy -= (cont **2) * 0.5
                cont -= 1
            else:
                pulo = False
                cont = 10
    return hero


''' ------------ [COLISÃO] ------------'''

'''
colide_plat: Hero, Plat -> Boolean
Verifica se o herói colidiu com a Plataforma.
'''
def colide_plat(hero, plat):
    '''Hit Box - Herói'''
    heroL = hero.x - METADE_L_HERO
    heroR = hero.x + METADE_L_HERO
    heroU = hero.y - METADE_A_HERO
    heroD = hero.y + METADE_A_HERO

    '''Hit Box - Plataforma'''
    platL = plat.x - METADE_L_PLAT
    platR = plat.x + METADE_L_PLAT
    platU = plat.y - METADE_A_PLAT
    platD = plat.y + METADE_A_PLAT

    return heroR >= platL and \
           heroL <= platR and \
           heroD >= platU and \
           heroU <= platD


''' ------------ [TRATA TECLA] ------------'''


'''
trata_tecla_jogo: Jogo, Tecla -> Jogo
Trata tecla para o jogo todo.
'''
def trata_tecla_jogo(jogo, tecla):
    hero_novo = trata_tecla_hero(jogo.hero, tecla)
    return Jogo(hero_novo, jogo.plat)


'''
trata_tecla: Hero, Tecla -> Hero
Faz o herói se movimentar para a direita ou esquerda, ou pular
'''
def trata_tecla_hero(hero, tecla):
    global COLIDE
    global Right
    global Left
    if tecla == pg.K_UP and COLIDE:
        COLIDE = False
        hero.y -= 20
        hero.dy -= 20
    elif tecla == pg.K_RIGHT:
        hero.dx = DX
        Right = True
        Left = False
    elif tecla == pg.K_LEFT:
        hero.dx = -DX
        Right = False
        Left = True
    return hero


'''
trata_solta_jogo: Jogo Tecla -> Jogo
'''
def trata_solta_jogo(jogo, tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_RIGHT:
        return Jogo(Hero(jogo.hero.x, jogo.hero.y, 0, jogo.hero.dy), jogo.plat)
    return jogo


'''
Jogo -> Jogo
inicie o mundo com JOGO_INICIAL
'''
def main(inic):
    big_bang(inic,  # Jogo
             tela=tela,
             frequencia=40,
             quando_tick=mover_tudo,  # Jogo -> Jogo
             desenhar=desenha_jogo,  # Jogo -> Imagem
             quando_tecla=trata_tecla_jogo,  # Hero Tecla -> Vaca
             quando_solta_tecla=trata_solta_jogo,  # Jogo Tecla -> Jogo
             modo_debug=True
             )



''' Hero -> Hero '''
''' inicie o mundo com HERO_INICIAL '''
def main_hero(inic):
    big_bang(inic,   # Hero
             tela=tela,
             frequencia=60,
             quando_tick=mover_hero,  # Hero -> Hero
             desenhar=desenha_hero,   # Hero -> Imagem
             quando_tecla=trata_tecla_hero, # Hero Tecla-> Hero
             modo_debug=True
             )

main(JOGO_INICIAL)