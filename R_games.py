import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CHILDE INVASIONNNN")

# Load background image
background = pygame.image.load("c:/Users/anand/OneDrive/Pictures/childe namecard.jpg")

# Clock for controlling FPS
clock = pygame.time.Clock()

# PLLAAAAAAAYYYYYYYEEEEEEEEERRRRR CLLLLASSSSSSSSS
class Player(object):
    def __init__(self):
        self.img = pygame.image.load("c:/Users/anand/OneDrive/Pictures/childe png.png")
        self.img = pygame.transform.scale(self.img, (200, 200))
        self.x = 370
        self.y = 480
        self.x_change = 0
        self.y_change = 0
        self.lives = 3

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# AALIEEEEEEEEEEEEENNNNNNN CLASSSSSSSSSSSSSS
class Enemy(object):
     def __init__(self, x, y):
         self.img = pygame.image.load("c:/Users/anand/OneDrive/Pictures/cry childe.PNG")
         self.img = pygame.transform.scale(self.img, (70, 70))  # Resize to 50x50 pixels
         self.x = x
         self.y = y
         self.x_change = random.choice([-3, 3])  # Random horizontal speed (left or right)
         self.y_change = 0.5  # Vertical speed

# BULLLLLLLLLLLLLEEEEEEEEETTTTT CLASSSSSSSSSS
class Bullet:
    def __init__(self, x, y):
        self.img = pygame.image.load("c:/Users/anand/OneDrive/Pictures/Primos.webp")
        self.img = pygame.transform.scale(self.img, (40, 40))  # Resize bullet to 20x20 pixels
        self.x = x
        self.y = y
        self.y_change = -10  # Speed of the bullet
        self.state = "ready"  # "ready" means the bullet is not visible, "fire" means it is moving

    def fire(self, x, y):
        self.state = "fire"
        self.x = x
        self.y = y

    def move(self):
        if self.state == "fire":
            self.y += self.y_change
            if self.y < 0:
                self.state = "ready"

    def draw(self):
        if self.state == "fire":
            screen.blit(self.img, (self.x, self.y))
 
# -----------------------------------------------------------           
class enemy_bullet:
    def __init__(self, x, y):
        self.img = pygame.image.load("c:/Users/anand/OneDrive/Pictures/Primos.webp")
        self.img = pygame.transform.scale(self.img, (40, 40))  # Resize bullet to 20x20 pixels
        self.x = x
        self.y = y
        self.y_change = -10  # Speed of the bullet
        
    def fire (self, x, y):
        self.state = "fire"
        self.x = x
        self.y = y
# ---------------------------------------------------------------   
    

# Function to display scores
def show_scores(scores):
    font = pygame.font.Font(None, 36)  # Create a font object
    scores_text = font.render(f"Score: {scores}", True, (255, 255, 255))  # Render the text
    screen.blit(scores_text, (10, 10))  # Draw the text at the top-left corner

# Function to display timer
def show_timer(time_left):
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time: {time_left}s", True, (255, 255, 255))
    screen.blit(timer_text, (650, 10))  # Draw the timer at the top-right corner

# SCORES N TIMER VARIABLES
scores = 0
max_scores = 20  # Designated score to win
time_left = 30  # Time in seconds
start_ticks = pygame.time.get_ticks()  # Start time

# collision detection function
def is_collision(a, b):
    distance = ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
    if (distance < 20):
        return True
    else:
        return False

# -----POSITIONSSS SPRITES-----
player = Player() # player
enemies = [Enemy(random.randint(0, 735), random.randint(50, 150)) for _ in range(6)] # Enemenies
bullet = Bullet(player.x, player.y) # Clone bullets bullet

# Main game loop
running = True
while running:
    # Draw the background
    screen.blit(background, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -5
            if event.key == pygame.K_RIGHT:
                player.x_change = 5
            if event.key == pygame.K_UP:
                player.y_change = -5
            if event.key == pygame.K_DOWN:
                player.y_change = 5
            if event.key == pygame.K_SPACE and bullet.state == "ready":
                bullet.fire(player.x + player.img.get_width() // 2 - bullet.img.get_width() // 2, player.y)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.x_change = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                player.y_change = 0

    # Update timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
    time_left = max(0, 30 - elapsed_time)

    # Check for game over or win condition
    if time_left == 0 and scores < max_scores:
        print("Game Over! You ran out of time.")
        running = False
    elif scores >= max_scores:
        print("You Win! You reached the designated score.")
        running = False

    # Update and draw each enemy
    for enemy in enemies:
        enemy.x += enemy.x_change
        if enemy.x <= 0 or enemy.x >= 735: # Reverse direction if enemy hits screen bounds
            enemy.x_change *= -1
        screen.blit(enemy.img, (enemy.x, enemy.y))
        
        # Check for collision
        if is_collision(bullet, enemy):
            bullet.state = "ready"  # Reset the bullet
            bullet.y = player.y  # Move bullet back to player
            enemy.x = random.randint(0, 735)  # Reset enemy to a new random position
            enemy.y = random.randint(50, 150)
            scores += 1  # Increment score

    # Update player position
    player.x += player.x_change
    player.y += player.y_change
    # Ensure the player stays within screen bounds
    player.x = max(0, min(player.x, 800 - player.img.get_width()))
    player.y = max(0, min(player.y, 600 - player.img.get_height()))
    # Draw the player
    player.draw()
    # Draw the scores and timer on the screen
    show_scores(scores)
    show_timer(time_left)
    
    # Update and draw the bullet
    bullet.move()
    bullet.draw()

    # Update the display
    pygame.display.update()
    # Limit FPS to 60
    clock.tick(60)
    
pygame.quit()