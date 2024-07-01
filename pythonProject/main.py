import random
import pygame
import sys

class Bird(object):
    '定义一个鸟类'
    def __init__(self):
        '定义初始方法'
        self.birdRect=pygame.Rect(65,50,50,50)
        self.birdStatus=[pygame.image.load('bird3.png'),pygame.image.load('bird2.png'),pygame.image.load('bird3.png')]
        self.status=0      #默认飞行状态
        self.birdx=120     #鸟所在的x轴坐标
        self.birdy=345     #y轴坐标
        self.jump=False    #默认情况小鸟自动降落
        self.jumpSpeed=10  #跳跃高度
        self.live=False    #默认活着
        self.gravity=5     #重力

    def birdupdate(self):
        if self.jump:
            self.jumpSpeed-=1
            self.birdy-=self.jumpSpeed
        else:
            self.gravity+=0.2
            self.birdy+=self.gravity
        self.birdRect[1]=self.birdy

class Pipeline(object):
    '定义一个管道类'
    def __init__(self):
        '定义初始方法'
        self.wallx=400
        self.wally1=-200
        self.wally2 = 600
        self.pineup=pygame.image.load('pine2.gif')
        self.pinedown=pygame.image.load('pine2.gif')

    def updatepipeline(self):
        '水平移动'
        self.wallx-=5
        if self.wallx==0:
            global score
            score += 1
        if self.wallx<-200:
            self.wallx=400
            self.wally1=random.randint(-700,  -100)
            self.wally2=self.wally1+random.randint(800,  1000)

def createmap():
    '定义创建地图的方法'
    screen.fill((255, 255, 255))
    screen.blit(background,(0,0))
    screen.blit(Pipeline.pineup,(Pipeline.wallx,Pipeline.wally1))
    screen.blit(Pipeline.pinedown,(Pipeline.wallx,Pipeline.wally2))
    Pipeline.updatepipeline()
    if Bird.live:
        Bird.status=2
    elif Bird.jump:
        Bird.status=0
    screen.blit(Bird.birdStatus[Bird.status],(Bird.birdx,Bird.birdy))
    Bird.birdupdate()
    screen.blit(font.render(str(score),-1,(255,255,255)),(200,50))
    pygame.display.update()

def checkdead():
    uprect=pygame.Rect(Pipeline.wallx,Pipeline.wally1,Pipeline.pineup.get_width()-200,Pipeline.pineup.get_height())
    downrect=pygame.Rect(Pipeline.wallx,Pipeline.wally2,Pipeline.pinedown.get_width()-200,Pipeline.pinedown.get_height())

    if uprect.colliderect(Bird.birdRect) or downrect.colliderect(Bird.birdRect):
        Bird.live=True
    if not 0<Bird.birdRect[1]<height:
        Bird.live=True
        return True
    else:
        return False

def getresult():
    final_text1='Game Over'
    final_text2='YOUR final score is:'+str(score)
    ft1_font=pygame.font.SysFont('Arial',70)
    ft1_surf=font.render(final_text1,1,(242,3,36))
    ft2_font=pygame.font.SysFont('Arial',50)
    ft2_surf=font.render(final_text2,1,(253,177,6))
    screen.blit(ft1_surf,[screen.get_width()/2-ft1_surf.get_width()/2,100])
    screen.blit(ft2_surf,[screen.get_width()/2-ft2_surf.get_width()/2,200])
    pygame.display.update()

if __name__ == '__main__':
    '主程序'
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 50)
    size = width, height = 400, 690
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()
    Bird = Bird()
    score=0
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.live:
                Bird.jump=True
                Bird.gravity=5
                Bird.jumpSpeed=10
        background = pygame.image.load('background.png')
        if checkdead():
            getresult()
        else:
            createmap()
