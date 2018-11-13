#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
import random

ALTURA, LARGURA = 600,600
tela = criar_tela_base(ALTURA, LARGURA)

Hero = definir_estrutura("hero", "x, y, dx, dy", mutavel=True)

def desenha_jogo(jogo):
    if (not jogo.game_over):
        desenha_hero(jogo.hero)
        desenha_enemy(jogo.enemy)
    else:
        desenha_game_over()


'''
desenha_hero: Hero -> Imagem
Desenha o herói'''
def desenha_hero(hero):
    if hero.dx >= 0:
        '''colocar_imagem(Imagem, tela, hero.x, hero.y, hero.dx, hero.dy)'''
        #colocar_imagem(IMG_VACA_INO, tela, vaca.x, Y_VACA)
    else:
        '''colocar_imagem(Imagem, tela, hero.x, hero.y, hero.dx, hero.dy)'''