import pygame
import button
import CalcFunctions as cf

from sys import exit

pygame.init()
screen = pygame.display.set_mode((280, 350))
pygame.display.set_caption("Calculator")
pygame.display.set_icon(pygame.image.load("calculator.png"))
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 40)


# operations
Plus = button.Button('+', 40, 35, (175, 300), 6, screen, gui_font)
Minus = button.Button('-', 40, 35, (175, 250), 6, screen, gui_font)
Times = button.Button('x', 40, 35, (175, 200), 6, screen, gui_font)
Divide = button.Button('/', 40, 35, (175, 150), 6, screen, gui_font)
Equals = button.Button('=', 40, 85, (230, 250), 6, screen, gui_font)
Delete = button.Button('D', 40, 35, (230, 200), 6, screen, gui_font)
DeleteAll = button.Button('C', 40, 35, (230, 150), 6, screen, gui_font)

# Numbers
Zero = button.Button('0', 40, 35, (10, 300), 6, screen, gui_font)
DoubleZero = button.Button('00', 40, 35, (65, 300), 6, screen, gui_font)
Comma = button.Button(',', 40, 35, (120, 300), 6, screen, gui_font)
One = button.Button('1', 40, 35, (10, 250), 6, screen, gui_font)
Two = button.Button('2', 40, 35, (65, 250), 6, screen, gui_font)
Three = button.Button('3', 40, 35, (120, 250), 6, screen, gui_font)
Four = button.Button('4', 40, 35, (10, 200), 6, screen, gui_font)
Five = button.Button('5', 40, 35, (65, 200), 6, screen, gui_font)
Six = button.Button('6', 40, 35, (120, 200), 6, screen, gui_font)
Seven = button.Button('7', 40, 35, (10, 150), 6, screen, gui_font)
Eight = button.Button('8', 40, 35, (65, 150), 6, screen, gui_font)
Nine = button.Button('9', 40, 35, (120, 150), 6, screen, gui_font)

# Result Screen:
Result1_Rect = pygame.Rect((10, 10), (260, 120))
Result1_Color = '#228DF1'

Result2_Rect = pygame.Rect((8, 8), (264, 124))
Result2_Color = '#FFFFFF'

opType = 0
Result = ""
operator1 = "0"
operator2 = "0"
clicked = False
clickedEquals = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # screen
    screen.fill((94, 129, 162))

    # Operators
    if Plus.draw():
        if not clicked:
            operator2 = '0'
            clicked = True
        if operator2 != '':
            operator1 = cf.add(cf.toInt(operator1), cf.toInt(operator2))
            operator2 = ''
            operator1 = str(operator1)
            Result = str(operator1)
        opType = 1
        clickedEquals = False

    if Minus.draw():
        if not clicked:
            operator2 = '0'
            clicked = True
        if operator2 != '':
            operator1 = cf.subtract(cf.toInt(operator1), cf.toInt(operator2))
            operator2 = ''
            operator1 = str(operator1)
            Result = str(operator1)
        opType = 2
        clickedEquals = False

    if Times.draw():
        if not clicked:
            operator2 = '1'
            clicked = True
        if operator2 != '':
            operator1 = cf.multiply(cf.toInt(operator1), cf.toInt(operator2))
            operator2 = ''
            operator1 = str(operator1)
            Result = str(operator1)
        opType = 3
        clickedEquals = False

    if Divide.draw():
        if not clicked:
            operator2 = '1'
            clicked = True
        if operator2 != '':
            operator1 = cf.devide(cf.toInt(operator1), cf.toInt(operator2))
            operator2 = ''
            operator1 = str(operator1)
            Result = str(operator1)
        opType = 4
        clickedEquals = False

    if Equals.draw():
        if opType == 1 and operator2 != '':
            operator1 = cf.add(cf.toInt(operator1), cf.toInt(operator2))
            operator2 = ''
            operator1 = str(operator1)
            Result = str(operator1)
        elif opType == 2 and operator2 != '':
            operator1 = cf.subtract(cf.toInt(operator1), cf.toInt(operator2))
            operator2 = ''
            operator1 = str(operator1)
            Result = str(operator1)
        elif opType == 3 and operator2 != '':
            operator1 = cf.multiply(cf.toInt(operator1), cf.toInt(operator2))
            operator2 = ''
            operator1 = str(operator1)
            Result = str(operator1)
        elif opType == 4 and operator2 != '':
            operator1 = cf.devide(cf.toInt(operator1), cf.toInt(operator2))
            operator2 = ''
            operator1 = str(operator1)
            Result = str(operator1)
        opType = 0
        clickedEquals = True

    if Delete.draw():
        if clicked:
            operator2 = cf.delete(operator2)
        else:
            operator2 = cf.delete(operator2)

    if DeleteAll.draw():
        Result = cf.clearString()
        operator2 = cf.clearString()
        operator1 = cf.clearString()
        opType = 0
        clicked = False
        clickedEquals = False

    # Numbers
    if Zero.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '0')
    if DoubleZero.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '00')
    if Comma.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '.')
    if One.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '1')
    if Two.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '2')
    if Three.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '3')
    if Four.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '4')
    if Five.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '5')
    if Six.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '6')
    if Seven.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '7')
    if Eight.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '8')
    if Nine.draw() and not clickedEquals:
        operator2 = cf.AddChar(operator2, '9')

    # Result Screen
    pygame.draw.rect(screen, Result2_Color, Result2_Rect, border_radius=5)
    pygame.draw.rect(screen, Result1_Color, Result1_Rect, border_radius=5)

    if not clicked:
        operator1 = operator2
        text_surf = gui_font.render(operator1, True, '#FFFFFF')
        text_rect = text_surf.get_rect(center=(220, 40))
        screen.blit(text_surf, text_rect)
    else:
        text_surf = gui_font.render(operator1, True, '#FFFFFF')
        text_rect = text_surf.get_rect(center=(220, 40))
        screen.blit(text_surf, text_rect)

        text_surf = gui_font.render(operator2, True, '#FFFFFF')
        text_rect = text_surf.get_rect(center=(220, 100))
        screen.blit(text_surf, text_rect)

    if opType == 1:
        text_surf = gui_font.render('+', True, '#FFFFFF')
        text_rect = text_surf.get_rect(center=(50, 100))
        screen.blit(text_surf, text_rect)
    if opType == 2:
        text_surf = gui_font.render('-', True, '#FFFFFF')
        text_rect = text_surf.get_rect(center=(50, 100))
        screen.blit(text_surf, text_rect)
    if opType == 3:
        text_surf = gui_font.render('x', True, '#FFFFFF')
        text_rect = text_surf.get_rect(center=(50, 100))
        screen.blit(text_surf, text_rect)
    if opType == 4:
        text_surf = gui_font.render('/', True, '#FFFFFF')
        text_rect = text_surf.get_rect(center=(50, 100))
        screen.blit(text_surf, text_rect)

    pygame.display.update()
    clock.tick(60)







































