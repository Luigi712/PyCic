# import the pygame module, so you can use it
import pygame
import time
import random


def move_x(xpos, step_x):
    return xpos + step_x

def move_y(ypos, step_y):
    return ypos + step_y

def showscore(screen_width, screen_height,screen):
    my_font = pygame.font.SysFont('times new roman', 20)
    game_over_surface = my_font.render(
      'e perz, premi Q per uscire, SPACE per ricominciare', True,pygame.Color(255, 0, 0))
    game_over_rect = game_over_surface.get_rect()
     
    
    game_over_rect.midtop = (screen_width/2, screen_height/4)
     
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

def gameover(screen_width, screen_height,screen):
     # creazione del testo
            my_font = pygame.font.SysFont('times new roman', 20)
            game_over_surface = my_font.render(
            'e perz, premi Q per uscire, SPACE per ricominciare', True,pygame.Color(255, 0, 0))
            game_over_rect = game_over_surface.get_rect()
     
    
            game_over_rect.midtop = (screen_width/2, screen_height/4)
     
            screen.blit(game_over_surface, game_over_rect)
            pygame.display.flip()
            time.sleep(1)
            while(True):
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_SPACE: 
                        main()

def score(screen_width, screen_height,screen,cont):
    my_font = pygame.font.SysFont('times new roman', 30)
    score_surface = my_font.render('score: ' + str(cont) , True,pygame.Color(255, 255, 255))
    score_rect = score_surface.get_rect()
    score_rect = (screen_width/16, screen_height/16)
    screen.blit(score_surface, score_rect)
    pygame.display.update()

def kebabcount(screen_width, screen_height,screen,kebab):
    my_font = pygame.font.SysFont('times new roman',  30)
    score_surface = my_font.render('N* kebab : ' + str(kebab) , True,pygame.Color(255, 255, 255))
    score_rect = score_surface.get_rect()
    score_rect = (screen_width/1.2, screen_height/1.1)
    screen.blit(score_surface, score_rect)
    pygame.display.update()



def shoot(xpos,ypos,change_shot,screen,bullet,x_v,y_v,cont,kebab):
    x_bull=xpos
    y_bull=ypos+20
    if change_shot == 'RIGHT':
        if kebab >0:
            kebab = kebab -1
            while x_bull<1200:
                x_bull=x_bull+40
                screen.blit(bullet, (x_bull,y_bull))
                if (x_bull > x_v - 40 and x_bull < x_v + 40) and (y_bull > y_v - 40 and y_bull < y_v + 40):
                    cont = cont + 20
                    x_v = x_v + 50
                    break
                pygame.display.flip()
    if change_shot == 'UP':
        if kebab >0:
            kebab = kebab -1
            while y_bull>-800:
                y_bull=y_bull-40
                screen.blit(bullet, (x_bull,y_bull))
                if (x_bull > x_v - 40 and x_bull < x_v + 40) and (y_bull > y_v - 40 and y_bull < y_v + 40):
                    cont = cont + 20
                    y_v = y_v - 50
                    break
                pygame.display.flip()
    if change_shot == 'LEFT':
        if kebab >0:
            kebab = kebab -1
            while x_bull>-1200:
                x_bull=x_bull-40
                screen.blit(bullet, (x_bull,y_bull))
                pygame.display.flip()
                if (x_bull > x_v - 40 and x_bull < x_v + 40) and (y_bull > y_v - 40 and y_bull < y_v + 40):
                    cont = cont + 20
                    x_v = x_v - 50
                    break
    if change_shot == 'DOWN':
        if kebab >0:
            kebab = kebab -1
            while y_bull<800:
                y_bull=y_bull+40
                screen.blit(bullet, (x_bull,y_bull))
                pygame.display.flip()
                if (x_bull > x_v - 40 and x_bull < x_v + 40) and (y_bull > y_v - 40 and y_bull < y_v + 40):
                    cont = cont + 20
                    y_v = y_v + 50
                    break
    #return cont variable and x,y of vlad. +7 keep vladimir moving with main
    return (cont,x_v + 7,y_v +7,kebab)


def ragevladi(screen,x_v,y_v,vlad_b,x_pos, y_pos, screen_width, screen_height):
        x_bull=x_v
        y_bull=y_v
        choice= random.randint(1,4);
        if (random.randint(10,20) == 15):
            while x_bull<1200 and x_bull>0 and y_bull<800 and y_bull>0:
                    if(choice==1):
                        x_bull=x_bull + x_pos/20
                        y_bull = y_bull + y_pos/20
                    if(choice==2):
                        x_bull=x_bull - x_pos/20
                        y_bull = y_bull + y_pos/20
                    if(choice==3):
                        x_bull=x_bull - x_pos/20
                        y_bull = y_bull - y_pos/20
                    if(choice==4):
                        x_bull=x_bull + x_pos/20
                        y_bull = y_bull - y_pos/20
                    screen.blit(vlad_b, (x_bull,y_bull))
                    pygame.display.flip()
                    if (x_bull > x_pos - 40 and x_bull < x_pos + 40) and (y_bull > y_pos - 40 and y_bull < y_pos + 40):
                        return True
        return False                



# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(30)
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1200,800))

    bg = pygame.image.load("asset/backg.png")
    bg = pygame.transform.scale(bg, (1200,800))

    image = pygame.image.load("asset/hasb.png")
    image = pygame.transform.scale(image,(65,65))

    img_enemy = pygame.image.load("asset/OIP.png")
    img_enemy = pygame.transform.scale(img_enemy,(40,40))
    
    vladimir = pygame.image.load("asset/vladi.png")
    vladimir = pygame.transform.scale(vladimir,(80,80))

    bullet = pygame.image.load("asset/R.png")
    bullet = pygame.transform.scale(bullet,(40,40))

    vlad_b = pygame.image.load("asset/vlad_b.png")
    vlad_b = pygame.transform.scale(vlad_b,(40,40))
    pygame.display.flip()



    cont = 0
    xpos = 50
    ypos = 50
    x_enemy = random.randint(100,1100)
    y_enemy = random.randint(100,700)
    x_v = 500
    y_v = 500
    kebab = 10

    # how many pixels we move our smiley each frame
    step_x = 15
    step_y = 15
    screen_width=1200
    screen_height=800
    # check if the smiley is still on screen, if not change direction
    change_to = 'RIGHT'
    
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        if cont > 10:
            boolvar =ragevladi(screen,x_v,y_v,vlad_b,xpos,ypos,screen_width,screen_height)
            if(boolvar):
                gameover(screen_width,screen_height,screen)
        kebabcount(screen_width, screen_height,screen,kebab)
        score(screen_width,screen_height,screen,cont)

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
           gameover(screen_width,screen_height,screen)
        if ypos>screen_height-64 or ypos<0:
           gameover(screen_width,screen_height,screen)
        #time.sleep(0.05)

        #spawn sprite

        


        screen.fill(0)
        screen.blit(bg, (0, 0))
        screen.blit(image, (xpos,ypos))
        screen.blit(img_enemy, (x_enemy,y_enemy))
        screen.blit(vladimir, (x_v,y_v))
        pygame.display.flip()
        if(random.randint(100,150) == 120):
            step_x=15
            step_y=15
            image = pygame.image.load("asset/hasb.png")
            image = pygame.transform.scale(image,(65,65))
        
        time.sleep(0.03)
        #hitbox for eating
        if xpos > x_enemy-40 and xpos < x_enemy+40 and ypos > y_enemy-40 and ypos < y_enemy+40:
            pygame.display.flip()
            x_enemy = random.randint(100,1100)
            y_enemy = random.randint(100,700)
            image = pygame.image.load("asset/hasb2.png")
            image = pygame.transform.scale(image,(65,65))
            step_x = step_x + 15
            step_y = step_y + 15
            kebab=kebab+3
            cont=cont+1

        #Vladimir follow you...

        if x_v < xpos:
            x_v = x_v + 7
        else:
            x_v = x_v - 7
        if y_v < ypos:
            y_v = y_v + 7
        else:
            y_v = y_v - 7

        #if vladimir goes out the screen, he becomes stronger:
        if x_v>screen_width-64 or x_v<0:
            vladimir = pygame.transform.scale(vladimir,(160,160))
            screen.fill(0)
            screen.blit(bg, (0, 0))
            screen.blit(image, (xpos,ypos))
            x_v = 500
            y_v = 500
            screen.blit(img_enemy, (x_enemy,y_enemy))
            screen.blit(vladimir, (x_v,y_v))
        if y_v>screen_height-64 or y_v<0:
            vladimir = pygame.transform.scale(vladimir,(160,160))
            screen.fill(0)
            screen.blit(bg, (0, 0))
            screen.blit(image, (xpos,ypos))
            x_v = 500
            y_v = 500
            screen.blit(img_enemy, (x_enemy,y_enemy))
            screen.blit(vladimir, (x_v,y_v))
        

        #hitbox for Vladimir
        if xpos > x_v-40 and xpos < x_v+40 and ypos > y_v-40 and ypos < y_v+40:
            pygame.display.flip()
            cont=cont-1

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
                if event.key == pygame.K_UP:
                    change_shot = 'UP'
                    (cont,x_v,y_v,kebab) = shoot(xpos,ypos,change_shot,screen,bullet,x_v,y_v,cont,kebab)
                if event.key == pygame.K_DOWN:
                    change_shot = 'DOWN'
                    (cont,x_v,y_v,kebab) = shoot(xpos,ypos,change_shot,screen,bullet,x_v,y_v,cont,kebab)
                if event.key == pygame.K_RIGHT:
                    change_shot = 'RIGHT'
                    (cont,x_v,y_v,kebab) = shoot(xpos,ypos,change_shot,screen,bullet,x_v,y_v,cont,kebab)
                if event.key == pygame.K_LEFT:
                    change_shot = 'LEFT'
                    (cont,x_v,y_v,kebab) = shoot(xpos,ypos,change_shot,screen,bullet,x_v,y_v,cont,kebab)
                

                    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)dwa
if __name__=="__main__":
    # call the main function
    main()