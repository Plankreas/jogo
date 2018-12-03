#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Jogo import *

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
             )

main(JOGO_INICIAL)