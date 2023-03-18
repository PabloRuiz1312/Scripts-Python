#PLEASE READ BEFORE PLAY OR USE THE CODE
'''

This game is designed with sprites and pygame figures, the ball its the protagonist ITS A FIGURE so 
have PREWall COLLISIONS if some object like bumpers or stick change, please, CHANGE COLLISIONS TOO

'''
#Import necesary libraries

#Pygame its very important to develop games
import pygame
#Random to object positions
import random

#---------------Surface and object create methods----------------#
#Wall creator method
def WallCreator (x,y,width,height):
 
#This method create walls like a sprite assigning it a size,position and colour
    borde = pygame.sprite.Sprite()

    borde.image = pygame.Surface([width,height])
    borde.image.fill(yellow)

    borde.rect = borde.image.get_rect()
    borde.rect.y = y
    borde.rect.x = x

    return borde

#Method to represent walls in the game window and point marker
def superficie (spritesPimball):
#This method represent walls and points marker save him in a sprites group
    Walles = pygame.sprite.Group()

#----------------Window surface wall--------------------#
    Wall_1 = WallCreator(0,0,10,1000)
    Walles.add(Wall_1)

    spritesPimball.add(Wall_1)

    Wall_2 = WallCreator(990,0,50,1000)
    Walles.add(Wall_2)

    spritesPimball.add(Wall_2)

    Wall_3 = WallCreator(0,0,990,10)
    Walles.add(Wall_3)

    spritesPimball.add(Wall_3) 
#----------------Walls to represent point marker and stats--------#
    Wall_4 = WallCreator(1000,150,350,20)
    Walles.add(Wall_4)

    spritesPimball.add(Wall_4)
    
    Wall_5 = WallCreator(1000,350,350,20)
    Walles.add(Wall_5)

    spritesPimball.add(Wall_5)

    Wall_6 = WallCreator(1000,450,350,20)
    Walles.add(Wall_6)

    spritesPimball.add(Wall_6)

    Wall_7 = WallCreator(1000,660,350,20)
    Walles.add(Wall_7)

    spritesPimball.add(Wall_7)

    
    
    return Walles

#Bumper creator method
def BumperCreator (x,y,width,height):
#This method create bumpers asigning it a size,position and color
    bumper = pygame.sprite.Sprite()

    bumper.image = pygame.Surface([width,height])
    bumper.image.fill(white)

    bumper.rect = bumper.image.get_rect()
    bumper.rect.y = y
    bumper.rect.x = x
    
    return bumper

#Método para representar los bumpers dentro de la superficie de juego - Method to represent bumpers inside game surface
def bumpers(SpriteObjetos):
#This method represet and place bumpers in determined positions, bumpers save in a diferent sprites group    
    bumpers = pygame.sprite.Group()

    bumper_1 = BumperCreator(200,250,60,60)
    bumpers.add(bumper_1)

    SpriteObjetos.add(bumper_1)

    bumper_2 = BumperCreator(700,250,60,60)
    bumpers.add(bumper_2)

    SpriteObjetos.add(bumper_2)

    bumper_3 = BumperCreator(475,600,60,60)
    bumpers.add(bumper_3)

    SpriteObjetos.add(bumper_3)

    return bumpers

#Method to fill the bumper inside
def fillBumpers (x,y,width,height):
#This methot create the padding for the bumper
    bumper = pygame.sprite.Sprite()

    bumper.image = pygame.Surface([width,height])
    bumper.image.fill(green)

    bumper.rect = bumper.image.get_rect()
    bumper.rect.y = y
    bumper.rect.x = x
    
    return bumper

#Method to represent the bumpers padding
def fillBumperss (SpriteObjetos):
#This method represent the bumpers padding asignin him a size,position and color, this padding save in the same sprites group    
    bumpers = pygame.sprite.Group()

    bumper_1 = fillBumpers(210,260,40,40)
    bumpers.add(bumper_1)

    SpriteObjetos.add(bumper_1)

    bumper_2 = fillBumpers(710,260,40,40)
    bumpers.add(bumper_2)

    SpriteObjetos.add(bumper_2)

    bumper_3 = fillBumpers(485,610,40,40)
    bumpers.add(bumper_3)

    SpriteObjetos.add(bumper_3)

    return bumpers

#Method to create the game platform 
def PlatformCreator(x,y,width,height):
#This method create the platform where sticks going
    platform = pygame.sprite.Sprite()

    platform.image = pygame.Surface([width,height])
    platform.image.fill(yellow)

    platform.rect = platform.image.get_rect()
    platform.rect.y = y
    platform.rect.x = x

    return platform

#Method to represent the left platform
def LeftPlatform(SpriteObjetos):
#This method represent the left platform usign rectangles that are getting shorter, left platform save in the bumpers sprites group
    platform = pygame.sprite.Group()

    platform_1 = PlatformCreator(10,960,320,10)
    platform.add(platform_1)

    SpriteObjetos.add(platform_1)

    platform_2 = PlatformCreator(10,970,310,10)
    platform.add(platform_2)

    SpriteObjetos.add(platform_2)

    platform_3 = PlatformCreator(10,980,300,10)
    platform.add(platform_3)

    SpriteObjetos.add(platform_3)

    platform_4 = PlatformCreator(10,990,290,10)
    platform.add(platform_4)

    SpriteObjetos.add(platform_4)

    return platform
#Método para representar la platform derecha - Method to represent the right platform
def RightPlatform(SpriteObjetos):
#This method represents the right platform that are getting shorter, right platform save in bumpers sprites group
    platform = pygame.sprite.Group()

    platform_1 = PlatformCreator(570,960,370,10)
    platform.add(platform_1)

    SpriteObjetos.add(platform_1)

    platform_2 = PlatformCreator(580,970,360,10)
    platform.add(platform_2)

    SpriteObjetos.add(platform_2)

    platform_3 = PlatformCreator(590,980,350,10)
    platform.add(platform_3)

    SpriteObjetos.add(platform_3)

    platform_4 = PlatformCreator(600,990,340,10)
    platform.add(platform_4)

    SpriteObjetos.add(platform_4)

    return platform

#Method to create the separator that separates the launcher from game space
def createSeparator(SpriteObjetos):
#This method create and represent the separator assinging him a size, position and color
#Later this separator will be one of colisions that balls will have, separator save in the bumpers sprites group
    separator = pygame.sprite.Sprite()

    separator.image = pygame.Surface([20,900])
    separator.image.fill(green)

    separator.rect = separator.image.get_rect()

    separator.rect.x=940
    separator.rect.y=110

    SpriteObjetos.add(separator)
    
    return separator

#Method to represent the left stick
def createLeftStick(x,y):
#This method create the left stick, an image its assigned like surface
#The image have to stay in the same folder that we save this program
    stick = pygame.sprite.Sprite()

    stick.image = pygame.image.load("flipperL.png")

    stick.image = pygame.transform.rotate(stick.image,345)
    stick.rect = stick.image.get_rect()

    stick.rect.x = x
    stick.rect.y = y

    return stick

