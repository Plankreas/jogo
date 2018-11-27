#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
import random

IMAGEM = circulo(25,Cor(94, 198, 196))
PLAT = retangulo(200,35,Cor(103, 133, 131))
ENEMY = circulo(25,Cor(215, 89, 127))

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
METADE_L_ENEMY = largura_imagem(ENEMY) // 2
METADE_A_ENEMY = altura_imagem(ENEMY) // 2
METADE_L_PLAT = largura_imagem(PLAT) // 2
METADE_A_PLAT = altura_imagem(PLAT) // 2


LIMITE_ESQUERDO = METADE_L_HERO
LIMITE_DIREITO = LARGURA - METADE_L_HERO
LIMITE_CIMA = METADE_A_HERO
LIMITE_BAIXO = ALTURA - METADE_A_HERO

CHAO = LIMITE_BAIXO
COLIDE = False
COLIDE_ENEMY = False

Right = True
Left = False

'''================================================================================================'''
''' ==================================== [DEFINIÇÃO DE DADOS] ====================================='''
'''================================================================================================'''


Hero = definir_estrutura("hero", "x, y, dx, dy", mutavel=True)
''' Hero pode ser formado da seguinte forma: Hero(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[-LARGURA, +LARGURA])
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


Enemy = definir_estrutura("enemy", "x, y, dx, dy", mutavel=True)
''' Enemy pode ser formado da seguinte forma: Enemy(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[-LARGURA, +LARGURA])
interp. representa a posição do inimigo no eixo x e y, e sua velocidade e direção (dx e dy)
'''
#EXEMPLOS:
ENEMY_INICIAL = Enemy(LARGURA//2, 0, 0, 0)

##TEMPLATE
'''
def fn_para_enemy(enemy):
    ... enemy.x
        enemy.y
        enemy.dx
        enemy.dy
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


