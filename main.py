import pygame
import time
import random

# Window size
SCREENWIDTH = 400
SCREEHEIGHT = 400
screen = pygame.display.set_mode((SCREENWIDTH, SCREEHEIGHT))
pygame.display.set_caption("Snake Game!")

pygame.init()

BLACK = 0, 0, 0
GREEN = 0, 255, 0
RED = 255, 0 , 0
PURPLE = 255, 0, 255

events = pygame.event

snakePos = [100, 50]
snakeBody = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]
snakeSpeed = 15
direction = 'DOWN'

fruitPos = [(random.randint(1,((SCREENWIDTH-10)/10))*10), (random.randint(1,((SCREEHEIGHT-10)/10))*10)]

fps = pygame.time.Clock()

score = 0

def die():
    myFont = pygame.font.SysFont('times new roman', 50)

    gameOverSurface = myFont.render("Game over.", True, RED)

    gameOverRect = gameOverSurface.get_rect()

    gameOverRect.center = [SCREENWIDTH/2, SCREEHEIGHT/2]

    screen.blit(gameOverSurface, gameOverRect)

    pygame.display.flip()

    time.sleep(4)

    pygame.quit()
    quit()
    
def scoring(score):
    scoreFont = pygame.font.SysFont('times new roman', 20)

    scoreSurface = scoreFont.render(f"Score: {score}", True, RED)

    scoreRect = scoreSurface.get_rect()

    # scoreRect.center = [SCREENWIDTH/2, SCREEHEIGHT/2]

    screen.blit(scoreSurface, scoreRect)

    pygame.display.flip()

running = True
# The loop that runs the game
while running:
    for event in events.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_s and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_a and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_d and direction != 'LEFT':
                direction = 'RIGHT'
    
    screen.fill(BLACK)
    scoring(score)

    pygame.draw.circle(screen, RED, [fruitPos[0]+5, fruitPos[1]+5], 5)
    # pygame.draw.rect(screen, RED, pygame.Rect(fruitPos[0],fruitPos[1], 10, 10))
    
    for pos in snakeBody:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    snakeBody.insert(0, list(snakePos))

    if snakePos[0] == fruitPos[0] and snakePos[1] == fruitPos[1]:
        fruitPos = [(random.randint(1,((SCREENWIDTH-10)/10))*10), (random.randint(1,((SCREEHEIGHT-10)/10))*10)]
        score +=1
    else: 
        snakeBody.pop()
    
    # Update the screen
    pygame.display.flip()

    fps.tick(snakeSpeed)

    if snakePos[0] < 0 or snakePos[0] > SCREENWIDTH:
        die()
    if snakePos[1] < 0 or snakePos[1] > SCREEHEIGHT:
        die()   

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            die()

pygame.quit()