#Método para crear el stick derecho - Method to create the right stick
def createRightStick(x,y):
#This method create the right stick, an image its assigned like surface
#The image have to stay in the same folder that we save this program
    stick = pygame.sprite.Sprite()

    stick.image = pygame.image.load("flipperR.png")

    stick.image = pygame.transform.rotate(stick.image,15)
    stick.rect = stick.image.get_rect()

    stick.rect.x = x
    stick.rect.y = y

    return stick

#Method to create the left stick raised
def createRaiseLeftStick(x,y):
#This method create the same left stick but in other angle, contains the same image
    stick = pygame.sprite.Sprite()

    stick.image = pygame.image.load("flipperL.png")

    stick.image = pygame.transform.rotate(stick.image,0)
    stick.rect = stick.image.get_rect()

    stick.rect.x = x
    stick.rect.y = y

    return stick

#Método para crear el stick derecho en posición levantado - Method to create the right stick raised
def createRaiseRightStick(x,y):
#This method create the same right stick but in other angle, contains the same image
    stick = pygame.sprite.Sprite()

    stick.image = pygame.image.load("flipperR.png")

    stick.image = pygame.transform.rotate(stick.image,0)
    stick.rect = stick.image.get_rect()

    stick.rect.x = x
    stick.rect.y = y

    return stick

#Method to represent the right stick
def LeftStick(SpriteObjetos):
#This method create the right stick in normal position, his size have it the image, we place his position
#The stick save in a diferent sprites group
    stick = pygame.sprite.Group()

    stick_1 = createLeftStick(310,945)
    stick.add(stick_1)

    SpriteObjetos.add(stick_1)

    return stick

#Method to represent the left stick
def RightStick(SpriteObjetos):
#This method create the left stick in normal position, his size have it the image, we place his position
#The stick save in the same sprites group that the right stick
    stick = pygame.sprite.Group()

    stick_1 = createRightStick(470,945)
    stick.add(stick_1)

    SpriteObjetos.add(stick_1)

    return stick
#Method to represent the right stick raised
def LeftRaiseStick(SpriteObjetos):
#This method represents the right stick raised, image dont change only change his angle
#This stick saves in a unique sprites group
    stick = pygame.sprite.Group()

    stick_1 = createRaiseLeftStick(310,945)
    stick.add(stick_1)

    SpriteObjetos.add(stick_1)

    return stick

#Method to represents the left stick raised
def RightRaiseStick(SpriteObjetos):
#This method represents the left stick raised, image dont change only change his angle
#This stick saves in the same sprites group that right stick raised
    stick = pygame.sprite.Group()

    stick_1 = createRaiseRightStick(470,945)
    stick.add(stick_1)

    SpriteObjetos.add(stick_1)

    return stick

#Method to create the pipes
def createPipe (x,y):
#This method create the pipes, his surface saves in a image
#The image have to stay in the same folder that the program
    Pipes = pygame.sprite.Sprite()

    Pipes.image = pygame.image.load("tuberia.png")

    Pipes.rect = Pipes.image.get_rect()

    Pipes.rect.x = x
    Pipes.rect.y = y

    return Pipes

#Método para representar las Pipess  - Method to represents the pipes
def Pipes (SpriteObjetos):
#Este método se encarga de representar las tuberías, la superficie se guarda en la imagen la posición se la damos nosotros
#This method represents the pipes, the surface save it in a image, we place the position
    Pipes = pygame.sprite.Group()
#Left pipe
    Pipes_1 = createPipe (180,500)
    Pipes.add(Pipes_1)
    SpriteObjetos.add(Pipes_1)
#Right pipe
    Pipes_2 = createPipe (710,500)
    Pipes.add(Pipes_2)
    SpriteObjetos.add(Pipes_2)

    return Pipes

#-------------------Métodos esenciales para el funcionamiento del juego--------------------------#
 
#Method to throws the ball
def throw(ball_y,launcher_y,launcher_height,timer,jump,impulso,force,ball_velocity_x):
#This method takes care of the first game phase, that its throws the ball or restart the round if we lost a life

#This conditional allows the launcher to move and launch the ball, if the inside boolean its false the launcher cand move
    if(impulso==False):
    #Gravity in the ball inside the launcher
        if(ball_y<launcher_y-10):
            ball_y+=0.4
        else:
            ball_y=launcher_y-10
    #We call keyPressed method for press or get pressed some determined keys the launcher down
        teclaPulsada = pygame.key.get_pressed()
        if ((teclaPulsada[pygame.K_DOWN] or teclaPulsada[pygame.K_s] or teclaPulsada[pygame.K_SPACE]) and jump==True):
        #When the keys are pressed the launcher down and a impulse force add
            launcher_y=launcher_y+0.2
            timer=timer+1.5
            force+=3
            if(timer==1100 or timer>1100):
                jump=False
        else:
        #When the key arent pressed the laucher comes again to his initial position, and the ball ups, if the ball dont enter in the game surface the ball launch again
            if(timer>0):
                ball_y-=(timer/280)
                timer=timer-1
                if(launcher_y>800):
                    launcher_y=launcher_y-2
                else:
                    launcher_y = 800
        if(ball_y<75):
        #When the ball enter in the game surface the launcher will be block 
            impulso=True
            timer=0
            ball_velocity_x-=(force/600)
        
    return ball_y,launcher_y,timer,jump,impulso,force,ball_velocity_x

#Method to impulse the ball
def push(ball_x,pusher_x,impulso,timer,inGame):
#This method takes care of impulse the ball to start the game phase
    if(impulso==True and inGame==False):
    #Cuando este condicional se activa se mueve el pusher a la misma altura que el separator y se desplaza la ball un poco
    #When this conditional it started the puser move to the same height that the separator and moves the ball a bit
        if(timer<100):
            pusher_x-=0.5
            timer+=1
            ball_x=ball_x-0.9
        if(timer>100 or timer==100):
            timer=0
            inGame=True
    return ball_x,pusher_x,impulso,timer,inGame

