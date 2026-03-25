import sys
import pygame
from .base_settings import *
from .targets import Target
from .effects import Particle

def run_game():
    # initialisation
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('PyPortal - Aim Trainer')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 28, bold=True)

    score = 0
    targets = []
    particles = []
    start_ticks = pygame.time.get_ticks() #Time when lauching the game

    pygame.mouse.set_visible(False)

    #Timer to make appear the targets
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, SPAWN_RATE)

    run = True
    while run:
        screen.fill(WHITE)

        # Board behind the game (bg)
        for i in range(0, WIDTH, 40):
            pygame.draw.line(screen, (230,230,240), (i,0), (i,HEIGHT))
        for j in range(0, HEIGHT, 40):
            pygame.draw.line(screen, (230,230,240), (0, j), (WIDTH, j))

        #calculate the past time
        time_left = max(0, GAME_DURATION - (pygame.time.get_ticks() - start_ticks) / 1000)
        if time_left <= 0:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == SPAWN_EVENT:
                targets.append(Target())

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                #check if a target is hit (collision circle-point)
                for t in targets[:]:
                    distance = ((t.x - mouse_pos[0]) ** 2 + (t.y - mouse_pos[1]) ** 2) ** 0.5
                    if distance <= t.radius:
                        score += t.point
                        for _ in range(12):
                            particles.append(Particle(t.x, t.y, t.color))
                        if t in targets:
                            targets.remove(t)
                        break

        # Update and Draw
        for p in particles[:]:
            p.update()
            p.draw(screen)
            if p.lifetime <= 0:
                particles.remove(p)

        #draw the targets et manage their life durancy
        current_time = pygame.time.get_ticks()
        for t in targets[:]:
            if current_time - t.spawn_time > TARGET_LIFESPAN: #dissapear after 1.5sec
                if t in targets:
                    targets.remove(t)
            else:
                t.draw(screen)

        # UI and Crosshair
        screen.blit(font.render(f"SCORE: {score}", True, DARK), (20,20)) # left
        screen.blit(font.render(f"{int(time_left)}s", True, RED), (WIDTH - 80, 20)) # Up right

        mx, my = pygame.mouse.get_pos()
        pygame.draw.line(screen, DARK, (mx - 10, my), (mx + 10, my), 2)
        pygame.draw.line(screen, DARK, (mx, my - 10), (mx, my + 10), 2)

        pygame.display.flip()
        clock.tick(FPS)

    screen.fill((5, 5, 17))
    over_text = font.render("TIME'S UP !", True, WHITE)
    over_score = font.render(f"SCORE: {score}", True, WHITE)
    screen.blit(over_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))
    screen.blit(over_score, (WIDTH // 2 - 50, HEIGHT // 2 ))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait 2 seconds for the user in order that he can read the end page

    pygame.quit()
    return score #return the score for flask

