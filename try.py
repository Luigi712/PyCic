# import the pygame module, so you can use it
import pygame
import time

def move_x(xpos, step_x):
    return xpos + step_x

def move_y(ypos, step_y):
    return ypos + step_y



# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800,800))
    image = pygame.image.load("asset/hasb.png")
    image = pygame.transform.scale(image,(100,100))
    pygame.display.flip()

    xpos = 50
    ypos = 50
    # how many pixels we move our smiley each frame
    step_x = 15
    step_y = 15
    screen_width=800
    screen_height=800
    # check if the smiley is still on screen, if not change direction
    change_to = 'RIGHT'
    

     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        if change_to=='RIGHT':
            xpos = move_x(xpos, step_x)
        if change_to=='UP':
            ypos = move_y(ypos, -step_y)
        if change_to=='LEFT':
            xpos = move_x(xpos, -step_x)
        if change_to=='DOWN':
            ypos = move_y(ypos, step_y)

        #Controlli per non superare il bordo, da sostituire con game over
        if xpos>screen_width-64 or xpos<0:
            step_x = -step_x
        if ypos>screen_height-64 or ypos<0:
            step_y = -step_y
        time.sleep(0.05)
        # update the position of the smiley
        # xpos += step_x # move it to the right
        screen.fill(0)
        
        
        screen.blit(image, (xpos,ypos))
        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if change_to == 'RIGHT':
                        pass
                    else:
                        change_to = 'LEFT'
                if event.key == pygame.K_d:
                    if change_to == 'LEFT':
                        pass
                    else:
                        change_to = 'RIGHT'
                if event.key == pygame.K_s:
                    if change_to == 'UP':
                        pass
                    else: 
                        change_to = 'DOWN'
                if event.key == pygame.K_w:
                    if change_to =='DOWN':
                        pass
                    else:
                        change_to = 'UP'
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()