from pygame import *
from random import randint
font.init()

window = display.set_mode((1260, 500))
win_width = 1260
win_height = 500
display.set_caption("Пекмен")
icon = image.load("pacmen.png")
display.set_icon(icon)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, width, height, player_x, player_y, player_speed = 0):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.dir = 'UP'
        self.directions = ["RIGHT", "DOWN", "UP"]

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, 40, 40, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_image), (40, 40))
        self.image_left = transform.scale(image.load("pacman_left.png"), (40, 40))
        self.image_right = self.image
        self.image_up = transform.scale(image.load("pacman_up.png"), (40, 40))
        self.image_down = transform.scale(image.load("pacman_down.png"), (40, 40))
        self.sated = False

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.dir = "LEFT"
            self.image = self.image_left

        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.dir = "RIGHT"
            self.image = self.image_right

        if keys[K_UP] and self.rect.y > 5:
            self.dir = "UP"
            self.image = self.image_up
        
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.dir = "DOWN"
            self.image = self.image_down
        
        if self.dir == "LEFT":
            self.rect.x -= self.speed
        
        elif self.dir == "RIGHT":
            self.rect.x += self.speed

        elif self.dir == "UP":
            self.rect.y -= self.speed

        elif self.dir == "DOWN":
            self.rect.y += self.speed
        
        elif self.dir == "OFF":
            self.rect.y = self.rect.y
            self.rect.x = self.rect.x

        collide_list =  sprite.spritecollide(self, walls, False)
        for wall in collide_list:
            if self.dir == "UP":
                self.rect.y = wall.rect.bottom
                self.dir = "OFF"
            elif self.dir == "RIGHT":
                self.rect.right = wall.rect.left
                self.dir = "OFF"
            elif self.dir == "DOWN":
                self.rect.bottom = wall.rect.top
                self.dir = "OFF"
            elif self.dir == "LEFT":
                self.rect.left = wall.rect.right
                self.dir = "OFF"
         
        collide_list2 =  sprite.spritecollide(self, fruits, True)
        for fruit in collide_list2:
            self.sated = True


class Enemy(GameSprite):
    def update(self):

        if self.dir == "LEFT":
            self.rect.x -= self.speed
        
        elif self.dir == "RIGHT":
            self.rect.x += self.speed

        elif self.dir == "UP":
            self.rect.y -= self.speed

        elif self.dir == "DOWN":
            self.rect.y += self.speed
        
        collide_list =  sprite.spritecollide(self, walls, False)
        for wall in collide_list:
            n = randint(0, 2)
            if self.dir == "UP":
                self.rect.y = wall.rect.bottom
                self.dir = ["RIGHT", "DOWN", "LEFT"][n]
            elif self.dir == "RIGHT":
                self.rect.right = wall.rect.left
                self.dir = ["DOWN", "LEFT", "UP"][n]
            elif self.dir == "DOWN":
                self.rect.bottom = wall.rect.top
                self.dir = ["RIGHT", "UP", "LEFT"][n]
            elif self.dir == "LEFT":
                self.rect.left = wall.rect.right
                self.dir = ["RIGHT", "DOWN", "UP"][n]

class Wall(sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.inner = Surface((self.width - 10, self.height - 10))
        self.inner.fill((0, 0, 0))
        self.color = (2, 108, 207)
        self.image = Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(self.color)

    def update(self):
        self.image.blit(self.inner, (5, 5))
        window.blit(self.image, (self.rect.x, self.rect.y))

class Fruits(sprite.Sprite):
    def __init__(self, fruits_x, fruits_y):
        super().__init__()
        self.image = transform.scale(image.load("Fruits.png"), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = fruits_x
        self.rect.y = fruits_y
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall1 = Wall(1260, 30, 0, 0)
wall2 = Wall(1260, 30, 0, 470)
wall3 = Wall(30, 180, 0, 0)
wall4 = Wall(30, 180, 0, 320)
wall5 = Wall(30, 180, 1230, 0)
wall6 = Wall(30, 180, 1230, 320)
wall7 = Wall(120, 30, 0, 150)
wall8 = Wall(120, 30, 0, 320)
wall9 = Wall(120, 30, 1140, 150)
wall10 = Wall(120, 30, 1140, 320)
wall11 = Wall(45, 30, 75, 75)
wall12 = Wall(200, 52, 165, 75)
wall13 = Wall(52, 275, 165, 75)
wall14 = Wall(200, 52, 165, 298)
wall15 = Wall(52, 127, 313, 223)
wall16 = Wall(103, 30, 262, 223)
wall17 = Wall(445, 30, 410, 75)
wall18 = Wall(200, 52, 410, 150)
wall19 = Wall(52, 200, 410, 150)
wall20 = Wall(52, 200, 558, 150)
wall21 = Wall(200, 52, 410, 298)
wall22 = Wall(200, 52, 655, 150)
wall23 = Wall(52, 200, 655, 150)
wall24 = Wall(52, 200, 803, 150)
wall25 = Wall(200, 52, 655, 298)
wall26 = Wall(195, 30, 900, 75)
wall27 = Wall(30, 105, 900, 150)
wall28 = Wall(30, 105, 1065, 150)
wall29 = Wall(195, 30, 900, 225)
wall30 = Wall(67, 30, 75, 395)
wall31 = Wall(223, 30, 187, 395)
wall32 = Wall(30, 105, 455, 395)
wall33 = Wall(325, 30, 530, 395)
wall34 = Wall(30, 75, 900, 440)
wall35 = Wall(30, 75, 975, 350)
wall36 = Wall(195, 30, 900, 350)
wall37 = Wall(30, 75, 1065, 440)
wall38 = Wall(45, 30, 1140, 395)
wall39 = Wall(45, 30, 1140, 75)
walls = sprite.Group()
walls.add(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20,
wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30,
wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39)
fruit1 = Fruits(30, 75)
fruit2 = Fruits(1185, 75)
fruit3 = Fruits(30, 425)
fruit4 = Fruits(1185, 425)
fruit5 = Fruits(275, 253)
fruits = sprite.Group()
fruits.add(fruit1, fruit2, fruit3, fruit4, fruit5)
pl = Player("pacmen.png", 975, 430, 3)
enemy1 = Enemy("hero.png", 40, 40, 600, 100, 3)
enemy2 = Enemy("hero.png", 40, 40, 500, 100, 3)
enemys = sprite.Group()
enemys.add(enemy1, enemy2)
start_button = GameSprite("button_star.png", 200, 50, 500, 250)
font1 = font.SysFont("Impact", 50)
end_text = font1.render("GAME OVER", True, (255, 0, 0))

run = True
game_finished = False
clock = time.Clock()
game = False
while run:
    window.fill((0, 0, 0))
    
    for e in event.get():
        if e.type == QUIT:
            run = False

    pl.reset()
    enemys.draw(window)
    walls.update()

    if not game:
        start_button.reset()
        click = mouse.get_pressed()
        if click[0] and start_button.rect.collidepoint(mouse.get_pos()):
            game = True

    if game and not game_finished:
        pl.update()
        enemys.update()
        fruits.update()
        collide_list3 = sprite.spritecollide(pl, enemys, False)
        for enemy in collide_list3:
            if pl.sated:
                enemy.kill()
            else:
                game_finished = True
        if len(enemys) == 0:   
            end_text = font1.render("YOU WIN", True, (0, 255, 0))
            game_finished = True


    if game_finished:
        window.blit(end_text, (500, 250))

    display.update()
    clock.tick(60)