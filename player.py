import pygame
import config


class Player:
    def __init__(self, x: int, y: int, speed: int, zoom: int) -> None:
        self.x      = x
        self.y      = y
        self.speed  = speed
        self.zoom   = zoom

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
    
    def keyboard_move(self, deltatime):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.move_right = True
                elif event.key == pygame.K_LEFT:
                    self.move_left = True
                elif event.key == pygame.K_UP:
                    self.move_up = True
                elif event.key == pygame.K_DOWN:
                    self.move_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                elif event.key == pygame.K_RIGHT:
                    self.move_right = False
                elif event.key == pygame.K_UP:
                    self.move_up = False
                elif event.key == pygame.K_DOWN:
                    self.move_down = False
            elif event.type == pygame.MOUSEWHEEL:
                if self.zoom < config.zoom and event.y > 0:
                    self.zoom = self.zoom + 0.2
                elif self.zoom > config.min_zoom and event.y < 0:
                    self.zoom = self.zoom - 0.2
                if self.zoom < config.min_zoom:
                    self.zoom = config.min_zoom
                self.zoom = round(self.zoom, 1)
        
        if self.move_right:
            self.x += (self.speed * self.zoom) / deltatime
        if self.move_left:
            self.x -= (self.speed * self.zoom) / deltatime
        if self.move_down:
            self.y -= (self.speed * self.zoom) / deltatime
        if self.move_up:
            self.y += (self.speed * self.zoom) / deltatime

    def get_coords(self):
        return (self.x, self.y)