import pygame  # type:ignore
import settings  # type:ignore

width = settings.width
height = settings.height

import koch_fractal
import dragon_fractal
import sierpinski_fractal
import tree_fractal
import hilbert_fractal
import Levy_fractal
import our_fractal

width, height = 600,600

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fraktale")
#n = int(input("Enter n: "))

#koch_fractal.start(n)

font = pygame.font.SysFont("arial", 20)

input_box = pygame.Rect(width / 2, height / 2, 140, 32)
input_box.center = (width / 2, height / 2)
inputtext = font.render("Iterationen (n): ", True, pygame.Color('dodgerblue2'))
inputtext_rect = inputtext.get_rect()
inputtext_rect.centery = input_box.centery
inputtext_rect.x = input_box.x - inputtext_rect.width
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
dimensions = (3,2)
choices = ["Koch Schneeflocke", "Drachenkurve", "Pythagoras Baum", "Sierpinski Dreieck", "Hilbert Kurve", "Levy Kurve"]

inputmenu = True
def draw_choices(n: int):
    screen.fill((30, 30, 30))
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            rect = pygame.Rect(
                            i * (width / dimensions[0]),
                           (j * (width / dimensions[1])),
                           width / dimensions[0],
                           height / dimensions[1]
                               )
            pygame.draw.rect(screen, "#A0A0A0", rect, 1)
            index = j * (dimensions[0]) + i
            surf = font.render(choices[index], True, "#F0F0F0")
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
            draw_fractal(n, y * dimensions[0] + x)
            return


        pygame.display.update()

def draw_fractal(n: int, id = 0):
    if id == 0:
        points = koch_fractal.start(n)
    elif id == 1:
        points = dragon_fractal.start(n)
    elif id == 2:
        points = tree_fractal.start(n)
    elif id == 3:
        points = sierpinski_fractal.start(n)
    elif id == 4:
        points = hilbert_fractal.start(n)
    elif id == 5:
        points = Levy_fractal.start(n)
    else:
        print(id)
        return

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
        color = color_active
        active = True
    pygame.display.update()