#Method to determinate the colisions with the bumpers
def BumpersCollision(ball_x,ball_y,force,force_y,ball_velocity_x,ball_velocity_y,points,PointsAcumulator,ExtraLifePointsAcumulator,LegendaryPointsAcumulator,powers):
#This method takes care of ball collisions with bumpers, when the ball reach bumper zone his velocity invert and it away a bit
#Also this method take cares to add points when the ball collide

    #Left bumper
    #Left collision
    if((ball_x>190 and ball_x<205) and (ball_y>240 and ball_y<320)):
        ball_x=184
        force+=600
        ball_velocity_x=-(force/800)
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==20 or numero==21):
            powers=True
     #Right collision
    if((ball_x>250 and ball_x<265) and (ball_y>240 and ball_y<320)):
        ball_x=275
        force+=600
        ball_velocity_x=+(force/800)
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==20 or numero==21):
            powers=True
    #Collision for above
    if((ball_y>240 and ball_y<255) and (ball_x>190 and ball_x<260)):
        ball_y=234
        force_y+=400
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==20 or numero==21):
            powers=True
    #Collision from below
    if((ball_y>280 and ball_y<315) and (ball_x>190 and ball_x<260)):
        ball_y=325
        force_y=0
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==20 or numero==21):
            powers=True
    #Left Bumper
    #Left collision
    if((ball_x>690 and ball_x<705) and (ball_y>240 and ball_y<320)):
        ball_x = 683
        force+=600
        ball_velocity_x=-(force/800)
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==30 or numero==31):
            powers=True
    #Right collision
    if((ball_x>750 and ball_x<765) and (ball_y>240 and ball_y<330)):
        ball_x = 775
        force+=600
        ball_velocity_x=+(force/800)
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==30 or numero==31):
            powers=True
    #Collision for above
    if((ball_y>240 and ball_y<265) and (ball_x>690 and ball_x<765)):
        ball_y = 244
        force_y+=400
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==30 or numero==31):
            powers=True
    #Collision from below
    if((ball_y>300 and ball_y<315) and (ball_x>690 and ball_x<765)):
        ball_y = 325
        force_y=0
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==30 or numero==31):
            powers=True
    #Bumper below
    #Left collision
    if((ball_x>465 and ball_x<480) and (ball_y>590 and ball_y<670)):
        ball_x = 459
        force+=600
        ball_velocity_x=-(force/800)
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==40 or numero==41):
            powers=True
    #Right collision
    if((ball_x>525 and ball_x<540) and (ball_y>590 and ball_y<670)):
        ball_x = 550
        force+=600
        ball_velocity_x=+(force/800)
        points+=100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==40 or numero==41):
            powers=True
    #Collision for above
    if((ball_y>590 and ball_y<610) and (ball_x>465 and ball_x<540)):
        ball_y = 580
        force_y+=600
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==40 or numero==41):
            powers=True
    #Collision from below
    if((ball_y>650 and ball_y<665) and (ball_x>465 and ball_x<540)):
        ball_y = 675
        force_y=0
        points=points+100
        PointsAcumulator+=100
        ExtraLifePointsAcumulator+=100
        LegendaryPointsAcumulator+=100
        numero = int(random.randint(1,100))
        if(numero==40 or numero==41):
            powers=True

    return ball_x,ball_y,force,force_y,ball_velocity_x,ball_velocity_y,points,PointsAcumulator,ExtraLifePointsAcumulator,LegendaryPointsAcumulator,powers

#Method to extra life bumper collision
def ExtraLifeBumperCollision(ExtraLife,ExtraLifePointsAcumulator,extraBumper_x,extraBumper_y,ball_x,ball_y,NewPosition,ExtraLifeTimer,lifes):
#This method takes care of extra life bumper collision and add lifes to the point marker
    if(ExtraLife==True):
    #This bumper isnt a sprite so it needs special variables to the conditionals run fine
    #The extra life bumper keeps while the timer exist, that also be decreased
        ExtraLifePointsAcumulator = 0
        ExtraLifeTimer-=2
        colision_x = extraBumper_x-10
        colision_x2 = extraBumper_x+10
        colisionSuma_x = extraBumper_x+50
        colisionSuma_x2 = extraBumper_x+70
        colision_y = extraBumper_y-10
        colision_y2 = extraBumper_y+10
        colisionSuma_y = extraBumper_y+50
        colisionSuma_y2 = extraBumper_y+70
        #If the ball collide, a life add to the point marker and the extra life bumper get a new position
        #Left collision
        if((ball_x>colision_x and ball_x<colision_x2) and (ball_y>colision_y and ball_y<colisionSuma_y2)):
            ExtraLife=False
            NewPosition = True
            lifes=lifes+1
        #Right collision
        if((ball_x>colisionSuma_x and ball_x<colisionSuma_x2) and (ball_y>colision_y and ball_y<colisionSuma_y2)):
            ExtraLife=False
            NewPosition = True
            lifes=lifes+1
        #Colision por arriba - Collision for above
        if((ball_y>colision_y and ball_y<colision_y2) and (ball_x>colision_x and ball_x<colisionSuma_x2)):
            ExtraLife=False
            NewPosition = True
            lifes = lifes+1
        #Collision for below
        if((ball_y>colisionSuma_y and ball_y<colisionSuma_y2) and (ball_x>colision_x and ball_x<colisionSuma_x2)):
            ExtraLife=False
            NewPosition = True
            lifes = lifes+1
        #If the timer times out the bumper desapear and get a new position
        if(ExtraLifeTimer==0 or ExtraLifeTimer<0):
            ExtraLife=False
            ExtraLifeTimer=10000
            NewPosition=True
    else:
        ExtraLifeTimer = 10000
    return ExtraLife,ExtraLifePointsAcumulator,extraBumper_x,extraBumper_y,ball_x,ball_y,NewPosition,ExtraLifeTimer,lifes  

#Method to legendary bumper collisions
def LegendaryBumperCollision(legendary,LegendaryPointsAcumulator,LegendaryBumper_x,LegendaryBumper_y,ball_x,ball_y,NewPosition,LegendaryTimer,GravityPoints):
    #This method takes care of the collision of legendary bumper, and decrease the gravity on 4 points if the ball collide
    if(legendary == True):
    #This bumper isnt a sprite so it needs special variables to the conditionals run fine
        LegendaryPointsAcumulator = 0
        LegendaryTimer-=2
        colision_x = LegendaryBumper_x-10
        colision_x2 = LegendaryBumper_x+10
        colisionSuma_x = LegendaryBumper_x+50
        colisionSuma_x2 = LegendaryBumper_x+70
        colision_y = LegendaryBumper_y-10
        colision_y2 = LegendaryBumper_y+10
        colisionSuma_y = LegendaryBumper_y+50
        colisionSuma_y2 = LegendaryBumper_y+70
        #If the ball collide with the bumper, gravity decrease on 4 points and the bumper gets a new position
        #Left collision
        if((ball_x>colision_x and ball_x<colision_x2) and (ball_y>colision_y and ball_y<colisionSuma_y2)):
            legendary=False
            NewPosition = True
            GravityPoints-=0.004
            LegendaryPointsAcumulator = 0
            if(GravityPoints<=0):
                GravityPoints = 0.002
        #Right collision
        if((ball_x>colisionSuma_x and ball_x<colisionSuma_x2) and (ball_y>colision_y and ball_y<colisionSuma_y2)):
            legendary=False
            NewPosition = True
            GravityPoints-=0.004
            LegendaryPointsAcumulator = 0
            if(GravityPoints<=0):
                GravityPoints = 0.002
        #Collision for above
        if((ball_y>colision_y and ball_y<colision_y2) and (ball_x>colision_x and ball_x<colisionSuma_x2)):
            legendary=False
            NewPosition = True
            GravityPoints-=0.004
            LegendaryPointsAcumulator = 0
            if(GravityPoints<=0):
                GravityPoints = 0.002
        #Collision from below
        if((ball_y>colisionSuma_y and ball_y<colisionSuma_y2) and (ball_x>colision_x and ball_x<colisionSuma_x2)):
            legendary=False
            NewPosition = True
            GravityPoints-=0.004
            LegendaryPointsAcumulator = 0
            if(GravityPoints<=0):
                GravityPoints = 0.002
        #If the timer times out, the bumper disaperar and get a new position
        if(LegendaryTimer==0 or LegendaryTimer<0):
            legendary=False
            LegendaryTimer=15000
            NewPosition=True
    else:
        LegendaryTimer = 15000
    
    return legendary,LegendaryPointsAcumulator,LegendaryBumper_x,LegendaryBumper_y,ball_x,ball_y,NewPosition,LegendaryTimer,GravityPoints
