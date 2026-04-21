import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader - Part 1")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

score = 0
font = pygame.font.SysFont("Arial", 32)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

player = Sprite(BLUE, 50, 50)
player.rect.x = SCREEN_WIDTH // 2
player.rect.y = SCREEN_HEIGHT - 70

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

for i in range(7):
    enemy = Sprite(RED, 40, 40)
    enemy.rect.x = random.randint(0, SCREEN_WIDTH - 40)
    enemy.rect.y = random.randint(0, SCREEN_HEIGHT // 2)
    enemies.add(enemy)
    all_sprites.add(enemy)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.x > 0:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT] and player.rect.x < SCREEN_WIDTH - 50:
        player.rect.x += 5
    if keys[pygame.K_UP] and player.rect.y > 0:
        player.rect.y -= 5
    if keys[pygame.K_DOWN] and player.rect.y < SCREEN_HEIGHT - 50:
        player.rect.y += 5

    hit_list = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hit_list:
        score += 1

    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()