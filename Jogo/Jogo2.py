#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
import random

IMAGEM = circulo(50,Cor(96, 219, 211))
PLAT = retangulo(200,35,Cor(96, 219, 211))









ALTURA, LARGURA = 600,600
tela = criar_tela_base(ALTURA, LARGURA)

DX = 7
G = 1

METADE_L_HERO = largura_imagem(IMAGEM) // 2
METADE_A_HERO = altura_imagem(IMAGEM) // 2
METADE_L_ENEMY = largura_imagem(IMAGEM) // 2
METADE_A_ENEMY = altura_imagem(IMAGEM) // 2
METADE_L_PLAT = altura_imagem(PLAT) // 2
METADE_A_PLAT = altura_imagem(PLAT) // 2


LIMITE_ESQUERDO = METADE_L_HERO
LIMITE_DIREITO = LARGURA - METADE_L_HERO
LIMITE_CIMA = METADE_A_HERO
LIMITE_BAIXO = ALTURA - METADE_A_HERO

CHAO = LIMITE_BAIXO


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
PLAT_INICIAL = Plat((LARGURA//2 + LARGURA//4), (ALTURA//2 + ALTURA//4))

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
    desenha_hero(jogo.hero)
    desenha_plat(jogo.plat)
    '''if (not jogo.game_over):
        desenha_hero(jogo.hero)
        desenha_enemies(jogo.enemy)
    else:
        desenha_game_over()'''


'''
desenha_hero: Hero -> Imagem
Desenha o herói'''
def desenha_hero(hero):
    colocar_imagem(IMAGEM, tela, hero.x, hero.y)

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
    if (not colide_plat(jogo.hero, jogo.plat)):
        mover_hero(jogo.hero)
    else:
        mover_hero(jogo.hero)
    return jogo

'''
mover_hero: Hero -> Hero
Move o Herói
'''
def mover_hero(hero):
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

    if hero.y == CHAO:
        hero.dy = 0
    else:
        hero.dy += G
        if not(pulo):
            if (pg.K_UP):
                pulo = True
        else:
            if cont >= -10:
                hero.dy -= (cont **2) * 0.5
                cont -= 1
            else:
                pulo = False
                cont = 10
        if hero.y >= CHAO:
            hero.y = CHAO
            hero.dy = 0
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
    if tecla == pg.K_UP and hero.y == CHAO:
        hero.dy -= 20
    elif tecla == pg.K_RIGHT:
        hero.dx = DX
    elif tecla == pg.K_LEFT:
        hero.dx = -DX
    return hero


'''
trata_solta_jogo: Jogo Tecla -> Jogo
'''
def trata_solta_jogo(jogo, tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_RIGHT:
        return Jogo(Hero(jogo.hero.x, jogo.hero.y, 0, jogo.hero.dy), jogo.plat,)
    return jogo


'''
trata_solta_jogo: Jogo Tecla -> Jogo
'''
def trata_solta_tecla(hero, tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_RIGHT:
        return Hero(hero.x, hero.y, 0, 0)
    return hero

