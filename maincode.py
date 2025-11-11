import pygame
import random
import sys

print("Welcome to the ForLorn bird game!")

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 400
HEIGHT = 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (254, 135, 56)
GREEN = (81, 21, 21)

# Bird settings
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
gravity = 1.0
bird_movement = 0
jump_strength = -8

# Load custom bird image
bird_image = pygame.image.load(r"C:\Users\KRISHNA PC\Downloads\rjr.png")  # Replace with your actual path
bird_image = pygame.transform.scale(bird_image, (40, 40))  # Resize as needed

# Pipe settings
pipe_width = 70
pipe_gap = 150
pipe_speed = 4
pipes = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def create_pipe():
    height = random.randint(100, 400)
    return {'x': WIDTH, 'top': height - pipe_gap // 2, 'bottom': height + pipe_gap // 2}

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe['x'], 0, pipe_width, pipe['top']))
        pygame.draw.rect(screen, GREEN, (pipe['x'], pipe['bottom'], pipe_width, HEIGHT - pipe['bottom']))

def check_collision(bird_y, pipes):
    if bird_y - bird_radius <= 0 or bird_y + bird_radius >= HEIGHT:
        return True
    for pipe in pipes:
        if (bird_x + bird_radius > pipe['x'] and bird_x - bird_radius < pipe['x'] + pipe_width):
            if bird_y - bird_radius < pipe['top'] or bird_y + bird_radius > pipe['bottom']:
                return True
    return False

def display_score(score):
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

# Game loop
running = True
while running:
    clock.tick(30)
    screen.fill(BLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_movement = jump_strength

    # Bird movement
    bird_movement += gravity
    bird_y += bird_movement

    # Pipe movement
    if not pipes or pipes[-1]['x'] < WIDTH - 200:
        pipes.append(create_pipe())

    for pipe in pipes:
        pipe['x'] -= pipe_speed

    pipes = [pipe for pipe in pipes if pipe['x'] + pipe_width > 0]

    # Check for collisions
    if check_collision(bird_y, pipes):
        pygame.quit()
        if score > 2:
            print("Nice, your score is - ",score)
        elif score <= 2:
            print("You NOOB, you only scored - ",score,"hahaha")
        elif score > 5:
            print("No frickin way dude, you scored - ",score,"Great Job!")
#        print(f"Game Over! Final Score: {score}")
        sys.exit()

    # Update score
    for pipe in pipes:  
        if pipe['x'] + pipe_width == bird_x:
            score += 1

    # Draw everything
    screen.blit(bird_image, (bird_x - 20, int(bird_y) - 20))  # Adjust position to center the image
    draw_pipes(pipes)
    display_score(score)

    pygame.display.update()
