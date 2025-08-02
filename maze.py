from pygame import *
class GameSpaite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))                            
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x  = player_x
        self.rect.y  = player_y
    def  reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSpaite):
    def update(self):

        keys_pressed = key.get_pressed()


        if keys_pressed[K_LEFT] and self.rect.x  > 5:
            self.rect.x  -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x  < win_width - 80:
            self.rect.x  += self.speed
        if keys_pressed[K_UP] and self.rect.y  > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x  < win_height - 80:
            self.rect.y += self.speed
class Enemy(GameSpaite):
    direct = "l"
    def update(self):
        if self.rect.x<=470:
            self.direct = "r"
        if self.rect.x>=win_width-85:    
            self.direct = "l"
        if self.direct == "l":
            self.rect.x -=self.speed
        else:
           self.rect.x +=self.speed    

class  Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_hidth):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.rect = self.image.get_rect()00
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.image = Surface((self.wall_width,self.wall_hidth))
        self.image.fill((color_1,color_2,color_3))
        self.wall_width = wall_width
        self.wall_hidth = wall_hidth
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.x)) #draw.rect(window,)(self.color_1,self.color_2,self.color_3),(self.rect.x,self.rect.y,self.wall_width,self.wall_hidth)
  

win_width = 700
win_hidth = 500
window = display.set_mode((win_width, win_hidth))
display.set_caption("лабиринт")
background = transform.scale(image.load("background.jpg"), (win_width,win_hidth))
x1 = 100
y1 = 300

monster = Enemy('cyborg.png',win_width - 80,280,4)
player = Player('hero.png',5,win_hidth-80,4)
final = GameSpaite('hero.png',win_hidth - 120,win_width - 80,0)
w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)


speed = 10
FPS = 60
clock = time.Clock()
run = True

font.init()
font = font.Font(None,70)
win = font.render("YOU WIN!", True,(255,215,0))
lose = font.render("YOU LOSER!", True,(180,0,0))



mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

x1 = 100
y1 = 300
fin = False
while run:
    
    
    for e in event.get():
        if e.type == QUIT:
            run = False
    if fin!=True:        
        window.blit(background,(0,0))
        player.update()
        monster.update()
        
        player.reset()
        monster.reset()
        fin.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

        if sprite.collide_rect(player,monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3):
            fin = True
            window.blit(lose,(200,200))
            kick.play()
        if sprite.collide_rect(player,final):
            fin = True
            window.blit(win,(200,200))
            money.play()












    display.update()
    clock.tick(FPS)    



