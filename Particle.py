from math import cos, sin, radians
import pygame

class Particle:

    def __init__(self,radius, pos, mass = 1,velocity = 0, direction = 0, color = (255,0,0)):
        self.pos = pos

        self.radius = radius

        self.vel = [velocity * cos(direction), velocity * sin(direction)]

        self.color = color

        self.mass = mass

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


    def apply_force(self, force, dt):
        #update position
        self.pos[0], self.pos[1] = self.pos[0] + self.vel * dt, self.pos[1] + self.vel * dt

        #update velocity
        self.vel[0], self.vel[1] = self.vel[0] + force[0] * dt, self.vel[1] + force[1] * dt


