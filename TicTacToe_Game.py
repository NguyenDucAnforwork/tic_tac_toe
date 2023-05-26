import pygame
import random
import time
pygame.init()

# Basic setup
pygame.display.set_caption('TicTacToe')
screen = pygame.display.set_mode((600, 700))
running = True
clock = pygame.time.Clock()
pausing = False
winner = -1
winner_side = -1
draw = True
pau_draw = False

#color

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)

#loading the images
opening = pygame.image.load('tic tac opening.png')
x_img = pygame.image.load('X.png')
o_img = pygame.image.load('O.png')
print(x_img)
print(o_img)
print(opening)
#resizing images
x_img = pygame.transform.scale(x_img, (180,180))
o_img = pygame.transform.scale(o_img, (180,180))
opening = pygame.transform.scale(opening, (600, 700))

font_small = pygame.font.SysFont('sans', 50)
font_big = pygame.font.SysFont('sans', 120)
'''text_x = font_big.render(x_img, True, WHITE)
text_o = font_big.render(o_img, True, WHITE)'''

# Biến lưu trạng thái xem đến lượt X hay O và hashmap lưu xem ô nào đã được đến thăm. 
# Quy ước: X là 1, O là 2

turn = 0
visited = {}
for i in range(3):
    for j in range(3):
        visited[(i, j)] = 0

#opening stage
clock.tick(60)
screen.blit(opening, (0, 0))
pygame.display.update()
time.sleep(1)
#start the loop

while running:

    
    
    screen.fill(WHITE)

    # Draw board
    for i in range(2):
        pygame.draw.line(screen, BLACK, (200 * (i + 1), 0), (200 * (i + 1), 600), 7)
    for i in range(2):
        pygame.draw.line(screen, BLACK, (0, 200 * (i + 1)), (600, 200 * (i + 1)), 7)
    pygame.draw.rect(screen, BLACK, (0,600,600,100))
    
    # Draw current position
    for i in range(3):
        for j in range(3):
            
            if visited[(i, j)] == 1:
                screen.blit(x_img, (200 * i, 200 * j))
            if visited[(i, j)] == 2:
                screen.blit(o_img, (200 * i, 200 * j))
        
   
    # Check crash
    for i in range(3):
        if visited[(0,i)] == visited[(1,i)] and visited[(1,i)] == visited[(2,i)] and visited[(0,i)] > 0:
            pausing = True
            winner = visited[(0,i)]
            pygame.draw.line(screen, RED, (50, 200*i+100),(550,200*i+100), 7)
    
    for i in range(3):
        if visited[(i,0)] == visited[(i,1)] and visited[(i,1)] == visited[(i,2)] and visited[(i,0)] > 0:
            pausing = True
            winner = visited[(i,0)]
            pygame.draw.line(screen, RED, (200*i+100, 50),(200*i+100,550), 7)
    
    if visited[(0,0)] == visited[(1,1)] and visited[(1,1)] == visited[(2,2)] and visited[(1,1)] > 0:
        pausing = True
        winner = visited[(1,1)]
        pygame.draw.line(screen, RED, (50,50),(550,550), 7)
    
    if visited[(0,2)] == visited[(1,1)] and visited[(1,1)] == visited[(2,0)] and visited[(1,1)] > 0:
        pausing = True
        winner = visited[(1,1)]
        pygame.draw.line(screen, RED, (550,50),(50,550), 7)
    
    #check draw condition
    # Check draw condition
    draw = True
    for i in range(3):
        for j in range(3):
            if visited[(i, j)] == 0:
                draw = False
                break
        

    
    if draw and not pausing:
        draw_txt = font_small.render("Draw! Play again!", True, WHITE)
        screen.blit(draw_txt, (150,620))
        pau_draw = True
    
    #check termination condition
    
    if pausing == True:
        if(winner == 1):
            winner_side = 'X'
        elif(winner == 2):
            winner_side = 'O'
        winner_txt = font_small.render("winner is: " + str(winner_side), True, WHITE)
        screen.blit(winner_txt, (200,620))                             

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos_x = int(event.pos[0] / 200)
                pos_y = int(event.pos[1] / 200)
                print(pos_x, pos_y)

                #swap turn
                
                if visited[(pos_x, pos_y)] == 0:
                    if turn == 0:
                        visited[(pos_x, pos_y)] = 1
                        turn = 1
                    elif turn == 1:
                        visited[(pos_x, pos_y)] = 2
                        turn = 0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pausing == True or pau_draw == True:
                    pausing = False
                    pau_draw = False
                    for i in range(3):
                        for j in range(3):
                            visited[(i, j)] = 0
                    
    pygame.display.flip()
    

pygame.quit()
