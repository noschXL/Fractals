import pygame
import koch_fractal
import Point_Walker
from settings import *

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

#pygame.draw.lines(screen, "#FFFFFF", False, koch_fractal.points, 1)

inputmenu = True
def draw_fractal(n: int, id = 0):
    
    if id == 0:
        points = koch_fractal.start(n)

    screen.fill((30, 30, 30))
    pygame.draw.lines(screen, "#FFFFFF", False, points, 1)

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
                    print(text)
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
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        screen.blit(inputtext, inputtext_rect)
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
    else:
        draw_fractal(n)
        inputmenu = True
        color = color_inactive
        active = False
    pygame.display.update()

