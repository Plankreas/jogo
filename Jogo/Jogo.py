#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Jogo_Const_Dados import *


'''================================================================================================'''
''' ========================================== [FUNÇÕES] =========================================='''
'''================================================================================================'''




''' ------------------------ [DESENHA] ------------------------'''

'''
desenha_jogo: Jogo -> Imagem
Desenha todos os elementos do jogo de acordo com o estado atual
'''
def desenha_jogo(jogo):
    colocar_imagem(FUNDO, tela, LARGURA // 2, ALTURA // 2)
    desenha_pontos(jogo)
    if (not jogo.game_over):
        colocar_imagem(MISC1, tela, (LARGURA - LARGURA // 8), (ALTURA // 2 - 60))
        colocar_imagem(MISC3, tela, (LARGURA // 8), (ALTURA - 60))
        colocar_imagem(MISC2, tela, (LARGURA // 2 - 40), (ALTURA // 4 - 55))

        desenha_plataformas(jogo.plataformas)
        desenha_inimigos(jogo.inimigos)
        desenha_hero(jogo.hero)
    else:
        desenha_game_over()


'''
desenha_hero: Hero -> Imagem
Desenha o herói'''
def desenha_hero(hero):
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

    if Wcont + 1 >= 24:
        Wcont = 0
    if hero.dy == 0 and hero.dx != 0 and Right:
        colocar_imagem(WalkR[Wcont // 3], tela, hero.x, hero.y)
        Wcont += 1
    if hero.dy == 0 and hero.dx != 0 and Left:
        colocar_imagem(WalkL[Wcont // 3], tela, hero.x, hero.y)
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
Desenha a plataforma.
'''
def desenha_plat(plat):
    colocar_imagem(PLAT_IMG, tela, plat.x, plat.y)


def desenha_plataformas(plataformas):
    for plat in plataformas:
        desenha_plat(plat)

'''
desenha_enemy: Enemy -> Imagem
Desenha o iminigo.
'''
def desenha_enemy(enemy):
    '''colocar_imagem(ENEMY, tela, enemy.x, enemy.y)'''
    global Econt
    if Econt + 1 >= 80:
        Econt = 0
    if enemy.dx == EDX:
        colocar_imagem(WalkER[Econt // 20], tela, enemy.x, enemy.y)
        Econt += 1
    if enemy.dx == -EDX:
        colocar_imagem(WalkEL[Econt // 20], tela, enemy.x, enemy.y)
        Econt += 1
    if enemy.dy > 0 and enemy.dz == 1:
        colocar_imagem(FallER, tela, enemy.x, enemy.y)
        Econt += 1
    if enemy.dy > 0 and enemy.dz == 0:
        colocar_imagem(FallEL, tela, enemy.x, enemy.y)
        Econt += 1

def desenha_inimigos(inimigos):
    for enemy in inimigos:
        desenha_enemy(enemy)


'''
desenha_game_over: Jogo -> Imagem
Desenha a tela de Game Over.
'''
def desenha_game_over():
    texto_game_over = texto("GAME OVER", Fonte("comicsans", 50), Cor("white"), (LARGURA//2))
    colocar_imagem(texto_game_over, tela, (LARGURA//2), (ALTURA//2))


def desenha_pontos(jogo):
    pontos = texto("Pontuação: ", Fonte("comicsans", 25), Cor("white"), (LARGURA))
    colocar_imagem(pontos, tela, 50, 25)
    ponto = texto(str(jogo.pontos), Fonte("comicsans", 25), Cor("white"), (LARGURA))
    px = largura_imagem(pontos)
    colocar_imagem(ponto,tela,px + 25, 25)






''' ------------------------ [MOVE] ------------------------'''
'''
mover_tudo: Jogo -> Jogo
Produz o próximo estado do jogo 
'''
def mover_tudo(jogo):
    global COLIDE

    if not (colide_inimigos(jogo.hero, jogo.inimigos) or caiu(jogo.hero)):
        if colide_plataformas(jogo.hero, jogo.plataformas):
            COLIDE = True
        if (not colide_plataformas(jogo.hero, jogo.plataformas)):
            COLIDE = False

        colide_enemies(jogo.inimigos, jogo.plataformas)

        if matou_inimigos(jogo.hero, jogo.inimigos):
            jogo.pontos += 10

        mover_hero(jogo.hero)
        mover_inimigos(jogo.inimigos)
        caiu_inimigo(jogo.inimigos)
        jogo.tempo_inimigos = (jogo.tempo_inimigos + 1) % 50
        if (jogo.tempo_inimigos == 0):
            jogo.inimigos.append(criar_inimigo())
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

    if COLIDE:
        hero.dy = 0

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
        enemy.dx = -enemy.dx
        if enemy.dz == 1:
            enemy.dz = 0
        else:
            enemy.dz = 1

    if enemy.x < LIMITE_ESQUERDO:
        enemy.x = LIMITE_ESQUERDO
        enemy.dx = -enemy.dx
        if enemy.dz == 1:
            enemy.dz = 0
        else:
            enemy.dz = 1

    return enemy

def mover_inimigos(inimigos):
    for enemy in inimigos:
        mover_enemy(enemy)





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

    return heroR >= platL and heroL <= platR and (heroD + 5) >= platU and heroU <= platD


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

    return enemyR >= platL and enemyL <= platR and (enemyD + 10) >= platU and enemyU <= platD


def colide_enemies(inimigos, plataformas):
    for enemy in inimigos:
        if colide_plataformas_inimigos(enemy, plataformas):
            enemy.dy = 0
            if enemy.dz == 1:
                enemy.dx = EDX
            else:
                enemy.dx = -EDX
        else:
            enemy.dy += G
            enemy.dx = 0


def colide_plataformas_inimigos(enemy, plataformas):
    for plat in plataformas:
        if colide_plat_enemy(enemy, plat):
            return True
    return False


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
    heroA = hero.y + METADE_A_HERO - 20

    '''Hit Box - Inimigo'''
    enemyL = enemy.x - METADE_L_ENEMY
    enemyR = enemy.x + METADE_L_ENEMY
    enemyU = enemy.y - METADE_A_ENEMY
    enemyD = enemy.y + METADE_A_ENEMY

    if heroR >= enemyL and heroL <= enemyR and heroD >= enemyU and heroU <= enemyD and heroA <= enemyU:
        return False

    return heroR >= enemyL and heroL <= enemyR and heroD >= enemyU and heroU <= enemyD





def colide_inimigos(hero, inimigos):
    for enemy in inimigos:
        if morreu(hero, enemy):
            return True
    return False

def matou(hero, enemy):
    '''Hit Box - Herói'''
    heroL = hero.x - METADE_L_HERO
    heroR = hero.x + METADE_L_HERO
    heroU = hero.y - METADE_A_HERO
    heroD = hero.y + METADE_A_HERO
    heroA = hero.y + METADE_A_HERO - 20

    '''Hit Box - Inimigo'''
    enemyL = enemy.x - METADE_L_ENEMY
    enemyR = enemy.x + METADE_L_ENEMY
    enemyU = enemy.y - METADE_A_ENEMY
    enemyD = enemy.y + METADE_A_ENEMY

    if heroR >= enemyL and heroL <= enemyR and heroD >= enemyU and heroU <= enemyD and heroA <= enemyU:
        INIMIGOS.remove(enemy)
        hero.y -= 20
        hero.dy -= 20
        return True

def matou_inimigos(hero, inimigos):
    for enemy in inimigos:
        if matou(hero, enemy):
            return True
    return False

'''
morreu: Hero, Enemy -> Boolean
Verifica se o inimigo matou o herói por contato.
'''
def caiu(hero):
    '''Hit Box - Herói'''
    heroU = hero.y - METADE_A_HERO

    return heroU >= CHAO


def caiu_enemy(enemy):
    '''Hit Box - Inimigo'''
    enemyU = enemy.y - METADE_A_ENEMY

    if enemyU >= CHAO:
        INIMIGOS.remove(enemy)


def caiu_inimigo(inimigos):
    for enemy in inimigos:
        caiu_enemy(enemy)








''' ------------ [OUTROS] ------------'''


def criar_jogo_inicial():
    return Jogo(Hero(LARGURA//2, ALTURA//2, 0, 0), INIMIGOS, PLATAFORMAS, False, 0,0)

def criar_inimigo():
    return Enemy(random.randrange(LIMITE_ESQUERDO, LIMITE_DIREITO + 1),
                 0 - ALTURA // 2,
                 0,
                 0,
                 random.randrange(0, 2))



''' ------------ [TRATA TECLA] ------------'''


'''
trata_tecla_jogo: Jogo, Tecla -> Jogo
Trata tecla para o jogo todo.
'''
def trata_tecla_jogo(jogo, tecla):
    if (not jogo.game_over):
        hero_novo = trata_tecla_hero(jogo.hero, tecla)
        return Jogo(hero_novo, jogo.inimigos, jogo.plataformas, False, jogo.tempo_inimigos,jogo.pontos)
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
        return Jogo(Hero(jogo.hero.x, jogo.hero.y, 0, jogo.hero.dy), jogo.inimigos, jogo.plataformas, False, jogo.tempo_inimigos,jogo.pontos)
    return jogo