#Method to pipes collisions
def pipesCollision(ball_x,ball_y,ball_velocity_x,ball_velocity_y,force):
#This method takes care of pipes collide
    #-----------------Lateral including inside ---------------#
    #Left pipe
    if((ball_x>195 and ball_x<200) and (ball_y>490 and ball_y<763)):
        ball_velocity_x = ball_velocity_x * (-1)
    if((ball_x>260 and ball_x<265) and (ball_y>490 and ball_y<763)):
        ball_velocity_x = ball_velocity_x * (-1)
    #Right pipe
    if((ball_x>725 and ball_x<730) and (ball_y>490 and ball_y<763)):
        ball_velocity_x = -ball_velocity_x
    if((ball_x>790 and ball_x<795) and (ball_y>490 and ball_y<763)):
        ball_velocity_x = -ball_velocity_x
    
    #ANNOTATION: If the ball enter in the pipe, the same collisions are applied as outside but the reverse, you can see it if you draw his sprite on top that the ball sprite 
    return ball_x,ball_y,ball_velocity_x,ball_velocity_y,force
#Method to choose and use a superpower
def superPower (powers,reverseGravity,activateBumpers,rescue,activate,GravityPoints,GravityTimer,ExtraLife,legendary,inGame):
#This method takes care to assign and activate a power
    if(inGame==True):
        if(powers==True):
            numero = int(random.randint(1,3))
            if(numero==1 and BumperActivation==False and rescue==False):
                reverseGravity = True
            elif(numero==2 and reverseGravity==False and rescue==False):
                activateBumpers = True
            elif(numero==3 and reverseGravity==False and BumperActivation==False):
                rescue = True
            powers=False
        teclaPulsada = pygame.key.get_pressed()
        #If this power appears, can be invert the gravity in 20 seconds or when his valor reach 0
        if(reverseGravity==True and powers==False):
            if(teclaPulsada[pygame.K_f] and GravityTimer==20000):
                GravityPoints = GravityPoints * (-1)
                activate=True
            if(activate==True):
                GravityTimer-=2
                if(GravityPoints>0):
                    GravityPoints = 0.001
                    GravityPoints = GravityPoints * (-1)
                    activate=False
                    GravityTimer=0
            if(GravityTimer==0 or GravityTimer<0):
                GravityPoints = GravityPoints * (-1)
                reverseGravity = False
                activate=False
                GravityTimer = 20000
        #If this power appears, can be activate the 2 specials bumpers in the same time
        if(activateBumpers == True and powers==False):
            if(teclaPulsada[pygame.K_f]):
                ExtraLife = True
                legendary = True
                activateBumpers = False
        #If this power appears, will be activate a brigde in the sticks hole that protect the balls falling
        if(rescue==True and powers==False):
            if(teclaPulsada[pygame.K_f]):
                activate = True
            if(activate==True):
                GravityTimer-=2
            if(GravityTimer==0 or GravityTimer<0):
                rescue = False
                activate = False
                GravityTimer = 20000
    return powers,reverseGravity,activateBumpers,rescue,activate,GravityPoints,GravityTimer,ExtraLife,legendary,inGame
#Method to draw the bridge when rescue actives
def WallRescue(spritesPinball):

#This method draw the bridge that protect the balls from losing the round
    rescue = pygame.sprite.Group()

    rescue_1 = WallCreator(320,930,260,100)
    rescue.add(rescue_1)

    spritesPinball.add(rescue_1)

    return rescue

#Method to rescue collisions
def PlaceRescue(ball_x,ball_y,ball_x1,ball_y1,ball_x2,ball_y2,force_y,force_y1,force_y2):
#Este método sirve para que las balls colisionen con el puente del poder rescue 
#This method takes care of the balls collide with the brigde of rescue power
    if(ball_y>930 and (ball_x>315 and ball_x<585)):
        force_y+=800
    if(ball_y1>930 and (ball_x1>315 and ball_x1<585)):
        force_y1+=800
    if(ball_y2>930 and (ball_x2>315 and ball_x2<585)):
        force_y2+=800
    return ball_x,ball_y,ball_x1,ball_y1,ball_x2,ball_y2,force_y,force_y1,force_y2  
