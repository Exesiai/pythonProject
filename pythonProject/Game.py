import pygame
import time
import math


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

#start time
current_time = 0
#overall font
font = pygame.font.SysFont('Arial',30)

#user imput box variables
user_text = ''
input_rect = pygame.Rect(72,616,200,61)

active_color = pygame.Color(1,1,1)
color_passive = pygame.Color(100,100,100)
color = color_passive

active = False

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
while running:

    #background loading
    bGimage = pygame.image.load("assets/bg1.png")
    background_image = pygame.transform.scale(bGimage, screen.get_size())
    screen.blit(background_image, (0, 0))

    #draw in the characters
    character.draw(screen)
    character2.draw(screen)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #changing the color of input text box when clicked on
        if current_time > 10000:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

        #deleting the most recent input after backspace is pushed
        #shooting the player input code of a function
        #adding the player input to a string
        if current_time > 10000:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]

                #use space bar to shoot a function
                elif event.key == pygame.K_SPACE:
                    #player 1
                    if ((((current_time / 1000) - 10) // 60) % 2) == 0:
                        x = 0
                        while x < 1280:
                            x += 1
                            a = user_text
                            a += "+"
                            a += str(character.y)
                            pygame.draw.circle(screen, (0,128,0), [character.x + x + 16, eval(a)+16], 1,1)
                            circle_rect = pygame.Rect(character.x+x+16,eval(a)+16,1,1)
                            if circle_rect.colliderect(character2.hitbox):
                                pygame.quit()

                    #player 2
                    elif ((((current_time / 1000) - 10) // 60) % 2) == 1:
                        x = 0
                        while x > -1280:
                            x -= 1
                            c = user_text
                            c += "+"
                            c += str(character2.y)
                            pygame.draw.circle(screen, (0,128,0), [character2.x + x + 16, eval(c)+16], 1,1)
                            circle_rect1 = pygame.Rect(character.x+x+16,eval(c)+16,1,1)
                            if circle_rect1.colliderect(character.hitbox):
                                pygame.quit()


                else:
                    user_text += event.unicode


    #changing color of input box
    if active:
        color = active_color
    else:
        color = color_passive

    #creating a variable for time
    current_time = pygame.time.get_ticks()

    #input text box for functions
    pygame.draw.rect(screen,color,input_rect)
    text_surface = font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)

    #timer text display for the first ten seconds
    if current_time < 10000:
        counter, text = current_time / 1000, str(int(current_time / 1000)).rjust(3)
        screen.blit(font.render(text, True, (0, 0, 0)), (1100, 630))

    # timer text display after ten seconds reset
    if current_time > 10000:
        counter, text = current_time / 1000, str(int(current_time / 1000 - 10)).rjust(3)
        screen.blit(font.render(text, True, (0, 0, 0)), (1100, 630))



    #movement for the player 1 sprite with boundaries
    keys = pygame.key.get_pressed()
    # if statement to lock player position after 10 seconds
    if current_time/1000 < 10:
        if keys[pygame.K_w]:
            MovedY = character.y - 300 * dt
            if MovedY > screen_rect.top:
                character.y = MovedY
        if keys[pygame.K_s]:
            MovedY = character.y + 300 * dt
            if MovedY <= screen_rect.bottom - 173:
                character.y = MovedY
        if keys[pygame.K_a]:
            MovedX = character.x - 300 * dt
            if MovedX > screen_rect.left - 3:
                character.x = MovedX
        if keys[pygame.K_d]:
            MovedX = character.x + 300 * dt
            if MovedX < screen_rect.right / 2 - 25:
                character.x = MovedX
        # movement for the player 2 sprite along with boundaries
        if keys[pygame.K_UP]:
            MovedY2 = character2.y - 300 * dt
            if MovedY2 > screen_rect.top:
                character2.y = MovedY2
        if keys[pygame.K_DOWN]:
            MovedY2 = character2.y + 300 * dt
            if MovedY2 <= screen_rect.bottom - 172:
                character2.y = MovedY2
        if keys[pygame.K_LEFT]:
            MovedX2 = character2.x - 300 * dt
            if MovedX2 > screen_rect.right / 2:
                character2.x = MovedX2
        if keys[pygame.K_RIGHT]:
            MovedX2 = character2.x + 300 * dt
            if MovedX2 < screen_rect.right - 27:
                character2.x = MovedX2


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()
