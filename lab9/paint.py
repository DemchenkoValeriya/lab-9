import pygame

WIDTH, HEIGHT = 1200, 800
FPS = 90
draw = False
radius = 2
color = 'blue'
mode = 'pen'

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('white'))
font = pygame.font.SysFont('None', 60)

# Функция для рисования линии
def drawLine(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, int(y)), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (int(x), y), width)

# Функция для рисования круга
def drawCircle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (int(x), int(y)), int(radius), width)

# Функция для рисования прямоугольника
def drawRectangle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)

# Функция для рисования квадрата
def drawSquare(screen, start, end, color):
    x1, y1 = start
    x2, y2 = end
    mn = min(abs(x2 - x1), abs(y2 - y1))

    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn))
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn))
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn))
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn))

# Функция для рисования прямоугольного треугольника 
def drawRightTriangle(screen, start, end, color):
    x1, y1 = start
    x2, y2 = end
    if x2 > x1 and y2 > y1:
        pygame.draw.lines(screen, pygame.Color(color), True, ((x1, y1), (x2, y2), (x1, y2)), 1)
    if y2 > y1 and x1 > x2:
        pygame.draw.lines(screen, pygame.Color(color), True, ((x1, y1), (x2, y2), (x1, y2)), 1)
    if x1 > x2 and y1 > y2:
        pygame.draw.lines(screen, pygame.Color(color), True, ((x1, y1), (x2, y2), (x2, y1)), 1)
    if x2 > x1 and y1 > y2:
        pygame.draw.lines(screen, pygame.Color(color), True, ((x1, y1), (x2, y2), (x2, y1)), 1)

# Функция для рисования равностороннего треугольника
def drawEquilateralTriangle(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    width_b = abs(x2 - x1)
    height = (3**0.5) * width_b / 2

    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)), width)

# Функция для рисования ромба
def drawRhombus(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.lines(screen, pygame.Color(color), True, (
        ((x1 + x2) / 2, y1),
        (x1, (y1 + y2) / 2),
        ((x1 + x2) / 2, y2),
        (x2, (y1 + y2) / 2)
    ), width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            # Обработка горячих клавиш для смены режима рисования
            if event.key == pygame.K_r:
                mode = 'rectangle'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_p:
                mode = 'pen'
            if event.key == pygame.K_e:
                mode = 'erase'
            if event.key == pygame.K_s:
                mode = 'square'
            if event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))

            # Смена цвета с помощью горячих клавиш
            if event.key == pygame.K_1:
                color = 'black'
            if event.key == pygame.K_2:
                color = 'green'
            if event.key == pygame.K_3:
                color = 'red'
            if event.key == pygame.K_4:
                color = 'blue'
            if event.key == pygame.K_5:
                color = 'yellow'
            if event.key == pygame.K_t:
                mode = 'right_tri'
            if event.key == pygame.K_u:
                mode = 'eq_tri'
            if event.key == pygame.K_h:
                mode = 'rhombus'

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
            # Вызов функции для рисования в зависимости от режима
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, color)
            elif mode == 'right_tri':
                drawRightTriangle(screen, prevPos, event.pos, color)
            elif mode == 'eq_tri':
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'rhombus':
                drawRhombus(screen, prevPos, event.pos, radius, color)

        if event.type == pygame.MOUSEMOTION and draw:
            # Рисование в режиме "pen"
            if mode == 'pen':
                drawLine(screen, prevPos, event.pos, radius, color)
                prevPos = event.pos
            elif mode == 'erase':
                pygame.draw.circle(screen, pygame.Color('white'), event.pos, 20)

    pygame.display.flip()  # Обновление экрана
    clock.tick(FPS)  # Контроль FPS
