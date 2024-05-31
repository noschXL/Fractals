import pygame
from settings import *

import koch_fractal
import dragon_fractal
import sierpinski_fractal

pygame.init()

screen = pygame.display.set_mode((width, height))

#n = int(input("Enter n: "))

#koch_fractal.start(n)

font = pygame.font.SysFont("arial", 20)


input_box = pygame.Rect(width / 2, height / 2, 140, 32)
input_box.center = (width / 2, height / 2)
inputtext = font.render("enter the number of steps (n): ", True, pygame.Color('dodgerblue2'))
inputtext_rect = inputtext.get_rect()
inputtext_rect.centery = input_box.centery
inputtext_rect.x = input_box.x - inputtext_rect.width
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
dimensions = (2,2)
choices = ["koch_fractal", "dragon_curve", "sierpinski_triangle", "Empty"]

inputmenu = True
def draw_choices(n: int):
    screen.fill((30, 30, 30))
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            rect = pygame.Rect(i * (width / dimensions[0]), (j * (width / dimensions[1])), height / dimensions[1], height / dimensions[1])
            pygame.draw.rect(screen, "#A0A0A0", rect, 1)
            surf = font.render(choices[i * dimensions[0] + j], True, "#F0F0F0")
            screen.blit(surf, (rect.centerx - surf.get_rect().width / 2, rect.centery - surf.get_rect().height / 2))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return
        
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()
            x = mouse[0] //  (width / dimensions[0])
            y = mouse[1] // (height / dimensions[1])
            draw_fractal(n, x * dimensions[0] + y)
            return


        pygame.display.update()

def draw_fractal(n: int, id = 0):
    
    if id == 0:
        points = koch_fractal.start(n)
    elif id == 1:
        points = dragon_fractal.start(n)
    elif id == 2:
        points = sierpinski_fractal.start(n)

    screen.fill((30, 30, 30))
    pygame.draw.lines(screen, "#00FFFF", False, points, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return
        pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
            # Change the current color of the input box.
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    n = int(text)
                    text = ''
                    inputmenu = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    if inputmenu:
        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        maxwidth = max(200, txt_surface.get_width()+10)
        input_box.w = maxwidth
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        screen.blit(inputtext, inputtext_rect)
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
    else:
        draw_choices(n)
        inputmenu = True
        color = color_inactive
        active = False
    pygame.display.update()

