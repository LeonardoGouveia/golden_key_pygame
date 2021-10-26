from time import sleep
import pygame
from pygame import mixer
pygame.init()
pygame.mixer.init()


#ASPECTOS PRINCIPAIS DO GAME
sWidth = 800
sHeight = 600
icone = pygame.image.load('FOTOS/chave.icon2.png')
iconeTransformado = pygame.transform.scale(icone, (50,50))
screen = pygame.display.set_mode((sWidth, sHeight))
pygame.display.set_caption('Golden Key')
pygame.display.set_icon(iconeTransformado)
relogio = pygame.time.Clock()
pygame.mixer.music.load('MUSICAS/MUSICA_COMECO.mp3')
pygame.mixer.music.play(-1)


#TELA DE LOADING

telaIntro1 = pygame.image.load('FOTOS/tela de loading.png')
telaIntro1_1 = pygame.image.load('FOTOS/tela de loading.png')

#MOVIMENTAÇÃO/ INTRODUÇÃO

backg = pygame.image.load('FOTOS/parque.png')

cacaNiquel = pygame.image.load('FOTOS/cacaniquel.png')
cNTransformado = pygame.transform.scale(cacaNiquel, (110, 110))

andarEsq = pygame.image.load('FOTOS/menino esquerda.png')
esqTrans = pygame.transform.scale(andarEsq, (110, 110))

andarDir = pygame.image.load('FOTOS/ed andando direita.png')
dirTrans = pygame.transform.scale(andarDir, (110, 110))

parado = pygame.image.load('FOTOS/eddard parado.png')
paradoTrans= pygame.transform.scale(parado, (110, 110))

#FASE UM/ PRIMEIRO MINIGAME

eddardDir = pygame.image.load('FOTOS/ed andando direita.png')
direita = pygame.transform.scale(eddardDir, (30, 30))

eddardEsq = pygame.image.load('FOTOS/eddard esquerda.png')
esquerda = pygame.transform.scale(eddardEsq, (30, 30))

eddardCima = pygame.image.load('FOTOS/edCostas.png')
cima = pygame.transform.scale(eddardCima, (30, 30))

eddardBaixo = pygame.image.load('FOTOS/edFrente.png')
baixo = pygame.transform.scale(eddardBaixo, (30, 30))

mapa = pygame.image.load('FOTOS/mapa.png')
inimigo = pygame.image.load('FOTOS/goblin.png')

isildur = pygame.image.load('FOTOS/conversa 1.png')
isildurT = pygame.transform.scale(isildur, (120, 120))

#FASE DE TRANSIÇÃO

mapaT = pygame.image.load('FOTOS/mapatrans.png')

isildurC1 = pygame.image.load('FOTOS/isildur chat 2.png')
isildorChat1 = pygame.transform.scale(isildurC1, (400,400))

eddard_d_t = pygame.transform.scale(eddardDir, (80,80))
eddard_e_t = pygame.transform.scale(eddardEsq, (80,80))

#FASE FINAL
mapaF = pygame.image.load('FOTOS/fase final.png')

espada = pygame.image.load('FOTOS/espada.png')

valar = pygame.image.load('FOTOS/valar esq.png')
valarTrans = pygame.transform.scale(valar, (100,100))
#CLASSES - PERSONAGEM1/MUDANÇA DE FASES

