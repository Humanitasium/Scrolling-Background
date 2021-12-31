import pygame #imports the pygame module
pygame.init() #initalizes the pygame module
width = 800
height= 600
win = pygame.display.set_mode((width, height)) #sets the display size
bg_img = pygame.image.load("Background.png") #loads the image
bg= pygame.transform.scale(bg_img, (width,height)) #scales the image to fit the display size
i=0
run=True
while run: #while loop
    for event in pygame.event.get(): #quits the program
        if event.type == pygame.QUIT:
            run=False #exits the while loop
    win.blit(bg, (i,0)) #displays the starting image
    win.blit(bg, (width+i, 0)) 
    '''
    displays the image again
    but further along to give the impression 
    of a seamless never ending background
    '''
    if i == -width: 
    '''
    once a full loop of the image has been completed
    the position of the image is reset
    '''
        win.blit(bg, (i+width,0))
        i=0
    i -= 5 # sets the speed of the loop
    pygame.display.flip() #updates display
pygame.quit() 

