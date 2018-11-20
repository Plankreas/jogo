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

CHAO = LIMITE_BAIXO

DX = 3

METADE_L_HERO = largura_imagem(IMAGEM) // 2
METADE_A_HERO = altura_imagem(IMAGEM) // 2
METADE_L_ENEMY = largura_imagem(IMAGEM) // 2
METADE_A_ENEMY = altura_imagem(IMAGEM) // 2
METADE_L_PLAT = altura_imagem(IMAGEM) // 2
METADE_A_PLAT = altura_imagem(IMAGEM) // 2


'''================================================================================================'''
''' ==================================== [DEFINIÇÃO DE DADOS] ====================================='''
'''================================================================================================'''


Hero = definir_estrutura("hero", "x, y, dx, dy", mutavel=True)
''' Hero pode ser formado da seguinte forma: Hero(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[-LARGURA, +LARGURA])
interp. representa a posição do herói no eixo x e y, e sua velocidadee direção (dx e dy)
'''
#EXEMPLOS:
HERO_INICIAL = Hero(LIMITE_ESQUERDO, LIMITE_BAIXO, 0, 0)

##TEMPLATE
'''
def fn_para_hero(hero):
    ... hero.x
        hero.y
        hero.dx
        hero.dy
'''

Enemies = definir_estrutura("enemies", "x, y, dx, dy", mutavel=True)
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

Jogo = definir_estrutura("Jogo", "hero, enemies, game_over, enemy_time, point", mutavel=True)
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
def desenha_enemies(enemies):
    for ene in enemies:
        desenha_enemy(enemies)


'''
desenha_plat: ListPlat -> Imagem
Desenha as plataformas
'''
def desenha_plat(plat):
    '''for ene in enemy:
        desenha_enemy(enemy)'''
    colocar_imagem(Imagem, tela, 300, 550)


def desenha_game_over():
    texto_game_over = texto("GAME OVER", Fonte("comicsans", 50), Cor("red"))
    colocar_imagem(texto_game_over, tela, LARGURA//2, ALTURA//2)



''' ------------ [MOVE] ------------'''

'''
mover_tudo: Jogo -> Jogo
Produz o próximo estado do jogo #############################################################################???
'''
def mover_tudo(jogo):
    if (not colide_enemies (jogo.hero, jogo.enemies)):
        mover_hero(jogo.hero)   ##funcao helper (auxiliar)
        if vaca_atingiu_alvo(jogo.vaca, ALVOS[jogo.proximo_alvo]):
            jogo.pontuacao += 10
            # novo_alvo = (jogo.proximo_alvo + 1) % len(ALVOS)
            jogo.proximo_alvo = random.randrange(0, len(ALVOS))

            mover_enemies(jogo.enemies)  ##funcao helper
        jogo.tempo_brotagem_churras = (jogo.enemy_time + 1) % (TEMPO_CADA_BROTAGEM * FREQUENCIA)
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
    nextx = hero.x + DX
    nexty = hero.y + hero.dy
    if nextx > LIMITE_DIREITO or nextx < LIMITE_ESQUERDO:
        hero.dx = 0
        return hero
    elif nexty > LIMITE_BAIXO or nexty< LIMITE_CIMA:
        hero.dy = -hero.dy
        return hero
    if hero.y == CHAO:
        hero.dy = 0
    else:
        hero.dy += G
        hero.y += hero.dy

        if hero.y >= CHAO:
            hero.y = CHAO
            hero.dy = 0
    return hero

'''
mover_enemy: Enemy -> Enemy
Move o Inimigo'''
def mover_enemy(enemy):
    nextx = enemy.x + enemy.dx
    if nextx > LIMITE_DIREITO or nextx < LIMITE_ESQUERDO:
        enemy.dx = -enemy.dx
        return enemy
    if enemy.y == CHAO:
        enemy.dy = 0
    else:
        enemy.dy += G
        enemy.y += enemy.dy

        if enemy.y >= CHAO:
            enemy.y = CHAO
            enemy.dy = 0
    return enemy

'''
mover_enemies: ListEnemy -> ListEnemy
'''
def mover_enemies(enemies):
    return [mover_enemy(enemy) for ene in enemy ]


''' ------------ [COLISÃO] ------------'''

'''
colidem: Hero, Enemy -> Boolean
Verifica se o herói e o inimigo colidiram
'''
def colidem(hero, enemy):
    heroL = hero.x - METADE_L_HERO
    heroR = hero.x + METADE_L_HERO
    heroU = hero.y - METADE_A_HERO
    heroD = hero.y + METADE_A_HERO

    enemyL = enemy.x - METADE_L_ENEMY
    enemyR = enemy.x + METADE_L_ENEMY
    enemyU = enemy.y - METADE_A_ENEMY
    enemyD = enemy.y + METADE_A_ENEMY

    return heroR >= enemyL and \
           heroL <= enemyR and \
           heroD >= enemyU and \
           heroU <= enemyD

'''
colide_enemies: Hero, ListEnemy -> Boolean
'''
def colide_enemies(hero, enemies):
    for ene in enemies:
        if colidem(hero, enemy):
            return True
    return False


''' ------------ [TRATA TECLA] ------------'''

'''
trata_tecla_jogo: Jogo, Tecla -> Jogo
Trata tecla para o jogo todo.
'''
def trata_tecla_jogo(jogo, tecla):
    if (not jogo.game_over):
        hero_novo = trata_tecla_hero(jogo.hero, tecla)
        return Jogo(hero_novo, jogo.enemies, jogo.game_over, jogo.enemy_time)''', jogo.pontuacao, jogo.proximo_alvo)'''
    elif tecla == pg.K_RETURN:
        return criar_jogo_inicial()
    else:
        return jogo


'''
trata_solta_jogo: Jogo Tecla -> Jogo
'''
def trata_solta_jogo(jogo, tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_RIGHT:
        return Jogo(Hero(jogo.hero.x, 0), jogo.enemies, jogo.game_over, jogo.enemy_time)''', jogo.pontuacao, jogo.proximo_alvo)'''
    return jogo


'''
trata_tecla: Hero, Tecla -> Hero
Faz o herói se movimentar para a direita ou esquerda, ou pular
'''
def trata_tecla_hero(hero, tecla):
    if tecla == pg.K_UP and hero.y == CHAO:
        hero.y -= 10
        hero.dy = -20
    elif tecla == pg.K_RIGHT:
        hero.dx = DX
    elif tecla == pg.K_LEFT:
        hero.dx = -DX
    return hero



''' ------------ [OUTROS] ------------'''

'''
Reinicia o jogo
'''
def criar_jogo_inicial():
    return Jogo(HERO_INICIAL, [], False, 0, 0, 1)

'''
criar_enemies: -> Enemies
'''
def criar_enemies():
    return Enemies(random.randrange(LIMITE_ESQUERDO, LIMITE_DIREITO+1),
                         random.randrange(LIMITE_CIMA, LIMITE_BAIXO + 1),
                         random.randrange(-5, 6),
                         random.randrange(-5, 6))
