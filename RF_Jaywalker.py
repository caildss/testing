import pygame
import random

# ---- Setting up pygame ----------------------------
pygame.init()
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jaywalker")
# ---------------------------------------------------- 

# --------- set sprite ----------------------------------------------------------------------------------
background = pygame.image.load("c:/Users/anand/Downloads/road.jpeg")

player_img = [
    pygame.transform.scale(pygame.image.load("c:/Users/anand/Downloads/walk.png"), (135, 155)),
    pygame.transform.scale(pygame.image.load("c:/Users/anand/Downloads/walkk.png"), (135, 155)),
    pygame.transform.scale(pygame.image.load("c:/Users/anand/Downloads/walkkk.png"), (135, 155))
]
current_frame = 0  # Start with the first frame
frame_delay = 10   # Delay between frames (lower = faster animation)
frame_counter = 0  # Counter to control frame updates

red_car = pygame.transform.scale(pygame.image.load("c:/Users/anand/Downloads/rw.png"), (145, 165))
blue_car = pygame.transform.scale(pygame.image.load("c:/Users/anand/Downloads/bw.png"), (145, 165))
green_car = pygame.transform.scale(pygame.image.load("c:/Users/anand/Downloads/gw.png"), (145, 165))

heart_img = pygame.transform.scale(pygame.image.load("c:/Users/anand/Downloads/heartt.png"), (50, 50))
# ------------------------------------------------------------------------------------------------------

#---------- variable for sprites --------------------------
lanes = [250, 460, 680]   # theres 3 lanes
time_left = 30  # Time in seconds
start_ticks = pygame.time.get_ticks()  # Start time

player_lane = 1           # player start midel
player_y = height - 100   # player y position
player_width = 135
player_height = 155

hearts = 3                # player hearts

car_images = [red_car, green_car, blue_car]
car_image = random.choice(car_images)  # Randomly select a car image
cars = []
car_speed = 7                # speed of the car
# ---------------------------------------------------------

# --------------- idk random setup---------------------------------------------------------------------------
delay = pygame.time.Clock()
def show_timer(time_left):
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time: {time_left}s", True, (255, 255, 255))
    screen.blit(timer_text, (650, 10))  # Draw the timer at the top-right corner
    
player_x = lanes[player_lane] - player_width // 2   # Position player in middle lane
player_y = 800 - player_height - 10  # Position player at bottom of screen

player = pygame.Rect(player_x, player_y, player_width, player_height) # Define player's rect for collision
#-------------------------------------------------------------------------------------------------------------


# ------------------------------------------GAME FR-------------------------------------------------
running = True
while running:
    
    # Draw sprites
    screen.blit(background, (0, 0))
    screen.blit(player_img[current_frame], (lanes[player_lane] - 25, player_y))
    for i in range(hearts):
        screen.blit(heart_img, (width - 50 * (i + 1), 20))
        
    # time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
    time_left = max(0, 30 - elapsed_time)
    
     # Update animation frame
    frame_counter += 1
    if frame_counter >= frame_delay:
        frame_counter = 0
        current_frame = (current_frame + 1) % len(player_img)  # Loop through frames
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_lane > 0:
            player_lane -= 1
            pygame.time.wait(150)
        elif keys[pygame.K_RIGHT] and player_lane < 2:
            player_lane += 1
            pygame.time.wait(150)
    
    # car movement
    if random.randint(1, 90) == 1:  # how often cars spawn
        lane = random.randint(0, 2)
        car_x = lanes[lane] - 50
        car_rect = pygame.Rect(car_x, -140, 100, 140)
        car_image = random.choice(car_images)
        cars.append({"rect": car_rect, "image": car_image})
        
    for car in cars:
        car["rect"].y += car_speed  # Move the car
        screen.blit(car["image"], car["rect"])  # Draw the car
        player.x = lanes[player_lane] - 50
        
        # debugging hitbox
        car_hitbox = car["rect"].inflate(-20, -20)
        pygame.draw.rect(screen, (255, 0, 0), car_hitbox, 2) # draw car hitbox
        player_hitbox = player.inflate(-40, -40)
        pygame.draw.rect(screen, (0, 255, 0), player_hitbox, 2)  # draw player hitbox
        
        # collision!!
        if player.colliderect(car["rect"]):
            hearts -= 1
            cars.remove(car)
            if hearts <= 0:
                running = False
                break
            
        


            
    # Update the display
    pygame.display.update()
    delay.tick(60)  # Limit FPS to 60