#Game phase method
def StartGame(ball_x,ball_y,GravityPoints,ball_velocity_x,ball_velocity_y,force,pusher_x,inGame,impulso,jump,points,recordpoints,PointsAcumulator,ExtraLifePointsAcumulator,extras1,extras2,Raise,ExtraLife,lifes,extraBumper_x,extraBumper_y,ExtraLifeTimer,NewPosition,NewPositionLegendaria,force_y,legendary,LegendaryPointsAcumulator,LegendaryBumper_x,LegendaryBumper_y,LegendaryTimer,powers):
#This method takes care of game operation, takes care of balls movement, balls collide (calling the other methods), points condition, sticks position and end of the round
    if(inGame==True):
        NewPosition = False
        NewPositionLegendaria = False
        #Gravity application in the ball in the game phase and horizontal force
        if(force>1000):
            force=force-2
        else:
            force=799
        if(force_y>1):
            ball_velocity_y = (force_y/280) *(-1)
            force_y=force_y - 1                           
        else:
            puntoGravedadMax = False
            force_y=0
            ball_velocity_y+=GravityPoints         
        #------------------Raise Sticks and Sticks collision-----------#
        #Call keyPressed method again
        teclaPulsada = pygame.key.get_pressed()
        if((teclaPulsada[pygame.K_DOWN]) or teclaPulsada[pygame.K_SPACE]):
            Raise = True
        else:
            Raise = False
        #Sticks collision without raise
        if(Raise==False):
            if((ball_y>950 and ball_y<970) and (ball_x>305 and ball_x<435)):
                ball_y = 940
                force+=900
                force_y+=700
                ball_velocity_y = 0
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x=+(force/800)
                if(numero==2):
                    ball_velocity_x=-(force/800)
            if((ball_y>950 and ball_y<970) and (ball_x>470 and ball_x<600)):
                ball_y = 940
                force+=900
                force_y+=700
                ball_velocity_y = 0
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x=+(force/800)
                if(numero==2):
                    ball_velocity_x=-(force/800)
        #Stick raise collision
        if(Raise==True):
            if((ball_y>930 and ball_y<960) and (ball_x>305 and ball_x<435)):
                ball_y = 930
                force+=1500
                force_y+=1500
                ball_velocity_y = 0
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x=+(force/800)
                if(numero==2):
                    ball_velocity_x=-(force/800)
            if((ball_y>935 and ball_y<960) and (ball_x>485 and ball_x<600)):
                ball_y = 930
                force+=1500
                force_y+=1200
                ball_velocity_y = 0
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x=+(force/800)
                if(numero==2):
                    ball_velocity_x=-(force/800)
        #-----------------Walls collision-----------------------------#
        #Left wall
        if(ball_x<20):
            ball_velocity_x=+(force/800)
        #Separator
        if(ball_x>930):
            ball_velocity_x=-(force/800)
        #----------------Bumpers collision -----------------------------#
        #The indicated bumpers collision method is called
        ball_x,ball_y,force,force_y,ball_velocity_x,ball_velocity_y,points,PointsAcumulator,ExtraLifePointsAcumulator,LegendaryPointsAcumulator,powers = BumpersCollision(ball_x,ball_y,force,force_y,ball_velocity_x,ball_velocity_y,points,PointsAcumulator,ExtraLifePointsAcumulator,LegendaryPointsAcumulator,powers) 
        #----------------Pipes collisions -----------------------------#
        #The indicated method of pipes collision is called
        ball_x,ball_y,ball_velocity_x,ball_velocity_y,force = pipesCollision(ball_x,ball_y,ball_velocity_x,ball_velocity_y,force)
        #-------------------Collisions for above and collisions in platforms---------------------------#
        #Collisions for above the window
        if(ball_y<20):
            ball_y=30
            force_y=0
            ball_velocity_y = ball_velocity_y * (-1)
        #Left platform collision
        if((ball_y>960 and ball_y<990) and (ball_x>10 and ball_x<309)):
            ball_y = 955
            force_y+=600
            ball_velocity_y = 0
        #Right platform collision
        if((ball_y>960 and ball_y<990) and (ball_x>596 and ball_x<930)):
            ball_y = 955
            force_y+=600
            ball_velocity_y = 0
            
        
        #----------------Point condition---------------------------------------#
        #Extra life bumper condition
        if(ExtraLifePointsAcumulator>=1000 and ExtraLife==False):
            ExtraLife=True
            ExtraLifePointsAcumulator = 0
        #Legendary bumper condition
        if(LegendaryPointsAcumulator>=5000 and legendary==False):
            legendary=True
            LegendaryPointsAcumulator = 0
        #Gravity increment condition
        if(PointsAcumulator>=750):
            PointsAcumulator=0
            if(GravityPoints<0.01):
                GravityPoints+=0.001
        #Extra balls condition
        elif(PointsAcumulator>=500 and (extras1==False and extras2==False)) :     
            extras1=True
            extras2=True
                 
        #-------------------Extra life bumper collision -----------------------------#
        #The indicated method of extra life bumper collision is called

        ExtraLife,ExtraLifePointsAcumulator,extraBumper_x,extraBumper_y,ball_x,ball_y,NewPosition,ExtraLifeTimer,lifes = ExtraLifeBumperCollision(ExtraLife,ExtraLifePointsAcumulator,extraBumper_x,extraBumper_y,ball_x,ball_y,NewPosition,ExtraLifeTimer,lifes)
        
        #-------------------Legendary bumper collision---------------------#
        #The indicated method of legendary bumper collisions is called

        legendary,LegendaryPointsAcumulator,LegendaryBumper_x,LegendaryBumper_y,ball_x,ball_y,NewPositionLegendaria,LegendaryTimer,GravityPoints = LegendaryBumperCollision(legendary,LegendaryPointsAcumulator,LegendaryBumper_x,LegendaryBumper_y,ball_x,ball_y,NewPositionLegendaria,LegendaryTimer,GravityPoints)
        
        #-------------------Fin de la ronda - End of the round------------------------------------#
        #When the ball beat the bottom of the window a life is taken, the variables that allows game operation resets and the ball place in launcher position
        if(ball_y>1000):
            lifes=lifes-1
            ExtraLifeTimer=10000
            LegendaryTimer=15000
            ball_y=750
            ball_x=975
            force=0
            force_y=0
            pusher_x=990
            inGame=False
            impulso=False
            jump=True
            extras1=False
            extras2=False
            ExtraLife=False
            legendary = False
            Raise=False
            NewPosition = True
            NewPositionLegendaria = True
            powers = False
            GravityPoints=0.001
            ball_velocity_y = 0
            #Also maximun points are scored
            if(points>recordpoints):
                recordpoints = points
            PointsAcumulator=0
            ExtraLifePointsAcumulator=0
            LegendaryPointsAcumulator = 0
            points=0
        #Ball movement
        ball_x+=ball_velocity_x
        ball_y+=ball_velocity_y
               
    return ball_x,ball_y,GravityPoints,ball_velocity_x,ball_velocity_y,force,pusher_x,inGame,impulso,jump,points,recordpoints,PointsAcumulator,ExtraLifePointsAcumulator,extras1,extras2,Raise,ExtraLife,lifes,extraBumper_x,extraBumper_y,ExtraLifeTimer,NewPosition,NewPositionLegendaria,force_y,legendary,LegendaryPointsAcumulator,LegendaryBumper_x,LegendaryBumper_y,LegendaryTimer,powers

#First extra ball method
def FirstExtraBall(extras1,ball_x1,ball_y1,ball_velocity_x1,ball_velocity_y1,force1,force_y1,GravityPoints,points,PointsAcumulator,ExtraLifePointsAcumulator,Raise,LegendaryPointsAcumulator,powers):
#This method takes care of movement and collisions (callings the methotds) of first extra ball
    if(extras1==True):
        #Gravity application and horizontal force
        if(force1>800):
            force1=force1-2
        else:
            force1=799
        if(force_y1>1):
            ball_velocity_y1 = (force_y1/300) *(-1)
            force_y1 =force_y1 - 1
        else:
            force_y1=0
            ball_velocity_y1 += GravityPoints 
        #---------------------Sticks collisions----------------------------------#
        #Stick without raise collision
        if(Raise==False):
            if((ball_y1>950 and ball_y1<960) and (ball_x1>310 and ball_x1<435)):
                ball_y1 = 940
                force1+=900
                force_y1+=700
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x1=+(force1/800)
                if(numero==2):
                    ball_velocity_x1=-(force1/800)
            if((ball_y1>950 and ball_y1<960) and (ball_x1>470 and ball_x1<595)):
                ball_y1 = 940
                force1+=900
                force_y1+=700
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x1=+(force/800)
                if(numero==2):
                    ball_velocity_x1=-(force/800)
        #Stick raise collision
        if(Raise==True):
            if((ball_y1>935 and ball_y1<940) and (ball_x1>310 and ball_x1<425)):
                ball_y1 = 930
                force1+=1500
                force_y1+=1500
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x1=+(force/800)
                if(numero==2):
                    ball_velocity_x1=-(force/800)
            if((ball_y1>935 and ball_y1<940) and (ball_x1>485 and ball_x1<595)):
                ball_y1 = 930
                force1+=1500
                force_y1+=1200
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x1=+(force/800)
                if(numero==2):
                    ball_velocity_x1=-(force/800)
        #-----------------Walls collision----------------------------#
        #Left wall collision
        if(ball_x1<20):
            ball_velocity_x1=+(force1/800)
        #Right wall collision
        if(ball_x1>930):
            ball_velocity_x1=-(force1/800)
        #------------------Bumpers collision----------------------------#
        #The indicated collision method is called
        ball_x1,ball_y1,force1,force_y1,ball_velocity_x1,ball_velocity_y1,points,PointsAcumulator,ExtraLifePointsAcumulator,LegendaryPointsAcumulator,powers = BumpersCollision(ball_x1,ball_y1,force1,force_y1,ball_velocity_x1,ball_velocity_y1,points,PointsAcumulator,ExtraLifePointsAcumulator,LegendaryPointsAcumulator,powers)
        #------------------Pipes collisions---------------------------#
        #The indicated pipes collisions metod is called
        ball_x1,ball_y1,ball_velocity_x1,ball_velocity_y1,force1=pipesCollision(ball_x1,ball_y1,ball_velocity_x1,ball_velocity_y1,force1)
        #-------------------Collision for above and platform-----------------------------#
        #Collision with the top of the window
        if(ball_y1<20):
            ball_y1=30
            force_y1=0
            ball_velocity_y1 = ball_velocity_y1 * (-1)
        #Left platform collision
        if((ball_y1>960 and ball_y1<990) and (ball_x1>10 and ball_x1<309)):
            ball_y1 = 955
            force_y1+=600
        #Right platform collision
        if((ball_y1>960 and ball_y1<990) and (ball_x1>596 and ball_x1<930)):
            ball_y1 = 955
            force_y1+=600
        #--------------------End of extra ball----------------------------#
        #When the ball beat the botton of the window, it stop representing and the position is changed randomly  
        if(ball_y1>1000):
            extras1=False
            ball_velocity_y1 = 0
            force1=600
            force_y1 = 0
            ball_x1=random.randint(20,900)
            ball_y1=random.randint(80,950)
        #Ball movement
        ball_x1+=ball_velocity_x1
        ball_y1+=ball_velocity_y1
        return extras1,ball_x1,ball_y1,ball_velocity_x1,ball_velocity_y1,force1,force_y1,GravityPoints,points,PointsAcumulator,ExtraLifePointsAcumulator,Raise,LegendaryPointsAcumulator,powers

