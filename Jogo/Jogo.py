#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
import random

ALTURA, LARGURA = 600,600
tela = criar_tela_base(ALTURA, LARGURA)

LIMITE_ESQUERDO = 20
LIMITE_DIREITO = LARGURA-20
LIMITE_CIMA = 20
LIMITE_BAIXO = ALTURA-20

METADE_L_HERO = largura_imagem(IMAGEM) // 2
METADE_A_HERO = altura_imagem(IMAGEM) // 2
METADE_L_ENEMY = largura_imagem(IMAGEM) // 2
METADE_A_ENEMY = altura_imagem(IMAGEM) // 2

'''================================================================================================'''
''' ==================================== [DEFINIÇÃO DE DADOS] ====================================='''
'''================================================================================================'''


Hero = definir_estrutura("hero", "x, y, dx, dy", mutavel=True)
''' Hero pode ser formado da seguinte forma: Hero(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[-LARGURA, +LARGURA])
interp. representa a posição do herói no eixo x e y, e sua velocidadee direção (dx e dy)
'''
#EXEMPLOS:
HERO_INICIAL = Hero(LIMITE_ESQUERDO//2, LIMITE_DIREITO//2)

##TEMPLATE
'''
def fn_para_hero(hero):
    ... hero.x
        hero.y
        hero.dx
        hero.dy
'''

Enemy = definir_estrutura("enemy", "x, y, dx, dy", mutavel=True)
''' Enemy pode ser formado como: Enemy(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[LIMITE_CIMA, LIMITE_BAIXO], Int)
interp. representa a posição do inimigo no eixo, x, y, e velocidade e direção (dx e dy) 
'''
#EXEMPLOS:
ENEMY_INICIAL = Enemy(LARGURA//2, LIMITE_CIMA, 3)

##TEMPLATE
'''
def fn_para_enemy(enemy):
    if enemy.x < LIMITE_ESQUERDO or enemy.x > LIMITE_DIREITO: #VALIDAÇÃO
        raise ValueError("ERRO: inimigo invalido (x está fora dos limites)")
    #COLOCAR VALIDACAO ṔARA Y
    ... enemy.x
        enemy.dx
        enemy.y
        enemy.dy
'''

'''
ListaEnemy é um desses:
    - VAZIA
    - juntar(enemy, ListaEnemy)
'''
#Exemplos:
L_ENEMY_1 = [ENEMY_INICIAL]
L_ENEMY_INICIAL = [
    Enemy(LARGURA//4, LIMITE_CIMA, 3),
    Enemy(LARGURA//2, ALTURA//2, 3),
    Enemy(LARGURA//2 + LARGURA//4, LIMITE_BAIXO, 3)]

'''
#template
def fn_para_lista(lista):
    if lista.vazia:
        return ...
    else:
        ... lista.primeiro
            fn_para_lista(lista.resto)
'''

Jogo = definir_estrutura("Jogo", "hero, enemy, game_over, enemy_time, point", mutavel=True)
''' Jogo pode ser formado assim: Jogo(Hero, ListaEnemy, Boolean, Int+)
interp. representa o jogo todo com um herói e zero ou mais inimigos. O campo game_over indica se o jogo está acabado ou não.
'''
#EXEMPLOS:
JOGO_INICIAL = Jogo(HERO_INICIAL, [], False, 0, 0, 1)

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
    if (not jogo.game_over):
        desenha_hero(jogo.hero)
        desenha_enemies(jogo.enemy)
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


'''
desenha_enemy: Enemy -> Imagem
Desenha o inimigo na posicao'''
def desenha_enemy(enemy):
    colocar_imagem(IMG, tela, enemy.x, enemy.y)


'''
desenha_enemy: ListEnemy -> Imagem
Desenha os inimigos
'''
def desenha_enemies(enemy):
    for ene in enemy:
        desenha_enemy(enemy)


'''
desenha_plat: ListPlat -> Imagem
Desenha as plataformas
'''
def desenha_plat(plat):
    '''for ene in enemy:
        desenha_enemy(enemy)'''
    colocar_imagem(Imagem, tela, 300, 550)



''' ------------ [MOVE] ------------'''

'''
mover_tudo: Jogo -> Jogo
Produz o próximo estado do jogo
'''
def mover_tudo(jogo):
    if (not colide_algum_churras (jogo.vaca, jogo.churrasqueiros)):
        mover_vaca(jogo.vaca)   ##funcao helper (auxiliar)
        if vaca_atingiu_alvo(jogo.vaca, ALVOS[jogo.proximo_alvo]):
            jogo.pontuacao += 10
            # novo_alvo = (jogo.proximo_alvo + 1) % len(ALVOS)
            jogo.proximo_alvo = random.randrange(0, len(ALVOS))

        mover_churrasqueiros(jogo.churrasqueiros)  ##funcao helper
        jogo.tempo_brotagem_churras = (jogo.tempo_brotagem_churras + 1) % (TEMPO_CADA_BROTAGEM * FREQUENCIA)
        if (jogo.tempo_brotagem_churras == 0):
            jogo.churrasqueiros.append(criar_churras_aleatorio())

        return jogo
    else:
        jogo.game_over = True
        return jogo

'''
mover_hero: Hero -> Hero
Move o Herói'''
def mover_hero(hero):
    nextx = hero.x + hero.dx
    nexty = hero.y + hero.dy
    if nextx > LIMITE_DIREITO or nextx < LIMITE_ESQUERDO:
        hero.dx = -hero.dx
        return hero
    elif nexty > LIMITE_BAIXO or nexty< LIMITE_CIMA:
        hero.dy = -hero.dy
        return hero
    return hero


'''
mover_enemy: Enemy -> Enemy
Move o Inimigo'''
def mover_enemy(enemy):
    nextx = enemy.x + enemy.dx
    nexty = enemy.y + enemy.dy
    if nextx > LIMITE_DIREITO or nextx < LIMITE_ESQUERDO:
        enemy.dx = -enemy.dx
        return enemy
    elif nexty > LIMITE_BAIXO or nexty< LIMITE_CIMA:
        enemy.dy = -enemy.dy
        return enemy
    return enemy


''' ------------ [COLISÃO] ------------'''

'''
colidem: Hero, Enemy -> Boolean
Verifica se o herói e o inimigo colidiram
'''
def colidem(vaca, churras):
    esquerda_vaca = vaca.x - METADE_L_VACA
    direita_vaca = vaca.x + METADE_L_VACA
    cima_vaca = Y_VACA - METADE_H_VACA
    baixo_vaca = Y_VACA + METADE_H_VACA

    enemyL = enemy.x - METADE_L_CHURRAS
    enemyR = enemy.x + METADE_L_CHURRAS
    enemyU = enemy.y - METADE_H_CHURRAS
    enemyD = enemy.y + METADE_H_CHURRAS

    return direita_vaca >= esquerda_churras and \
        esquerda_vaca <= direita_churras and \
        baixo_vaca >= cima_churras and \
        cima_vaca <= baixo_churras