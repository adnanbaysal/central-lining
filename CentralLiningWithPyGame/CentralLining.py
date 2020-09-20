import pygame
from time import sleep

line = pygame.draw.aaline


def draw_lines_center2edges(screen, width, height, center, step, line_width):
    for i in range(0, width, step):
        line(screen, (255, 0, 0), center, (i, 0), line_width)
        line(screen, (255, 0, 0), center, (i, height - 1), line_width)
    for i in range(0, height, step):
        line(screen, (255, 0, 0), center, (0, i), line_width)
        line(screen, (255, 0, 0), center, (width - 1, i), line_width)


def draw_2center_lines(width, height, step=1, line_width=1):
    screen = pygame.display.set_mode((width, height))
    point_a = (int(width / 3), int(height / 2))
    point_b = (int(2 * width / 3), int(height / 2))
    background_colour = (255, 255, 255)
    screen.fill(background_colour)
    draw_lines_center2edges(screen, width, height, point_a, step, line_width)
    draw_lines_center2edges(screen, width, height, point_b, step, line_width)
    pygame.display.flip()


def two_center_animating():
    for i in range(50):
        draw_2center_lines(1200, 800, step=i + 1)
        sleep(0.04)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def draw_3center_lines(width, height, step=1, line_width=1):
    screen = pygame.display.set_mode((width, height))
    point_a = (int(width / 2), int(height / 3))
    point_b = (int(width / 3), int(2 * height / 3))
    point_c = (int(2 * width / 3), int(2 * height / 3))
    background_colour = (255, 255, 255)
    screen.fill(background_colour)
    draw_lines_center2edges(screen, width, height, point_a, step, line_width)
    draw_lines_center2edges(screen, width, height, point_b, step, line_width)
    draw_lines_center2edges(screen, width, height, point_c, step, line_width)
    pygame.display.flip()


def three_center_animating():
    for i in range(50):
        draw_3center_lines(900, 900, step=i + 1)
        sleep(0.5)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def draw_4center_lines(width, height, step=1, line_width=1):
    screen = pygame.display.set_mode((width, height))
    point_a = (int(width / 3), int(height / 3))
    point_b = (int(width / 3), int(2 * height / 3))
    point_c = (int(2 * width / 3), int(height / 3))
    point_d = (int(2 * width / 3), int(2 * height / 3))
    background_colour = (255, 255, 255)
    screen.fill(background_colour)
    draw_lines_center2edges(screen, width, height, point_a, step, line_width)
    draw_lines_center2edges(screen, width, height, point_b, step, line_width)
    draw_lines_center2edges(screen, width, height, point_c, step, line_width)
    draw_lines_center2edges(screen, width, height, point_d, step, line_width)
    pygame.display.flip()


def four_center_animating():
    for i in range(50):
        draw_4center_lines(900, 900, step=i + 1)
        sleep(0.5)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def two_moving_center_animating():
    step = 10
    width = 1200
    height = 800
    line_width = 1
    for i in range(400):
        screen = pygame.display.set_mode((width, height))
        point_a = (int(width / 3), int(height / 2) + i)
        point_b = (int(2 * width / 3), int(height / 2) - i)
        background_colour = (255, 255, 255)
        screen.fill(background_colour)
        draw_lines_center2edges(screen, width, height, point_a, step, line_width)
        draw_lines_center2edges(screen, width, height, point_b, step, line_width)
        pygame.display.flip()
        sleep(0.01)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    two_moving_center_animating()
    # two_center_animating()
    # three_center_animating()
    # four_center_animating()
