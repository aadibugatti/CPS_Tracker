import pygame
pygame.init()
pygame.display.set_caption("CPS tracker")
window = pygame.display.set_mode((750, 500))
pygame.font.init()
pygame.mixer.init() 
run = True
counter=0
size=(50,50)#blit for click counter

class countdown:
    def __init__(self,timer):
        self.starttime = timer
        self.timer=timer
        self.dt=0
        self.convert2='0'
    def timeIt(self):
        self.clock = pygame.time.Clock()

        self.timer -= self.dt
        if self.timer <= 0:
                self.timer = 0.00
        self.convert2 ="{:.2f}".format(self.timer)
        self.dt = self.clock.tick(30) / 1000



def image(fileName):
    fileName = pygame.image.load(fileName)
    window.blit(fileName,(5,400))
    pygame.display.update()
    


mousedown = False
mytimer=countdown(5)
firstClick = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    
    mouse = pygame.mouse.get_pressed()
    background = pygame.Surface(size)
    if mouse[0]== True: #mouse clicked
        firstClick = True
        mousedown = True
    else:# mouse realeased
        if mousedown==True:
   #         mytimer.timeIt();
            convert=str(counter)
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render(convert, False, (255, 255, 255))
            window.blit(background,(0,0))
            window.blit(textsurface,(0,0))
            pygame.display.update()
            pygame.mixer.music.load('beep.wav')
            pygame.mixer.music.play(1)
            if mytimer.timer > 0:
                #only increment the counter if the timer valaue is greater than 0.
                counter=counter+1
            mousedown=False

    if firstClick == True:
        print('click')
        mytimer.timeIt();
    size2= (100,60)
    background2 = pygame.Surface(size2)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    timersurface = myfont.render(mytimer.convert2, False, (255, 255, 255))
    window.blit(background2,(650,0))
    window.blit(timersurface,(650,0))
    pygame.display.update()

    if mytimer.timer == 0:
        cps = str(counter/mytimer.starttime)
        intCps = counter/mytimer.starttime
        size3 = (50,50)
        background3 =pygame.Surface(size2)
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        cpssurface = myfont.render(cps, False, (255, 255, 255))
        window.blit(background3,(300,150))
        window.blit(cpssurface,(300,150))
        pygame.display.update()
        if intCps <=5:
            image('sloth.png')
            
        elif intCps >=5 and intCps <=15:
            image('rabbit.png')
        elif intCps >=15:
            image('cheetah.png')

    
pygame.quit()







