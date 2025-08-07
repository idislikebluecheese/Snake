import pygame, sys, random
from pygame.math import Vector2
pygame.init()
font = pygame.font.Font(None, 60)
#####Settings Modify this to your liking 
cs = 10 #10
cq = 50 #50
SNAKE_COLOR = "#3dd77f" #3dd77f
APPLE_COLOR = "#ff0000" #ff0000
BG_COLOR = (67,67,67)
DELAY = 55 #200 #55
GROW = True #True
GAY_BACKGROUND = False #False #dont turn this on if you have elipsy
GAY_SNAKE = False # False
GAY_SNAKE2 = False # False
DEADLY_EDGE = True # True
DEADLY_TAIL = True # True
#####Settings
screen = pygame.display.set_mode((cs*cq, cs*cq))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")
class Food:
 def __init__(self):
  self.cord = Vector2(random.randint(0, cq-1), random.randint(0, cq-1))
 def draw(self):
  rect = pygame.Rect(self.cord.x * cs, self.cord.y * cs, cs, cs)
  pygame.draw.rect(screen, APPLE_COLOR, rect)
 def update(self):
  self.cord = Vector2(random.randint(0, cq-1), random.randint(0, cq-1))
class Snake:
 def __init__(self):
  self.body = [Vector2(6,7), Vector2(6,8), Vector2(6,8)]
  self.dir = Vector2(1,0)
  self.SNAKE_COLOR = SNAKE_COLOR
  self.Running = True
  self.score = 0
  self.score2 = 0
 def draw(self):
  for i in self.body:
   rect = pygame.Rect(i.x * cs, i.y * cs, cs, cs)
   if i.x > cq - 1:
    self.body[0] = Vector2(0,self.body[0][1])
    self.die() if DEADLY_EDGE else None
   elif i.x < 0:
    self.body[0] = Vector2(cq-1,self.body[0][1])
    self.die() if DEADLY_EDGE else None
   elif i.y > cq - 1:
    self.body[0] = Vector2(self.body[0][0],0)
    self.die() if DEADLY_EDGE else None
   elif i.y < 0:
    self.body[0] = Vector2(self.body[0][0],cq-1)
    self.die() if DEADLY_EDGE else None
   if GAY_SNAKE:
    self.SNAKE_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
   pygame.draw.rect(screen, self.SNAKE_COLOR, rect)
   if self.body[0] == food.cord:
    food.update()
    self.score += 1
    if GROW == True:
     self.body.insert(0, self.body[0] + self.dir)
 def update(self):
  if self.body[0] in self.body[1:] and DEADLY_TAIL:
   self.die()
  if GAY_SNAKE2:
   self.SNAKE_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  self.body = self.body[:-1]
  self.body.insert(0, self.body[0] + self.dir)
 def die(self):
  food.update()
  self.body = [Vector2(6,7), Vector2(6,8), Vector2(6,8)]
  self.dir = Vector2(1,0)
  self.update()
  self.Running = False
  self.score2 = self.score
  self.score = 0
food = Food()
snake = Snake()
uv = pygame.USEREVENT
pygame.time.set_timer(uv, DELAY)
while True:
 for ev in pygame.event.get():
  if ev.type == 768:
   match ev.key:
    case 1073741906:
     if not snake.dir == Vector2(0, 1):
      snake.dir = Vector2(0, -1)
      snake.Running = True
    case 1073741905:
     if not snake.dir == Vector2(0, -1):
      snake.dir = Vector2(0, 1)
      snake.Running = True
    case 1073741903:
     if not snake.dir == Vector2(-1, 0):
       snake.dir = Vector2(1, 0)
       snake.Running = True
    case 1073741904:
     if not snake.dir == Vector2(1, 0):
       snake.dir = Vector2(-1, 0)
       snake.Running = True
  if ev.type == uv:
   snake.update() if snake.Running else None
  if ev.type == pygame.QUIT:
   pygame.quit()
   sys.exit()
 screen.fill(BG_COLOR)
 snake.draw()
 food.draw()
 if GAY_BACKGROUND:
  BG_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
 ts = font.render(f"Score: {snake.score2}", True, "#362887")
 if not snake.Running:
  screen.blit(ts, (cs*cq/3,cs*cq/3))
 pygame.display.update()
 clock.tick(1000)