'''
ListaEnemy é um desses:
    - VAZIA
    - juntar(enemy, ListaEnemy)
'''
#Exemplos:
L_PLAT_1 = [PLAT_INICIAL]
L_PLAT_INICIAL = [
    Plat(LARGURA//4, ALTURA//4),
    Plat(LARGURA//2, ALTURA//2 + ALTURA//4),
    Plat(LARGURA//2 + LARGURA//4, ALTURA//4)]

'''
#template
def fn_para_lista(lista):
    if lista.vazia:
        return ...
    else:
        ... lista.primeiro
            fn_para_lista(lista.resto)
'''

Jogo = definir_estrutura("Jogo", "hero, enemy, plataformas, game_over", mutavel=True)
''' Jogo pode ser formado assim: Jogo(Hero, ListaEnemy, Boolean, Int+)
interp. representa o jogo todo com um herói, zero ou mais inimigos, e plataformas. O campo game_over indica se o jogo está acabado ou não.
'''
#EXEMPLOS:
JOGO_INICIAL = Jogo(HERO_INICIAL, ENEMY_INICIAL, L_PLAT_INICIAL, False)

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
        desenha_plat(jogo.plataformas)
        desenha_enemy(jogo.enemy)
        desenha_hero(jogo.hero)
    else:
        desenha_game_over()


'''
desenha_hero: Hero -> Imagem
Desenha o herói'''
def desenha_hero(hero):
    colocar_imagem(IMAGEM, tela, hero.x, hero.y)


'''
desenha_plat: Plat -> Imagem
Desenha a plataforma.
'''
def desenha_plat(plat):
    colocar_imagem(PLAT, tela, plat.x, plat.y)


'''
desenha_enemy: Enemy -> Imagem
Desenha o iminigo.
'''
def desenha_enemy(enemy):
    colocar_imagem(ENEMY, tela, enemy.x, enemy.y)


'''
desenha_game_over: Jogo -> Imagem
Desenha a tela de Game Over.
'''
def desenha_game_over():
    texto_game_over = texto("GAME OVER", Fonte("comicsans", 50), Cor("red"), (LARGURA//2))
    colocar_imagem(texto_game_over, tela, (LARGURA//2), (ALTURA//2))


''' ------------ [MOVE] ------------'''
'''
mover_tudo: Jogo -> Jogo
Produz o próximo estado do jogo 
'''
def mover_tudo(jogo):
    global COLIDE
    global COLIDE_ENEMY

    if not (morreu(jogo.hero, jogo.enemy) or caiu(jogo.hero)):
        if colide_plataformas(jogo.hero, jogo.plataformas):
            COLIDE = True
            jogo.hero.dy = 0
        if (not colide_plataformas(jogo.hero, jogo.plataformas)):
                COLIDE = False
        if colide_plataformas_enemy(jogo.enemy, jogo.plataformas):
            COLIDE_ENEMY = True
            jogo.enemy.dy = 0
        if (not colide_plataformas_enemy(jogo.enemy, jogo.plataformas)):
            COLIDE_ENEMY = False

        mover_hero(jogo.hero)
        mover_enemy(jogo.enemy)
        return jogo
    else:
        jogo.game_over = True
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


'''
mover_enemy: Enemy -> Enemy
Move o inimigo.
'''
def mover_enemy(enemy):
    enemy.x = enemy.x + enemy.dx
    enemy.y = enemy.y + enemy.dy

    if enemy.x > LIMITE_DIREITO:
        enemy.x = LIMITE_DIREITO
        enemy.dx -= enemy.dx
    elif enemy.x < LIMITE_ESQUERDO:
        enemy.x = LIMITE_ESQUERDO
        enemy.dx -= enemy.dx

    if COLIDE_ENEMY:
        enemy.dy = 0
        enemy.dx = DX or -DX
    else:
        enemy.dy += G
        enemy.dx = 0
    return enemy



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


def colide_plataformas(hero, plataformas):
    for plat in plataformas:
        if colide_plat(hero, plat):
            return True
    return False



'''
colide_plat_enemy: v, Plat -> Boolean
Verifica se o herói colidiu com a Plataforma.
'''
def colide_plat_enemy(enemy, plat):
    '''Hit Box - Inimigo'''
    enemyL = enemy.x - METADE_L_ENEMY
    enemyR = enemy.x + METADE_L_ENEMY
    enemyU = enemy.y - METADE_A_ENEMY
    enemyD = enemy.y + METADE_A_ENEMY

    '''Hit Box - Plataforma'''
    platL = plat.x - METADE_L_PLAT
    platR = plat.x + METADE_L_PLAT
    platU = plat.y - METADE_A_PLAT
    platD = plat.y + METADE_A_PLAT

    return enemyR >= platL and \
           enemyL <= platR and \
           enemyD >= platU and \
           enemyU <= platD


def colide_plataformas_enemy(enemy, plataformas):
    for plat in plataformas:
        if colide_plat_enemy(enemy, plat):
            return True

'''
morreu: Hero, Enemy -> Boolean
Verifica se o inimigo matou o herói por contato.
'''
def morreu(hero, enemy):
    '''Hit Box - Herói'''
    heroL = hero.x - METADE_L_HERO
    heroR = hero.x + METADE_L_HERO
    heroU = hero.y - METADE_A_HERO
    heroD = hero.y + METADE_A_HERO

    '''Hit Box - Inimigo'''
    enemyL = enemy.x - METADE_L_ENEMY
    enemyR = enemy.x + METADE_L_ENEMY
    enemyU = enemy.y - METADE_A_ENEMY
    enemyD = enemy.y + METADE_A_ENEMY

    return heroR >= enemyL and \
           heroL <= enemyR and \
           heroD >= enemyU and \
           heroU <= enemyD


'''
morreu: Hero, Enemy -> Boolean
Verifica se o inimigo matou o herói por contato.
'''
def caiu(hero):
    '''Hit Box - Herói'''
    heroU = hero.y - METADE_A_HERO

    return heroU >= CHAO

''' ------------ [OUTROS] ------------'''


def criar_jogo_inicial():
    return Jogo(HERO_INICIAL, ENEMY_INICIAL, PLAT_INICIAL, False)



''' ------------ [TRATA TECLA] ------------'''


'''
trata_tecla_jogo: Jogo, Tecla -> Jogo
Trata tecla para o jogo todo.
'''
def trata_tecla_jogo(jogo, tecla):
    if (not jogo.game_over):
        hero_novo = trata_tecla_hero(jogo.hero, tecla)
        return Jogo(hero_novo, jogo.enemy, jogo.plat, False)
    elif tecla == pg.K_SPACE:
        return criar_jogo_inicial()
    else:
        return jogo


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
        return Jogo(Hero(jogo.hero.x, jogo.hero.y, 0, jogo.hero.dy), jogo.enemy, jogo.plat, False)
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