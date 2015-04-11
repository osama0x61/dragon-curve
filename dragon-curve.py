import sys
import math
import copy
import random
import pygame

RESOLUTION = (800, 600)
CAPTION = 'Cells'
BGCOLOR = (240, 240, 240)

class Cursor:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        
    def rotate(self, angle):
        pass

def vectorangle(dx, dy):
    angle = math.acos(dx/(math.sqrt(dx*dx + dy*dy)))
    if dy < 0: angle *= -1
    return angle

##    if dx == 0:
##        if dy < 0:
##            angle = -math.pi/2
##        elif dy > 0:
##            angle = math.pi/2
##    else:
##        angle = math.atan(dy/dx)
##    return angle

def vline(x1, y1, length, theta):
    x2 = x1 + (length * math.cos(theta))
    y2 = y1 + (length * math.sin(theta))
    return x2, y2

def gendragon(x1, y1, x2, y2, n, dirflag=True):
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt((dx*dx) + (dy*dy))
    angle = vectorangle(dx, dy)
    rot_angles = (math.pi/4, -math.pi/4) #[::-1] # rotation angles to alternate between

    if n > 0:
        direction = 0
        if dirflag: direction = 1
        theta = rot_angles[direction%len(rot_angles)]
        #print "theta = %s, n = %d" %(theta, n)
        segment_length = math.sqrt((length**2)/2)
        x3, y3 = vline(x1, y1, segment_length, angle + theta)
        return gendragon(x1, y1, x3, y3, n - 1, False)[:-1] + gendragon(x3, y3, x2, y2, n - 1, True)
    else:
        return [(x1, y1), (x2, y2)]
        

def mainloop():
    # init pygame
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(CAPTION)
    screen.fill(BGCOLOR)
    
    # init stuff
    angle = 0
    origin = (RESOLUTION[0]/2, RESOLUTION[1]/2)

##    pgroups = []
##    colors = []
##    for i in range(1):

##        pgroups.append(points)
##        colors.append([255*random.random() for c in range(3)])

    depth_counter = 0
    max_depth = 17

##    depth = 10
##    points = gendragon(origin[0]-150, origin[1], origin[0]+150, origin[1], depth)
##    colors = [[255 for i in range(3)] for j in range(len(points))]
    
    frames = 0
    done = False
    while not done:
        # events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done = True
            elif (event.type==pygame.KEYUP and
                  event.key==pygame.K_SPACE):
                pass
        
        # update
        if ((frames == 0) or
            (frames%(0.5*fps) == 0)):
            depth = depth_counter%max_depth
            print "depth = ", depth
            points = gendragon(origin[0]-200, origin[1]+100, origin[0]+200, origin[1]+100, depth)
            colors = [[255*random.random() for i in range(3)] for j in range(len(points))]
            depth_counter += 1
##            print points
##            print

        # draw
        screen.fill(BGCOLOR)
        
##        for points in pgroups:
        i = 0
        lastpoint = points[0]
        for point in points[1:]:
            color = colors[i]
            pygame.draw.line(screen,
                             (50, 50, 50),
##                             color,
                             lastpoint,
                             point,
                             2)
            lastpoint = point
            i += 1

        pygame.display.flip()
        clock.tick(fps)
        frames += 1
    # print cells
    pygame.quit()
    
def main():
    mainloop()

if __name__=='__main__':
    main()
