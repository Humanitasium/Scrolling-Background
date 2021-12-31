import pygame
pygame.init()
width = 800
height= 600
win = pygame.display.set_mode((width, height))
bg_img = pygame.image.load("Assets/Background.png")
bg= pygame.transform.scale(bg_img, (width,height))
i=0
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    win.blit(bg, (i,0))
    win.blit(bg, (width+i, 0))
    if i == -width:
        win.blit(bg, (i+width,0))
        i=0
    i -= 5
    pygame.display.flip()
pygame.quit()

