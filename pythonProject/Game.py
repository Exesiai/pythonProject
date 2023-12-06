import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
Width = 720
Height = 1280
screen_rect = screen.get_rect()
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/smiley-modified.png")
        self.rect = self.image.get_rect()

        self.x = 500
        self.y = 500

        self.hitbox = (self.x, self.y, 32, 32)

    def update(self):
        # Update the character's position

        self.x += 1
        self.y += 1

    def draw(self, screen):
        # Draw the character to the screen

        screen.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, 32, 32)
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


class Character2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/smiley-modified1.png")
        self.rect = self.image.get_rect()

        self.x = 750
        self.y = 500

        self.hitbox = (self.x, self.y, 32, 32)


    def update(self):
        # Update the character's position

        self.x += 1
        self.y += 1

    def draw(self, screen):
        # Draw the character to the screen

        screen.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, 32, 32)
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    #def died



# Create a Sprite group
sprites = pygame.sprite.Group()

# Create a character object
character = Character()
character.rect = pygame.Rect(character.x, character.y, 50, 50)
character2 = Character2()
character.rect = pygame.Rect(character.x, character.y, 50, 50)
# Add the character to the Sprite group
sprites.add(character)
sprites.add(character2)

#countdown timer
counter, text = 10,'10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT,1000)
font = pygame.font.SysFont('Arial',30)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.K_KP_ENTER:
            counter -= 1
        if event.type == pygame.QUIT:
            running = False

    #background loading
    bGimage = pygame.image.load("assets/bg1.png")
    background_image = pygame.transform.scale(bGimage, screen.get_size())
    screen.blit(background_image, (0, 0))

    screen.blit(font.render(text, True, (0, 0, 0)), (1160, 630))

    #background music
    # mixer.music.load('song.mp3')
    # mixer.music.set_volume(0.2)
    # mixer.music.play()


    #movement for the player 1 sprite with boundaries
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        MovedY = character.y - 300 * dt
        if MovedY > screen_rect.top:
            character.y = MovedY
    if keys[pygame.K_s]:
        MovedY = character.y + 300 * dt
        if MovedY <= screen_rect.bottom-173:
            character.y = MovedY
    if keys[pygame.K_a]:
        MovedX = character.x - 300 * dt
        if MovedX > screen_rect.left-3:
            character.x = MovedX
    if keys[pygame.K_d]:
        MovedX = character.x + 300 * dt
        if MovedX < screen_rect.right/2-25:
            character.x = MovedX
    #movement for the player 2 sprite along with boundaries
    if keys[pygame.K_UP]:
        MovedY2 = character2.y - 300 * dt
        if MovedY2 > 1280:
            MovedY2 = 1280
        if MovedY2 > screen_rect.top:
            character2.y = MovedY2
    if keys[pygame.K_DOWN]:
        MovedY2 = character2.y + 300 * dt
        if MovedY2 > 720 - 172:
            MovedY2 = 720 - 172
        if MovedY2 <= screen_rect.bottom - 172:
            character2.y = MovedY2
    if keys[pygame.K_LEFT]:
        MovedX2 = character2.x - 300 * dt
        if MovedX2 < 1280/2:
            MovedX2 = 1280/2
        if MovedX2 > screen_rect.right/2:
            character2.x = MovedX2
    if keys[pygame.K_RIGHT]:
        MovedX2 = character2.x + 300 * dt
        if MovedX2 > 1280:
            MovedX2 = 1280
        if MovedX2 < screen_rect.right -27:
            character2.x = MovedX2



    #draw in the characters
    character.draw(screen)
    character2.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
