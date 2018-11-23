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
METADE_L_PLAT = largura_imagem(PLAT) // 2
METADE_A_PLAT = altura_imagem(PLAT) // 2


LIMITE_ESQUERDO = METADE_L_HERO
LIMITE_DIREITO = LARGURA - METADE_L_HERO
LIMITE_CIMA = METADE_A_HERO
LIMITE_BAIXO = ALTURA - METADE_A_HERO

CHAO = LIMITE_BAIXO
COLIDE = False

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

Plataformas = definir_estrutura("plataformas", "x, y", mutavel=True)
''' Plat pode ser formado da seguinte forma: Plat(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[-LARGURA, +LARGURA])
interp. representa a posição da plataforma no eixo x e y
'''
#EXEMPLOS:
PLAT_INICIAL = Plataformas(LARGURA//2, (ALTURA//2 + ALTURA //4))

##TEMPLATE
'''
def fn_para_plat(plat):
    ... plat.x
        plat.y
'''
'''
ListaPlat é um desses:
    - VAZIA
    - juntar(Plataformas, ListaPlat)
'''
#Exemplos:



Jogo = definir_estrutura("Jogo", "hero, plataformas", mutavel=True)
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
    desenha_plataformas(jogo.plataformas)
    desenha_hero(jogo.hero)
    '''if (not jogo.game_over):
        desenha_hero(jogo.hero)
        desenha_enemies(jogo.enemy)
    else:
        desenha_game_over()'''


'''
desenha_plat: Plat -> Imagem
Desenha a plataforma'''
def desenha_plat(plataformas):
    colocar_imagem(PLAT, tela, plataformas.x, plataformas.y)

'''
desenha_plataformas: ListPlat -> Imagem
Desenha todas as Plataformas
'''
def desenha_plataformas(plataformas):
    for plataformas in plataformas:
        desenha_plat(plataformas)

'''
desenha_hero: Hero -> Imagem
Desenha o herói'''
def desenha_hero(hero):
    colocar_imagem(IMAGEM, tela, hero.x, hero.y)









''' ------------ [MOVE] ------------'''
'''
mover_tudo: Jogo -> Jogo
Produz o próximo estado do jogo 
'''
def mover_tudo(jogo):
    global COLIDE
    if colide_plataforma(jogo.hero, jogo.plataformas):
        COLIDE = True
        jogo.hero.dy = 0

    if (not colide_plataforma(jogo.hero, jogo.plataformas)):
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
def colide_plat(hero, plataformas):
    '''Hit Box - Herói'''
    heroL = hero.x - METADE_L_HERO
    heroR = hero.x + METADE_L_HERO
    heroU = hero.y - METADE_A_HERO
    heroD = hero.y + METADE_A_HERO

    '''Hit Box - Plataforma'''
    platL = plataformas.x - METADE_L_PLAT
    platR = plataformas.x + METADE_L_PLAT
    platU = plataformas.y - METADE_A_PLAT
    platD = plataformas.y + METADE_A_PLAT

    return heroR >= platL and \
           heroL <= platR and \
           heroD >= platU and \
           heroU <= platD

'''
colide_plataforma: Hero, ListaChurras -> Boolean
'''
def colide_plataforma(hero, plataformas):
    for plat in plataformas:
        if colide_plat(hero, plataformas):
            return True
    return False









''' ------------ [TRATA TECLA] ------------'''


'''
trata_tecla_jogo: Jogo, Tecla -> Jogo
Trata tecla para o jogo todo.
'''
def trata_tecla_jogo(jogo, tecla):
    hero_novo = trata_tecla_hero(jogo.hero, tecla)
    return Jogo(hero_novo, jogo.plataformas)


'''
trata_tecla: Hero, Tecla -> Hero
Faz o herói se movimentar para a direita ou esquerda, ou pular
'''
def trata_tecla_hero(hero, tecla):
    global COLIDE
    if tecla == pg.K_UP and COLIDE:
        COLIDE = False
        hero.y -= 20
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
        return Jogo(Hero(jogo.hero.x, jogo.hero.y, 0, jogo.hero.dy), jogo.plataformas)
    return jogo











'''
Jogo -> Jogo
inicie o mundo com JOGO_INICIAL
'''
def main(inic):
    big_bang(inic,  # Jogo
             tela=tela,
             frequencia=60,
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