#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
import random

IMAGEM = circulo(50,Cor(96, 219, 211))









ALTURA, LARGURA = 600,600
tela = criar_tela_base(ALTURA, LARGURA)

DX = 7
G = 1

METADE_L_HERO = largura_imagem(IMAGEM) // 2
METADE_A_HERO = altura_imagem(IMAGEM) // 2
METADE_L_ENEMY = largura_imagem(IMAGEM) // 2
METADE_A_ENEMY = altura_imagem(IMAGEM) // 2
METADE_L_PLAT = altura_imagem(IMAGEM) // 2
METADE_A_PLAT = altura_imagem(IMAGEM) // 2


LIMITE_ESQUERDO = METADE_L_HERO
LIMITE_DIREITO = LARGURA - METADE_L_HERO
LIMITE_CIMA = METADE_A_HERO
LIMITE_BAIXO = ALTURA - METADE_A_HERO

CHAO = LIMITE_BAIXO


Hero = definir_estrutura("hero", "x, y, dx, dy", mutavel=True)
''' Hero pode ser formado da seguinte forma: Hero(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[-LARGURA, +LARGURA])
interp. representa a posição do herói no eixo x e y, e sua velocidadee direção (dx e dy)
'''
#EXEMPLOS:
HERO_INICIAL = Hero(LARGURA//2, ALTURA//2, 0, 0)



'''
desenha_hero: Hero -> Imagem
Desenha o herói'''
def desenha_hero(hero):
    colocar_imagem(IMAGEM, tela, hero.x, hero.y)


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
def trata_solta_tecla(hero, tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_RIGHT:
        return Hero(hero.x, hero.y, 0, 0)
    return hero


def main(inic):
    big_bang(inic, tela=tela,
             frequencia=60,
             quando_tick=mover_hero,
             desenhar=desenha_hero,
             quando_tecla=trata_tecla_hero,
             quando_solta_tecla=trata_solta_tecla,
             modo_debug= True
             )

main(HERO_INICIAL)