class Player(object):
    def __init__(self, pos_x, pos_y, width, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
    def draw(self, window):
        if self.left:
            screen.blit(esqTrans, (self.pos_x, self.pos_y))
        elif self.right:
            screen.blit(dirTrans, (self.pos_x, self.pos_y))
        else:
            screen.blit(paradoTrans, (self.pos_x, self.pos_y))
    def mover(self, alvo):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and personagem1.pos_x < 700:
            personagem1.pos_x += personagem1.vel
            personagem1.right = True
            personagem1.left = False
        elif keys[pygame.K_LEFT] and personagem1.pos_x > 0:
            personagem1.pos_x -= personagem1.vel
            personagem1.right = False
            personagem1.left = True
        else:
            personagem1.left = False
            personagem1.right = False

personagem1 = Player(50, 403, 40, 20)

class Eddard(object):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def draw(self, window):
        if self.left:
            screen.blit(esquerda, (self.pos_x, self.pos_y))
        if self.right:
            screen.blit(direita, (self.pos_x, self.pos_y))
        if self.up:
            screen.blit(cima,(self.pos_x, self.pos_y))
        if self.down:
            screen.blit(baixo, (self.pos_x, self.pos_y))
    def mover(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            eddard.pos_x -= eddard.vel
            eddard.left = True
            eddard.right = False
            eddard.up = False
            eddard.down = False
        elif keys[pygame.K_RIGHT]:
            eddard.pos_x += eddard.vel
            eddard.left = False
            eddard.right = True
            eddard.up = False
            eddard.down = False
        elif keys[pygame.K_UP]:
            eddard.pos_y -= eddard.vel
            eddard.left = False
            eddard.right = False
            eddard.up = True
            eddard.down = False
        elif keys[pygame.K_DOWN]:
            eddard.pos_y += eddard.vel
            eddard.left = False
            eddard.right = False
            eddard.up = False
            eddard.down = True

eddard = Eddard(100, 60,)

class Goblin(object):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    def drawG(self):
        screen.blit(inimigo, (self.pos_x, self.pos_y))


class Goblin2(object):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    def drawG(self):
        screen.blit(inimigo, (self.pos_x, self.pos_y))


class Goblin3(object):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    def drawG(self):
        screen.blit(inimigo, (self.pos_x, self.pos_y))


goblin = Goblin(610, 530)
goblin3 = Goblin3(572, 323)
goblin2 = Goblin2(215, 473)

class EddardT():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    def drawT(self):
        if self.left:
            screen.blit(eddard_e_t, (self.pos_x, self.pos_y))
        if self.right:
            screen.blit(eddard_d_t, (self.pos_x, self.pos_y))
    def moverTrans(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.pos_x <= 750:
            eddard_transicao.pos_x += self.vel
            self.left = False
            self.right = True
        elif keys[pygame.K_LEFT] and self.pos_x > 0:
            self.left = True
            self.right = False
            eddard_transicao.pos_x -= self.vel


eddard_transicao = EddardT(100, 475)

class Eddard_Final():
    def __init__(self, pos_x, pos_y):
        self.image = pygame.image.load('FOTOS/ed andando direita.png')
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    def draw_Ed_f(self):
        if self.left:
            screen.blit(esquerda, (self.pos_x, self.pos_y))
        if self.right:
            screen.blit(direita, (self.pos_x, self.pos_y))
        if self.up:
            screen.blit(cima,(self.pos_x, self.pos_y))
        if self.down:
            screen.blit(baixo, (self.pos_x, self.pos_y))
    def mover_final(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and eddard_final.pos_x > 0:
            eddard_final.pos_x -= eddard.vel
            eddard_final.left = True
            eddard_final.right = False
            eddard_final.up = False
            eddard_final.down = False
        elif keys[pygame.K_RIGHT] and eddard_final.pos_x < 760:
            eddard_final.pos_x += eddard.vel
            eddard_final.left = False
            eddard_final.right = True
            eddard_final.up = False
            eddard_final.down = False
        elif keys[pygame.K_UP] and eddard_final.pos_y > 20:
            eddard_final.pos_y -= eddard.vel
            eddard_final.left = False
            eddard_final.right = False
            eddard_final.up = True
            eddard_final.down = False
        elif keys[pygame.K_DOWN] and eddard_final.pos_y < 530:
            eddard_final.pos_y += eddard.vel
            eddard_final.left = False
            eddard_final.right = False
            eddard_final.up = False
            eddard_final.down = True


eddard_final = Eddard_Final(100, 300)
class Espadas():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel = 5
        self.hitbox = (self.pos_x + 20, self.pos_y, 32, 70)
    def draw_espadas(self):
        screen.blit(espada, (self.pos_x, self.pos_y))
        self.hitbox = (self.pos_x + 20, self.pos_y, 32, 70)
        pygame.draw.rect(screen, (30, 30, 30), self.hitbox, 1)


class Valar():
    def __init__(self, pos_x, pos_y, end):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.end = end
        self.vel = 5
        self.caminho = [self.pos_y, self.end ]
        self.hitbox = (self.pos_x + 20, self.pos_y, 32, 70)
        self.cont = 0
    def drawValar(self):
        self.updateValar()
        screen.blit(valarTrans, (self.pos_x, self.pos_y))
        self.hitbox = (self.pos_x + 20, self.pos_y, 32, 70)
        pygame.draw.rect(screen, (30,30,30), self.hitbox, 1)
    def updateValar(self):
       if self.vel > 0:
           if self.pos_y + self.vel < self.caminho[1]:
               self.pos_y += self.vel
           else:
               self.vel *= -1
       else:
           if self.pos_y - self.vel > self.caminho[0]:
               self.pos_y += self.vel
           else:
               self.vel *= -1
    def hit(self):
        self.cont += 1


valarC = Valar(650, 100, 500)


class GameState():
    def __init__(self):
        self.state = 'intro1'
        self.goblins = 0
        self.run = True
    def intro1(self):
        relogio.tick(27)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                self.state = 'intro2'
        loading()
        pygame.display.flip()
    def intro2(self):
        relogio.tick(35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.state = 'tirinha1'
        intro()
        pygame.display.flip()
    def tirinhaUm(self):
        tirUm = pygame.image.load('FOTOS/TIRINHA 1.png')
        screen.blit(tirUm, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                self.state = 'main_game'
    def main_game(self):
        relogio.tick(35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        faseUm()
        enfeites_mapa()
        screen.blit(isildurT, (150, 60))
        if 610 <= eddard.pos_x <= 615 and 505 <= eddard.pos_y <= 540:
            morte = mixer.Sound('MUSICAS/inimigo morrendo.wav')
            morte.play()
            goblin.pos_x = 900
            sleep(0.2)
            self.goblins += 1
        if 565 <= eddard.pos_x <= 572 and 315 <= eddard.pos_y <= 330:
            morte = mixer.Sound('MUSICAS/inimigo morrendo.wav')
            morte.play()
            goblin3.pos_x = 900
            sleep(0.2)
            self.goblins += 1
        if 210 <= eddard.pos_x <= 220 and 480 <= eddard.pos_y <= 495:
            morte = mixer.Sound('MUSICAS/inimigo morrendo.wav')
            morte.play()
            goblin2.pos_x = 900
            sleep(0.2)
            self.goblins += 1
        if 6 <= self.goblins <= 10:
            sleep(0.5)
            self.state = 'Fora_Game'
        fonte = pygame.font.Font('texto/Minecrafter.Reg.ttf', 14)
        placar = fonte.render(f'Inimigos mortos x {self.goblins}', True, (255, 255, 255))
        screen.blit(placar, (560, 14))
        pygame.display.flip()
    def fora_Game(self):
        relogio.tick(40)
        faseSaida()
        pygame.display.flip()
        if eddard_transicao.pos_x >= 750:
            self.state = 'Fase_Final'
    def Fase_final(self):
        relogio.tick(50)
        fase_final()
        pygame.display.flip()
        if valarC.cont >= 20:
            self.state = 'scape'
    def scape(self):
        fundoFinal = pygame.image.load('FOTOS/tirinha 2.png')
        screen.blit(fundoFinal, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                self.state = 'tirinhaFinal'
    def tirinhaFinal(self):
        tirinhaF = pygame.image.load('FOTOS/Tirinha 3.png')
        screen.blit(tirinhaF, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                exit()
    def stateManager(self):
        if self.state == 'intro1':
            self.intro1()
        if self.state == 'intro2':
            self.intro2()
        if self.state == 'tirinha1':
            self.tirinhaUm()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'Fora_Game':
            mixer.music.stop()
            self.fora_Game()
        if self.state == 'Fase_Final':
            self.Fase_final()
        if self.state == 'scape':
            mixer.music.stop()
            self.scape()
        if self.state == 'tirinhaFinal':
            self.tirinhaFinal()



game_state = GameState()


#FUNÇÕES INSERIDAS NAS CLASSES
def loading():
    screen.blit(telaIntro1, (0,0))


def intro():
    screen.blit(backg, (0,0))
    screen.blit(cNTransformado, (700, 415))
    personagem1.draw(screen)
    personagem1.mover(personagem1)


goblins = 3


def contador(x, y):
    fonte = pygame.font.Font('texto/Minecrafter.Reg.ttf', 14)
    placar = fonte.render(f'Inimigos x {goblins}', True, (255,255,255))
    screen.blit(placar, (640, 14))
    pygame.display.flip()


def faseUm():
    screen.blit(mapa, (0,0))
    rectgroup()
    goblin.drawG()
    goblin2.drawG()
    goblin3.drawG()
    eddard.draw(screen)
    eddard.mover()


def rectgroup():
    #RETÂNGULOS DE COLISÃO
    rect = pygame.draw.rect(screen, (0, 0, 0), (550, 314, 23, 23))
    rect2 = pygame.draw.rect(screen, (0, 0, 0), (550, 338, 23, 23))
    rect3 = pygame.draw.rect(screen, (0, 0, 0), (573, 314, 23, 23))
    rect4 = pygame.draw.rect(screen, (0, 0, 0), (619, 287, 23, 23))
    rect5 = pygame.draw.rect(screen, (0, 0, 0), (619, 310, 23, 23))
    rect6 = pygame.draw.rect(screen, (0, 0, 0), (619, 333, 23, 23))

    rect7 = pygame.draw.rect(screen, (0, 0, 0), (330, 312, 23, 23))

    rect8 = pygame.draw.rect(screen, (0, 0, 0), (420, 88, 23, 23))
    rect9 = pygame.draw.rect(screen, (0, 0, 0), (420, 65, 23, 23))
    rect10 = pygame.draw.rect(screen, (0, 0, 0), (466, 35, 23, 23))
    rect11 = pygame.draw.rect(screen, (0, 0, 0), (466, 58, 23, 23))

    rect12 = pygame.draw.rect(screen, (0, 0, 0), (169, 411, 23, 23))
    rect13 = pygame.draw.rect(screen, (0, 0, 0), (219, 411, 23, 23))
    rect14 = pygame.draw.rect(screen, (0, 0, 0), (219, 463, 23, 23))
    rect15 = pygame.draw.rect(screen, (0, 0, 0), (269, 463, 23, 23))
    rect16 = pygame.draw.rect(screen, (0, 0, 0), (194, 488, 23, 23))
    rect17 = pygame.draw.rect(screen, (0, 0, 0), (219, 513, 23, 23))

    rect18 = pygame.draw.rect(screen, (139,69,19), (298, 387, 10, 25))


def enfeites_mapa():
    arvore1 = pygame.image.load('FOTOS/arvore 1.png')
    a1 = pygame.transform.scale(arvore1, (60,60))
    screen.blit(a1, (220, 170))
    screen.blit(a1, (80, 173))
    arvore2 = pygame.image.load('FOTOS/arvore 2.png')
    a2 = pygame.transform.scale(arvore2, (60, 60))
    screen.blit(a2, (150, 170))
    screen.blit(a2, (220, 140))
    pedra = pygame.image.load('FOTOS/pedra.png')
    screen.blit(pedra, (200, 200))
    screen.blit(pedra, (200, 180))
    dragao1 = pygame.image.load('FOTOS/dragão.png')
    drag = pygame.transform.scale(dragao1, (80,80))
    screen.blit(drag, (575, 400))


def faseSaida():
    mixer.music.load('MUSICAS/musicafundo.mp3')
    mixer.music.play(-1)
    screen.blit(mapaT, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    eddard_transicao.drawT()
    eddard_transicao.moverTrans()
    screen.blit(isildorChat1, (200, 150))

projecteis = []

def fase_final():
    espadasCont = 0
    if espadasCont > 0:
        espadasCont+= 1
    if espadasCont > 3:
        espadasCont = 0
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    for espadas in projecteis:
        if espadas.pos_y - 5 < valarC.hitbox[1] + valarC.hitbox[3] and espadas.pos_y + 5 > valarC.hitbox[1]:
            if espadas.pos_x + 5 > valarC.hitbox[0] and espadas.pos_x - 5 < valarC.hitbox[0] + valarC.hitbox[2]:
                valarC.hit()
                projecteis.pop(projecteis.index(espadas))
        if espadas.pos_x < 800 and espadas.pos_x > 0:
            espadas.pos_x += espadas.vel
        else:
            projecteis.pop(projecteis.index(espadas))
    screen.blit(mapaF, (0,0))
    eddard_final.draw_Ed_f()
    eddard_final.mover_final()
    if keys[pygame.K_SPACE] and espadasCont == 0:
        if len(projecteis) < 4:
            projecteis.append(Espadas(eddard_final.pos_x, eddard_final.pos_y))
        espadasCont = 1
    valarC.drawValar()
    for espadas in projecteis:
        espadas.draw_espadas()


run = True
while run:
    game_state.stateManager()
    pygame.display.flip()
