from pygame import *

font.init()



class sSprite(sprite.Sprite):
    def __init__(self, kakapukaimage, x, y, speed=1, l=75, h=50):
        super().__init__()
        self.image = transform.scale(image.load(kakapukaimage), (l, h))
        self.step = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(sSprite):
    def update(self):

        
        key_pressed = key.get_pressed()

        if key_pressed[K_a] and self.rect.x>5:
            self.rect.x -= self.step
        if key_pressed[K_d] and self.rect.x<length-75:
            self.rect.x += self.step
        if key_pressed[K_w] and self.rect.y>5:
            self.rect.y -= self.step
        if key_pressed[K_s] and self.rect.y<high-55:
            self.rect.y += self.step
    
    def unupdate(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_d] and self.rect.x>5:
            self.rect.x -= self.step
        if key_pressed[K_a] and self.rect.x<length-75:
            self.rect.x += self.step
        if key_pressed[K_s] and self.rect.y>5:
            self.rect.y -= self.step
        if key_pressed[K_w] and self.rect.y<high-55:
            self.rect.y += self.step

class Enemy(sSprite):
    def update(self, x1=400+100+150+100, x2=1280-125): #length
        if self.rect.x >= x2 or self.rect.x <= x1:
            self.step = -self.step
        self.rect.x += self.step

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.image = Surface((wall_width, wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))









length = 1280
high = 700
window = display.set_mode((length, high))
display.set_caption("Лабиринт")
background = transform.scale(image.load("Steam.jpeg"), (length, high)) 



step = 10

clock = time.Clock()
FPS = 75




Gaben1 = Player("Gaben.png", 5, high-55, step)
Gaben2 = Player("Gaben.png", length-75, 5, step)
monster = Enemy("Heavy.png", length-380, high-200, step/2, 100, 100)
monster2 = Enemy("Heavy.png", 125, 200-100, step/2, 100, 100)
final = sSprite("treasure.png", length-75, high-50)
final2 = sSprite("treasure.png", length-75, 5)







w1 = Wall(154, 205, 50, 0, high/2, length, 10) #центр
#w2 = Wall(154, 205, 50, 400, high/2+150, 350, 10)
w2 = Wall(154, 205, 50, 400, high/2+150, 100, 10)#1 стенка со второй дыркой
w3 = Wall(154, 205, 50, 200, high/2+250, 10, high-(high/2+250))#1 стенка с первой дыркой
w4 = Wall(154, 205, 50, length-200, high/2-(high-(high/2+250)), 10, high-(high/2+250))#2 стенка с первой дыркой
w5 = Wall(154, 205, 50, length-400, high/2-150, 10, 150)#1 ограда второй дырки
w6 = Wall(154, 205, 50, length-400-350, 0, 10, high-(high/2+150))#2 ограда второй дырки
w7 = Wall(154, 205, 50, 400+100+150, high/2+150, 100, 10)#2 стенка второй дырки


game = True








#
mixer.init() 
mixer.music.load("jungles.ogg") 
mixer.music.play()


kick = mixer.Sound("kick.ogg") 
money = mixer.Sound("money.ogg")



font = font.SysFont("Arial", 70)
win = font.render("YOU WIN!", True, (255, 215, 0))
lose = font.render("YOU LOSE!", True, (180, 0, 0))
Restart = font.render('press "R" to restart game', True, (180, 0, 0))



finish = False
flag = False


while game:
    
    


    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYUP:
            if e.key == K_r: 
                finish = False
                flag = False
                Gaben1.rect.x = 5
                Gaben1.rect.y = high-55
                Gaben2.rect.x = length-75
                Gaben2.rect.y = 5


    if finish != True:
        
        window.blit(background, (0, 0))
        Gaben1.update()
        Gaben2.unupdate()
        monster.update()
        monster2.update(0, length-400-350-100)

        Gaben1.reset()
        Gaben2.reset()
        monster.reset()
        monster2.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

        if sprite.collide_rect(Gaben1, monster) or sprite.collide_rect(Gaben1, w1) or sprite.collide_rect(Gaben1, w2) or sprite.collide_rect(Gaben1, w3) or sprite.collide_rect(Gaben1, w7) or  sprite.collide_rect(Gaben2, w1) or sprite.collide_rect(Gaben2, w4) or sprite.collide_rect(Gaben2, w5) or sprite.collide_rect(Gaben2, w6) or sprite.collide_rect(Gaben2, monster2):
            finish = True
            kick.play()
            window.blit(lose, (length/2-100, high/2))
            window.blit(Restart, (length/2-250, high/2+50))

        
        if flag:
            final2.reset()
            if sprite.collide_rect(Gaben2, final2):
                money.play()
                window.blit(win, (length/2-100, high/2))
        else:
            final.reset()
            if sprite.collide_rect(Gaben1, final):
                money.play()
                flag = True

    clock.tick(FPS)
    display.update() 













window.blit(background, (0, 0))