#Second extra ball method
def SecondExtraBall(extras2,ball_x2,ball_y2,ball_velocity_x2,ball_velocity_y2,force2,force_y2,GravityPoints,points,PointsAcumulator,ExtraLifePointsAcumulator,Raise,LegendaryPointsAcumulator,powers):
#This method takes care of movement and collision (calling the methods) pf seconds extra ball

    if(extras2==True):
        #Gravity application and horizontal force
        if(force2>800):
            force2=force2-2
        else:
            force2=799
        if(force_y2>1):
            ball_velocity_y2 = (force_y2/300) *(-1)
            force_y2=force_y2 - 1
        else:
            force_y2=0
            ball_velocity_y2+=GravityPoints
        #---------------------Sticks collisions----------------------#
        #Sticks without raise
        if(Raise==False):
            if((ball_y2>950 and ball_y2<960) and (ball_x2>310 and ball_x2<435)):
                ball_y2 = 940
                force2+=900
                force_y2+=700
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x2=+(force2/800)
                if(numero==2):
                    ball_velocity_x2=-(force2/800)
            if((ball_y2>950 and ball_y2<960) and (ball_x2>470 and ball_x2<595)):
                ball_y2 = 940
                force2+=900
                force_y2+=700
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x2=+(force2/800)
                if(numero==2):
                    ball_velocity_x2=-(force2/800)
        #Stick raise
        if(Raise==True):
            if((ball_y2>935 and ball_y2<940) and (ball_x2>310 and ball_x2<425)):
                ball_y2 = 930
                force2+=1500
                force_y2+=1500
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x2=+(force2/800)
                if(numero==2):
                    ball_velocity_x2=-(force2/800)
            if((ball_y2>935 and ball_y2<940) and (ball_x2>485 and ball_x2<595)):
                ball_y2 = 930
                force2+=1500
                force_y2+=1200
                numero = random.randint(1,2)
                if(numero==1):
                    ball_velocity_x2=+(force2/800)
                if(numero==2):
                    ball_velocity_x2=-(force2/800)

         #------------------Bumpers collision----------------------------#
        #The indicated bumper collision method is called
        ball_x2,ball_y2,force2,force_y2,ball_velocity_x2,ball_velocity_y2,points,PointsAcumulator,ExtraLifePointsAcumulator,LegendaryPointsAcumulator,powers = BumpersCollision(ball_x2,ball_y2,force2,force_y2,ball_velocity_x2,ball_velocity_y2,points,PointsAcumulator,ExtraLifePointsAcumulator,LegendaryPointsAcumulator,powers)

        #-----------------Pipes collision---------------------------#
        #The indicated pipes collision method is called 
        ball_x2,ball_y2,ball_velocity_x2,ball_velocity_y2,force2=pipesCollision(ball_x2,ball_y2,ball_velocity_x2,ball_velocity_y2,force2)

        #-----------------Walls collisions----------------------------#
        #Left wall collision
        if(ball_x2<20):
            ball_velocity_x2=+(force2/800)
        #Separator collision
        if(ball_x2>930):
            ball_velocity_x2=-(force2/800)
        #--------------------Top and platform collision ----------------------------#
        #Colisión con el tope de lla ventana - Collision with the top of the window
        if(ball_y2<20):
            force_y2=0
            ball_y2=30
            ball_velocity_y2 = ball_velocity_y2 * (-1)
        #Left platform collision
        if((ball_y2>960 and ball_y2<990) and (ball_x2>10 and ball_x2<309)):
            ball_y2 = 955
            force_y2+=600
        #Right platform collision
        if((ball_y2>960 and ball_y2<990) and (ball_x2>596 and ball_x2<930)):
            ball_y2 = 955
            force_y2+=600
        #-------------------------------------End of second extra ball---------------------#
        #When the ball beat the bottom of the window the second extra ball disappear and the second extra ball position is changed
        if(ball_y2>1000):
            extras2=False
            ball_velocity_y2 = 0
            force2=600
            force_y2 = 0
            ball_x2=random.randint(20,800)
            ball_y2=random.randint(80,800)
        #Ball movement
        ball_x2+=ball_velocity_x2
        ball_y2+=ball_velocity_y2
        return extras2,ball_x2,ball_y2,ball_velocity_x2,ball_velocity_y2,force2,force_y2,GravityPoints,points,PointsAcumulator,ExtraLifePointsAcumulator,Raise,LegendaryPointsAcumulator,powers 
#------------------VARIABLES-------------------# 

