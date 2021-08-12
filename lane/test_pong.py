#!/usr/bin/env python3
import pygame


ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

FENSTERBREITE = 640
FENSTERHOEHE = 480
BALL_DURCHMESSER = 20

class Ball:
    bewegung_x = 4
    bewegung_y = 4
    
    def __init__(self, scre):
      self.ballpos_x = 10
      self.ballpos_y = 300
   
   def move(self, scre):
      pygame.draw.ellipse(scre, WEISS, [self.ballpos_x, self.ballpos_y, BALL_DURCHMESSER, BALL_DURCHMESSER])
      self.ballpos_x += self.bewegung_x
      self.ballpos_y += self.bewegung_y

      if self.ballpos_y > FENSTERHOEHE - BALL_DURCHMESSER or self.ballpos_y < 0:
            self.bewegung_y = self.bewegung_y * -1

      if self.ballpos_x > FENSTERBREITE - BALL_DURCHMESSER or self.ballpos_x < 0:
            self.bewegung_x = self.bewegung_x * -1


if __name__ == "__main__":
  run = True

  pygame.init()
  screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))
  pygame.display.set_caption('Pong')
  clock = pygame.time.Clock()
  ball = Ball(screen) 

  while run:
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       run = False

   screen.fill(SCHWARZ)
   ball.move(screen)
   pygame.display.flip()
   clock.tick(60)

  pygame.quit()
  quit()
