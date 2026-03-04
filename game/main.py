import sys
import random
import pygame

# initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyPortal - Aim Trainer')
clock = pygame.time.Clock()

#Colors
WHITE = (240, 240, 255)
DARK = (5,5,17)
GREEN = (34,197,94)
ORANGE = (249,115,22)
RED = (239,68,68)

class Target:
    def __init__(self):
        # define the difficulty (size vs points)
        rand = random.random()
        if rand > 0.6: # 60% grand
            self.radius, self.point, self.color = 30, 10, GREEN
        elif rand > 0.2: # 40% medium
            self.radius, self.point, self.color = 20, 25, ORANGE
        else: # 20% small
            self.radius, self.point, self.color = 10, 50, RED

        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.spawn_time = pygame.time.get_ticks()

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def run_game():
    game_duration = 30 #Time in secondes
    start_ticks = pygame.time.get_ticks() #Time when lauching the game

    score = 0
    targets = []
    run = True

    #Timer to make appear the targets
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 800)

    while run:

        #calculate the past time
        seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
        time_left = max(0, game_duration - seconds_passed)

        if time_left <= 0:
            run = False

        screen.fill(WHITE)

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
                        targets.remove(t)

        #draw the targets et manage their life durancy
        current_time = pygame.time.get_ticks()
        for t in targets[:]:
            if current_time - t.spawn_time > 1500: #dissapear after 1.5sec
                targets.remove(t)
            else:
                t.draw()

        font = pygame.font.SysFont('Inter', 30)
        timer_text = font.render(f'Temps: {int(time_left)}s' , True, RED)
        score_text = font.render(f"Score: {score}", True, DARK)

        screen.blit(timer_text, (WIDTH - 150, 20)) # Up right
        screen.blit(score_text, (20, 20)) # Up left

        pygame.display.flip()
        clock.tick(60)

    screen.fill((5, 5, 17))
    over_text = font.render("TIME'S UP !", True, WHITE)
    over_score = font.render(f"SCORE: {score}", True, WHITE)
    screen.blit(over_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))
    screen.blit(over_score, (WIDTH // 2 - 50, HEIGHT // 2 ))
    pygame.display.flip()
    pygame.time.wait(2000)  # Attend 2 secondes pour que le joueur voie son score final

    pygame.quit()
    return score #return the score for flask

run_game()