#------------------SURFACE AND OBJECT CREATION VARIABLES------------------------#  
#CWe create the size of the window
width = 1350
height = 1000
#We create the colors that we use in the game
white = pygame.Color (255,255,255)
black = pygame.Color (0,0,0)
red = pygame.Color (255,0,0)
green = pygame.Color (0,255,0)
blue = pygame.Color (0,0,255)
orange = pygame.Color (255,128,0)
yellow = pygame.Color (255,255,0)
#We inicializate the pygame around
pygame.init()
#We create the window and we write a name
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pimball')
#We create the sprites groups
WallsSprites = pygame.sprite.Group()
SpriteObjetos = pygame.sprite.Group()
SpriteObjetosStick = pygame.sprite.Group()
RaiseStickSpriteObject = pygame.sprite.Group()
PowerRescueSpriteObject = pygame.sprite.Group()
#We create the game ball (protagonist)
ball_radio = 10
ball_x=975
ball_y=550
ball_velocity_x = 0
ball_velocity_y = 0
#We create the extra balls (will appear for points condition)
#ball extra 1 - First extra ball
ball_radio1 = 10
ball_x1=random.randint(20,910)
ball_y1=random.randint(80,980)
ball_velocity_x1 = 0.3
ball_velocity_y1 = 0
#Second extra ball
ball_radio2 = 10
ball_x2=random.randint(20,900)
ball_y2=random.randint(80,950)
ball_velocity_x2 = 0.5
ball_velocity_y2 = 0
#We create the launcher
launcher_x = 965
launcher_y = 800
launcher_width = 20
launcher_height = 200
#We create the pusher
pusher_x=990
pusher_y=10
pusher_width=50
pusher_height=100
#We create the extra life bumper
extraBumper_x = int(random.randint(280,620))
extraBumper_y = int(random.randint(250,500))
extraBumper_width = 60
extraBumper_height = 60
#We create the legendary bumper
LegendaryBumper_x = int(random.randint(280,620))
LegendaryBumper_y = int(random.randint(30,280))
LegendaryBumper_width = 60
LegendaryBumper_height = 60
#------------------OPERATING GAME VARIABLES------------------#
#Gravity points (the same for all balls)
GravityPoints = 0.001
#Movement force of main ball
force = 0
force_y = 0
#Movement force of extra balls
#First extra ball force
force1 = 1
force1_y = 0
#Second extra ball force
force2 = 1
force2_y = 0
#Phase variables
jump = True
impulso = False
inGame = False
#Timers 
timer = 0
ExtraLifeTimer = 10000
LegendaryTimer = 15000
#Points and acumulators
#Points
points = 0
recordpoints = 0
#Acumulator points
PointsAcumulator = 0
ExtraLifePointsAcumulator = 0
LegendaryPointsAcumulator = 0
MissingPoints = 0
LegendaryMissingPoints = 0
#Superpower variables
activate = False
reverseGravity = False
GravityTimer = 20000
BumperActivation = False
rescue = False
#Elements activation variables
extras1 = False
extras2 = False
Raise = False
ExtraLife = False
legendary = False
powers = False
#Otras variables - Other variables
lifes = 3
NewPosition = False
NewPositionExtraLife = False
NewPositionLegendaria = False
#----------------CALLING THE METHODS TO SAVE SPRITES-------------------------#
#We save the walls in his group
Walls = superficie(WallsSprites)
#We save the objects in his group
separator = createSeparator(SpriteObjetos)
bumper = bumpers(SpriteObjetos)
relleno = fillBumperss(SpriteObjetos)
platformIzq = LeftPlatform(SpriteObjetos)
platformDer = RightPlatform(SpriteObjetos)
Pipes = Pipes(SpriteObjetos)
#We save the sticks without raise 
StickDer = LeftStick(SpriteObjetosStick)
StickIzq = RightStick(SpriteObjetosStick)
#Guardamos los sticks levantados - We save the raise sticks
StickDerLevantado = LeftRaiseStick(RaiseStickSpriteObject)
StickIzqLevantado = RightRaiseStick(RaiseStickSpriteObject)
#We save rescue superpower wall
salvar = WallRescue(PowerRescueSpriteObject)
#---------------------------SENTENCES GENERATOR----------------------------#
frasepoints = pygame.font.Font(None,35) 
fraselifes = pygame.font.Font(None,35)
fraseExtraLife = pygame.font.Font(None,35)
fraseGravedad = pygame.font.Font(None,35)
fraseLegendaria = pygame.font.Font(None,35)
PowerSentence = pygame.font.Font(None,35)

