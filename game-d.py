import pygame
from random import randint

pygame.init()

# initializing variables to account for the number of balls caught, and total dropped
score = 0
total = 0

myfont = pygame.font.SysFont('monospace', 50) # creating a font to write the score in

# Making dictionaries with settings for everything.

display = {
  "width": 800,
  "height": 600
}

paddle = {
  "width": 200,
  "height": 20,
  "x": 300,
  "y": 580,
  "velocity": 50
}

ball = {
  "radius": 15,
  "y": 30,
  "x": randint(0, display["width"]),
  "velocity": 40
}

# creating a window, and launching our game
win = pygame.display.set_mode((display["width"], display["height"])) # 800 width, 600 height
while True:
  pygame.time.delay(100)
  win.fill((255, 255, 255))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    paddle["x"] -= paddle["velocity"]
    if paddle["x"] < 0 :
      paddle["x"] = 0
  if keys[pygame.K_RIGHT]:
    paddle["x"] += paddle["velocity"]
    if paddle["x"] + paddle["width"] > display["width"] :
      paddle["x"] = display["width"] - paddle["width"]
  pygame.draw.rect(win, (255, 0, 0), (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))
  ball["y"] += ball["velocity"]
  pygame.draw.circle(win, (0, 0, 255), (ball["x"], ball["y"]), ball["radius"])
  if ball["y"] + ball["radius"] >= paddle["y"]:
    if ball["x"] > paddle["x"] and ball["x"] < paddle["x"] + paddle["width"]:
      score += 1
    total += 1
    ball["y"] = 30
    ball["x"] = randint(0, display["width"] - ball["radius"])

  textsurface = myfont.render("score: {0}/{1}".format(score, total), False, (0, 0, 0))
  win.blit(textsurface, (10, 10))
  
  pygame.display.update()
        
pygame.quit()
