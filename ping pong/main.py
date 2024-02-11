from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
      
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed



win_width = 700
win_height = 500

display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
ground = transform.scale(image.load("background.jpg"), (win_width, win_height))

ball = GameSprite("ball.png", 200, 200, 90,90,25)

Player1 = Player1("stolb1.jpg", 20, 200, 10, 90, 10)
Player2 = Player2("stolb1.jpg", 670, 200, 10, 90, 10)




run = True
finish = False

clock = time.Clock()
FPS = 60


speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 lose!', True, (180,0,0))
lose2 = font1.render('Player 2 lose!', True, (180,0,0))

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    if ball.rect.y>win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    
    if sprite.collide_rect(Player1, ball) or sprite.collide_rect(Player2, ball):
        speed_x *= - 1

    if not finish:

        window.blit(ground, (0, 0))

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))

        ball.rect.x += speed_x
        ball.rect.y += speed_y
    



        Player1.reset()
        Player2.reset()
        ball.reset()

        ball.update()        
        Player1.update()
        Player2.update()
        display.update()

    clock.tick(FPS)