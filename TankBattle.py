import pygame
import random
import math


pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255,255,0)
lightblue = (173, 216, 230)
darkgreen = (0, 75, 0)


TANK_WIDTH = 70
TANK_HEIGHT = 45
TANK_SPEED = 5
BARREL_WIDTH = 10
BARREL_HEIGHT = 20


BULLET_SPEED = 7


STONE_WIDTH = 30
STONE_HEIGHT = 30
STONE_SPAWN_INTERVAL = 2500  # in milliseconds

BOOSTER_SPAWN_INTERVAL = 10000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Battle Game")


#baackgrd
background_image = pygame.image.load("background.jpeg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

#indian flag
india_pic = pygame.image.load("Flag_of_India.png")  # Replace with the actual path to your image
india_pic = pygame.transform.scale(india_pic, (30, 20))  # Resize if necessary


font = pygame.font.Font(None, 36)

class Tank(pygame.sprite.Sprite):
    # def __init__(self):
    #     super().__init__()
    #     self.image = pygame.Surface((TANK_WIDTH, TANK_HEIGHT))
    #     self.image.fill(black)
    #     self.rect = self.image.get_rect()
    #     self.rect.centerx = SCREEN_WIDTH // 2
    #     self.rect.bottom = SCREEN_HEIGHT
    #     self.speed = TANK_SPEED

    # def update(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_LEFT]:
    #         self.rect.x -= self.speed
    #     if keys[pygame.K_RIGHT]:
    #         self.rect.x += self.speed
    #     # Ensure the tank stays within screen bounds
    #     if self.rect.left < 0:
    #         self.rect.left = 0
    #     if self.rect.right > SCREEN_WIDTH:
    #         self.rect.right = SCREEN_WIDTH
    # def __init__(self):
    #     super().__init__()
    #     self.image = pygame.Surface((TANK_WIDTH, TANK_HEIGHT + BARREL_HEIGHT), pygame.SRCALPHA)
    #     self.image.fill((0, 0, 0, 0))  # Fill with transparent color
    #     self.rect = self.image.get_rect()
    #     self.rect.centerx = SCREEN_WIDTH // 2
    #     self.rect.bottom = SCREEN_HEIGHT
    #     self.speed = TANK_SPEED
    #     self.draw_tank()

    # def draw_tank(self):
    #     pygame.draw.rect(self.image, darkgreen, (0, BARREL_HEIGHT, TANK_WIDTH, TANK_HEIGHT))
    #     pygame.draw.rect(self.image, black, ((TANK_WIDTH // 2) - (BARREL_WIDTH // 2), 0, BARREL_WIDTH, BARREL_HEIGHT))

    # def update(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_LEFT]:
    #         self.rect.x -= self.speed
    #     if keys[pygame.K_RIGHT]:
    #         self.rect.x += self.speed
    #     # Ensure the tank stays within screen bounds
    #     if self.rect.left < 0:
    #         self.rect.left = 0
    #     if self.rect.right > SCREEN_WIDTH:
    #         self.rect.right = SCREEN_WIDTH
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TANK_WIDTH, TANK_HEIGHT + BARREL_HEIGHT), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # Fill with transparent color
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT
        self.speed = TANK_SPEED
        self.draw_tank()

    def draw_tank(self):
        pygame.draw.rect(self.image, darkgreen, (0, BARREL_HEIGHT, TANK_WIDTH, TANK_HEIGHT))
        pygame.draw.rect(self.image, black, ((TANK_WIDTH // 2) - (BARREL_WIDTH // 2), 0, BARREL_WIDTH, BARREL_HEIGHT))
        # Blit the small picture onto the tank
        self.image.blit(india_pic, (TANK_WIDTH // 2 - india_pic.get_width() // 2, BARREL_HEIGHT + TANK_HEIGHT // 2 - india_pic.get_height() // 2))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # Ensure the tank stays within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, hitpoint):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED
        self.hitpoint = hitpoint
        # self.image = pygame.image.load('missile1.png').convert_alpha()
        # aeroplane_image = pygame.image.load("missile1.png")
        # aeroplane_image = pygame.transform.scale(aeroplane_image, (50, 50))
        # self.image = aeroplane_image

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

class Stone(pygame.sprite.Sprite):
    def __init__(self, x, y, number,speed):
        super().__init__()
        self.image = pygame.Surface(( random.randint(30, 70) , random.randint(30, 70)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.number = number
        if self.number%3 == 0:
            self.image.fill(green)
        elif self.number%3 == 1:
            self.image.fill(blue)
        else :
            self.image.fill(red)

    def update(self):
        self.rect.y += self.speed
        if self.number%3 == 0:
            self.image.fill(green)
        elif self.number%3 == 1:
            self.image.fill(blue)
        else :
            self.image.fill(red)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.speed *= -1
            self.rect.y += self.speed
        elif ((self.rect.top < 0) & (self.speed < 0.0)):
            self.speed *= -1
            self.rect.y += self.speed
            
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        text = font.render(str(self.number), True, black)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

class Booster(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        super().__init__()
        self.image = pygame.Surface((30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.number = number
        self.image.fill(yellow)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        text = font.render(str(self.number), True, black)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
    
def show_start_screen():
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    # title_text = font.render('Hello!', True, black)
    prompt_text = small_font.render('Press Enter to Start the Game', True, black)

    # title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT -50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Exit the start screen

        # screen.fill(lightblue)
        screen.blit(background_image, (0, 0))
        # screen.blit(title_text, title_rect)
        screen.blit(prompt_text, prompt_rect)
        pygame.display.flip()        
    
    
def show_game_over_screen():
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    game_over_text = font.render('Game Over!!', True, red)
    prompt_text = small_font.render('Press Enter to Restart', True, black)
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 - 50))
    prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show_start_screen()
                    main()
                    return  # Exit the game over screen

        screen.blit(background_image, (0, 0))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(prompt_text, prompt_rect)
        pygame.display.flip()

# Main game function
def main():
    clock = pygame.time.Clock()
    # user starting interface:
    

    tank = Tank()
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    stones = pygame.sprite.Group()
    boosters = pygame.sprite.Group()
    all_sprites.add(tank)

    # Stone spawning event
    hitpoint = 1
    
    speed = 1
    
    SPAWNSTONE = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWNSTONE, STONE_SPAWN_INTERVAL)

    INCSPEED = pygame.USEREVENT + 2
    pygame.time.set_timer(INCSPEED, 6000)
    
    SPAWNBOOSTER = pygame.USEREVENT + 3
    pygame.time.set_timer(SPAWNBOOSTER, BOOSTER_SPAWN_INTERVAL)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == SPAWNBOOSTER:
                x = random.randint(0, SCREEN_WIDTH - 70)
                y = -STONE_HEIGHT
                number = random.randint(4, 5)
                booster = Booster(x, y, number)
                all_sprites.add(booster)
                boosters.add(booster)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == INCSPEED:
                speed*=1.175    
            elif event.type == SPAWNSTONE:
                x = random.randint(0, SCREEN_WIDTH - STONE_WIDTH)
                y = -STONE_HEIGHT
                number = random.randint(1, 8)
                stone = Stone(x, y, number,speed)
                all_sprites.add(stone)
                stones.add(stone)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(tank.rect.centerx, tank.rect.top, hitpoint)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        all_sprites.update()

        # Check for bullet-stone collisions
        for bullet in bullets:
            hits = pygame.sprite.spritecollide(bullet, stones, False)
            for stone in hits:
                stone.number -= bullet.hitpoint
                bullet.kill()
                if stone.number <= 0:
                    stone.kill()
        
        for bullet in bullets:
            hits = pygame.sprite.spritecollide(bullet, boosters, False)
            for booster in hits:
                booster.number -= 1
                bullet.kill()
                if booster.number <= 0:
                    booster.kill()
                    hitpoint+=2
                    
        if pygame.sprite.spritecollide(tank, stones, False):
            running = False  # End the game if the tank collides with a stone
            show_game_over_screen()
            
        screen.blit(background_image, (0, 0))
        # screen.fill(white)
        all_sprites.draw(screen)
        for stone in stones:
            stone.draw(screen)
        for booster in boosters:
            booster.draw(screen)
        
        
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
show_start_screen()
if __name__ == "__main__":
    main()