#We create the loop that allows run the game one times that execute
running = True
while (running and lifes>0):
    #We establish that finish the game when we press the X in the window
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
    
    #----------------------PHASE METHODS---------------#
    ball_y,launcher_y,timer,jump,impulso,force ,ball_velocity_x= throw(ball_y,launcher_y,launcher_height,timer,jump,impulso,force,ball_velocity_x)
    ball_x,pusher_x,impulso,timer,inGame = push(ball_x,pusher_x,impulso,timer,inGame)
    ball_x,ball_y,GravityPoints,ball_velocity_x,ball_velocity_y,force,pusher_x,inGame,impulso,jump,points,recordpoints,PointsAcumulator,ExtraLifePointsAcumulator,extras1,extras2,Raise,ExtraLife,lifes,extraBumper_x,extraBumper_y,ExtraLifeTimer,NewPositionExtraLife,NewPositionLegendaria,force_y,legendary,LegendaryPointsAcumulator,LegendaryBumper_x,LegendaryBumper_y,LegendaryTimer,powers = StartGame(ball_x,ball_y,GravityPoints,ball_velocity_x,ball_velocity_y,force,pusher_x,inGame,impulso,jump,points,recordpoints,PointsAcumulator,ExtraLifePointsAcumulator,extras1,extras2,Raise,ExtraLife,lifes,extraBumper_x,extraBumper_y,ExtraLifeTimer,NewPositionExtraLife,NewPositionLegendaria,force_y,legendary,LegendaryPointsAcumulator,LegendaryBumper_x,LegendaryBumper_y,LegendaryTimer,powers)
    powers,reverseGravity,BumperActivation,rescue,activate,GravityPoints,GravityTimer,ExtraLife,legendary,inGame = superPower (powers,reverseGravity,BumperActivation,rescue,activate,GravityPoints,GravityTimer,ExtraLife,legendary,inGame)
    #We draw the window deep and walls
    screen.fill(black)
    WallsSprites.draw(screen)
    #Change of position of extra life bumper and legendary bumper
    if(NewPositionExtraLife==True):
        extraBumper_x = random.randint(280,620)
        extraBumper_y = random.randint(250,500)
    if(NewPositionLegendaria==True):
        LegendaryBumper_x = random.randint(70,810)
        LegendaryBumper_y = random.randint(30,280)
    #Change of position of sticks
    if(Raise==False):
        SpriteObjetosStick.draw(screen)
    else:
        RaiseStickSpriteObject.draw(screen)
    #We draw the launcher, pusher and ball
    pygame.draw.rect(screen,red,(launcher_x,launcher_y,launcher_width,launcher_height))
    pygame.draw.rect(screen,yellow,(pusher_x,pusher_y,pusher_width,pusher_height))
    pygame.draw.circle(screen,blue,(ball_x,ball_y),ball_radio)
    #We draw the extra balls when his condition is met
    if(extras1==True):
        pygame.draw.circle(screen,green,(ball_x1,ball_y1),ball_radio1)
        extras1,ball_x1,ball_y1,ball_velocity_x1,ball_velocity_y1,force1,force1_y,GravityPoints,points,PointsAcumulator,ExtraLifePointsAcumulator,Raise,LegendaryPointsAcumulator,powers = FirstExtraBall(extras1,ball_x1,ball_y1,ball_velocity_x1,ball_velocity_y1,force1,force1_y,GravityPoints,points,PointsAcumulator,ExtraLifePointsAcumulator,Raise,LegendaryPointsAcumulator,powers)
    if(extras2==True):
        pygame.draw.circle(screen,red,(ball_x2,ball_y2),ball_radio2)
        extras2,ball_x2,ball_y2,ball_velocity_x2,ball_velocity_y2,force2,force2_y,GravityPoints,points,PointsAcumulator,ExtraLifePointsAcumulator,Raise,LegendaryPointsAcumulator,powers = SecondExtraBall(extras2,ball_x2,ball_y2,ball_velocity_x2,ball_velocity_y2,force2,force2_y,GravityPoints,points,PointsAcumulator,ExtraLifePointsAcumulator,Raise,LegendaryPointsAcumulator,powers)
    #We draw the game object
    SpriteObjetos.draw(screen)
    if(rescue==True and activate==True):
        PowerRescueSpriteObject.draw(screen)
        ball_x,ball_y,ball_x1,ball_y1,ball_x2,ball_y2,force_y,force1_y,force2_y = PlaceRescue(ball_x,ball_y,ball_x1,ball_y1,ball_x2,ball_y2,force_y,force1_y,force2_y)
    #--------MESSAGES---------#
    #Points
    timerpoints = "PUNTOS: "+str(points)
    mensajepoints = frasepoints.render(timerpoints,1,white)
    screen.blit(mensajepoints,(1110,20))
    #Points record
    record = "TU RECORD: "+str(recordpoints)
    mensajeRecordpoints = frasepoints.render(record,1,white)
    screen.blit(mensajeRecordpoints,(1110,80))
    #Lifes
    timerlifes = "TUS VIDAS: "+str(lifes)
    mensajelifes = fraselifes.render(timerlifes,1,white)
    screen.blit(mensajelifes,(1110,190))
    #Points to extra life
    MissingPoints = 1000 - ExtraLifePointsAcumulator
    if(ExtraLife == False):
        marcadorExtraLife = "FALTAN "+str(MissingPoints)
        mensajeExtraLife = fraseExtraLife.render(marcadorExtraLife,1,white)
        screen.blit(mensajeExtraLife,(1110,260))
    #Existent extra life indicator and draw of extra life bumper
    else:
        pygame.draw.rect(screen,green,(extraBumper_x,extraBumper_y,extraBumper_width,extraBumper_height))
        indicarExtraLifeExistente = "VIDA EXTRA ACTIVA"
        mensajeExtraLife_Extra = fraseExtraLife.render(indicarExtraLifeExistente,1,white)
        screen.blit(mensajeExtraLife_Extra,(1050,260))
        indicarTiempo = str(int(ExtraLifeTimer/1000))+" SEGUNDOS"
        mensajeTiempo = fraseExtraLife.render(indicarTiempo,1,white)
        screen.blit(mensajeTiempo,(1110,300))
    #We indicate the gravity level in game
    nivelGravedad = "NIVEL GRAVEDAD "+str(int(GravityPoints*1000))
    mensajeGravedad = fraseGravedad.render(nivelGravedad,1,white)
    screen.blit(mensajeGravedad,(1080,400))
    #Points to the legendary bumper
    LegendaryMissingPoints = 5000 - LegendaryPointsAcumulator
    if(legendary == False):
        marcadorlegendary = "FALTAN "+str(LegendaryMissingPoints)
        mensajelegendary = fraseLegendaria.render(marcadorlegendary,1,white)
        screen.blit(mensajelegendary,(1110,500))
    #Existent legendary bumper indicator and draw of legendary bumper
    else:
        pygame.draw.rect(screen,orange,(LegendaryBumper_x,LegendaryBumper_y,LegendaryBumper_width,LegendaryBumper_height))
        indicarlegendaryExistente = "BUMPER LEGENDARIO"
        indicarlegendaryExistenteActivo = "ACTIVO"
        mensajelegendaryExistente = fraseLegendaria.render(indicarlegendaryExistente,1,white)
        mensajelegendaryExistenteActivo = fraseLegendaria.render(indicarlegendaryExistenteActivo,1,white)
        screen.blit(mensajelegendaryExistente,(1050,500))
        screen.blit(mensajelegendaryExistenteActivo,(1130,550))
        indicarTiempolegendary = str(int(LegendaryTimer/1000))+" SEGUNDOS"
        mensajeTiempolegendary = fraseLegendaria.render(indicarTiempolegendary,1,white)
        screen.blit(mensajeTiempolegendary,(1100,600))
    #Power indicator
    #No powers
    if(reverseGravity==False and BumperActivation==False and rescue==False):
        noPowers = "SIN PODERES"
        NoPowersMessage = PowerSentence.render(noPowers,1,white)
        screen.blit(NoPowersMessage,(1110,700))
    #Reverse gravity
    elif(reverseGravity==True and BumperActivation==False and rescue==False):
        if(activate==False):
            poderGravedad = "INVERTIR GRAVEDAD"
            mensajePoderGravedad = PowerSentence.render(poderGravedad,1,white)
            screen.blit(mensajePoderGravedad,(1070,700))
            activateIndicator = "PULSA F PARA ACTIVAR"
            activateMessage = PowerSentence.render(activateIndicator,1,white)
            screen.blit(activateMessage,(1050,750))
        #Seconds remaining
        else:
            poderGravedad = "INVERTIR GRAVEDAD"
            mensajePoderGravedad = PowerSentence.render(poderGravedad,1,white)
            screen.blit(mensajePoderGravedad,(1070,700))
            segundosGravedad = str(int(GravityTimer/1000))+" SEGUNDOS"
            mensajeSegundosGravedad = PowerSentence.render(segundosGravedad,1,white)
            screen.blit(mensajeSegundosGravedad,(1110,750))
    #Bumpers activation
    elif(BumperActivation==True and reverseGravity==False and rescue==False):
        poderBumper = "ACTIVAR BUMPERS"
        mensajePoderBumper = PowerSentence.render(poderBumper,1,white)
        screen.blit(mensajePoderBumper,(1080,700))
        activateIndicator = "PULSA F PARA ACTIVAR"
        activateMessage = PowerSentence.render(activateIndicator,1,white)
        screen.blit(activateMessage,(1050,750))
    #Rescue
    elif(rescue==True and BumperActivation==False and reverseGravity==False):
        if(activate==False):
            rescuePower = "SALVAMENTO"
            RescuePowerMessage = PowerSentence.render(rescuePower,1,white)
            screen.blit(RescuePowerMessage,(1070,700))
            activateIndicator = "PULSA F PARA ACTIVAR"
            activateMessage = PowerSentence.render(activateIndicator,1,white)
            screen.blit(activateMessage,(1050,750))
        #Seconds remaining
        else:
            rescuePower = "SALVAMENTO"
            RescuePowerMessage = PowerSentence.render(rescuePower,1,white)
            screen.blit(RescuePowerMessage,(1110,700))
            SecondsRescue = str(int(GravityTimer/1000))+" SEGUNDOS"
            SecondsRemainingRescuePower = PowerSentence.render(SecondsRescue,1,white)
            screen.blit(SecondsRemainingRescuePower,(1110,750))
    

    #We udapte constantly the screen
    
    pygame.display.flip()

#When the loop end, the window and the game are closed
pygame.quit() 