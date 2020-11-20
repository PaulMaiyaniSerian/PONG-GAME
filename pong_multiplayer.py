# pong by paul serian maiyani
import pygame
from random import randrange, randint
import sys

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0, 255,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
OLIVE = (128,128,0)
BLUE = (0,0,255)
MAROON = (128,0,0)
OVER =(255,12, 12)

colors = [WHITE, GREEN, RED, YELLOW, OLIVE, BLUE, MAROON]
# velocities
BALL_VEL_X = 15
BALL_VEL_Y = 15
PADDLE_VEL = 7

pygame.init()

SCREEN = (1000,600)
FULL_SCREEN = (1280, 1024)



# main window
MAIN_WINDOW = pygame.display.set_mode(SCREEN)


# title
pygame.display.set_caption("PAUL'S PONG GAME")

# is running
running = True

start_time = None
# balance framerate
clock = pygame.time.Clock()

# snow background for game
snow_cord_list = []


for i in range(100):
    x = randrange(0,SCREEN[0])
    y = randrange(0,SCREEN[1])
    snow_cord_list.append([x,y])


def draw_snow():
     for i in range(len(snow_cord_list)-1):
                pygame.draw.circle(MAIN_WINDOW, colors[randint(0,5)], snow_cord_list[i], 2)

                snow_cord_list[i][1] += 1

                if snow_cord_list[i][1] > SCREEN[1]:
                    snow_cord_list[i][1] = 1

# paddles
class Paddle:
    def __init__(self, parent, color, cord_x, cord_y,velocity=0, pos="right"):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.velocity = velocity
        self.color = color
        self.parent = parent
        self.pos = pos

    def create_paddle(self, length, width):
        self.paddle = pygame.draw.rect(self.parent, self.color, [self.cord_x, self.cord_y, length, width], 0)

    def reset(self):
        if self.pos == "right":
            self.cord_x = 970
            self.cord_y = 200
        if self.pos == "left":   
            self.cord_x = 10
            self.cord_y = 200



    def move(self, stop=False):
        self.stop = stop

        if not stop:
            if self.cord_y > 0:
                self.cord_y += self.velocity
            else:
                self.cord_y = 1
            if self.cord_y < 450:
                self.cord_y += self.velocity
            else:
                self.cord_y = 451
        else:
            pass
        
        

        
    

paddle_left = Paddle(MAIN_WINDOW, RED,cord_x=10 ,cord_y=200, pos="left")
paddle_right = Paddle(MAIN_WINDOW, BLUE,cord_x=970 ,cord_y=200, pos="right")

# wall_sound = "link.wav"
# click_sound = pygame.mixer.Sound(wall_sound)

miss_m = "teleport.wav"
miss_sound = pygame.mixer.Sound(miss_m)


paddle_m = "itemback.wav"
paddle_sound = pygame.mixer.Sound(paddle_m)

background_m = "back"
# back_music = pygame.mixer.Sound(background_m)

end_m = "laugh.ogg"
endmusic = pygame.mixer.Sound(end_m)

start_m = "witch.ogg"
start_music = pygame.mixer.Sound(start_m)

# ball
class Ball():
    def __init__(self, parent, color, cord_x, cord_y, velocity_x, velocity_y):
        self.parent = parent
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

        

    def create_ball(self, radius):
        self.radius = radius
        self.ball = pygame.draw.circle(self.parent, self.color,[self.cord_x, self.cord_y], radius)
    

    def reset(self):
        self.cord_x = 480
        self.cord_y = 280

    def move(self, collided=False, stop=False):
        self.stop = stop
        if not stop:
            self.cord_x += self.velocity_x
            self.cord_y += self.velocity_y

            if self.cord_y > 550:
                # click_sound.play()
                self.velocity_y *= -1
                
            if self.cord_y < 20:
                # click_sound.play()
                self.velocity_y *= -1


        

            if collided:
                if self.cord_x > 950:
                    paddle_sound.play()
                    self.velocity_x *= -1
                if self.cord_x < 50:
                    paddle_sound.play()
                    self.velocity_x *= -1

            # check if ball is out of bound
            
        else:
            pass
        



ball = Ball(MAIN_WINDOW, RED, 480, 280, BALL_VEL_X, BALL_VEL_Y)
ball2 = Ball(MAIN_WINDOW, GREEN, 480, 280,BALL_VEL_X, BALL_VEL_Y)

#draw text
font4 = pygame.font.SysFont('Calibri', 70, True, False)
start_text1 = font4.render("PONG by PAUL .SB", True, RED)

font50 = pygame.font.SysFont('Calibri', 50, True, False)

font5 = pygame.font.SysFont('Calibri', 30, True, False)
start_text2 = font5.render("this is my own custom version of pong with animations.. enjoy", True, GREEN)

start_text3 = font5.render("There are no media files or sprites of any kind just python : )", True, GREEN)

# splash screen 2

start_text4 = font4.render("WRITTEN BY PAUL SERIAN..", True, RED)
start_space = font5.render("PRESS SPACE |_________|", True, RED)

start_text5 = font5.render("this software has been written in a day up to its current state : )", True, GREEN)

#draw text
font = pygame.font.SysFont('Calibri', 100, True, False)
game_over_text = font.render("GAME OVER!!!", True, OVER)

# new game text
font1 = pygame.font.SysFont('Calibri', 30, True, False)
new_game_text = font1.render("New Game:  press Enter", True, GREEN)



# press_q to quit
font2 = pygame.font.SysFont('Calibri', 30, True, False)
quit_text = font2.render("EXIT:  press Q", True, GREEN)




# score text:
font3 = pygame.font.SysFont('Calibri', 30, True, False)

left_score = 0
right_score = 0


def draw_text(message, color):
    font3 = pygame.font.SysFont('Calibri', 50, True, False)
    paused_text = font3.render(message, True, color)
    MAIN_WINDOW.blit(paused_text, [400, 100])


paused = False

game_over = False

green = True

screen1 = True

screen2 = False

            
winner = ""

playing = True

# sounds

def get_tick():
    start_time = pygame.time.get_ticks()
    return (start_time / 60)

pygame.mouse.set_visible(False)
# update functionality for play
def play():
    global running, paused, BALL_VEL_X, BALL_VEL_Y, playing, game_over, green, screen1, screen2, left_score, winner, right_score

    while running:

        for event in pygame.event.get():
            # quit button
            if event.type == pygame.QUIT:
                sys.exit()
        
            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle_left.velocity = -PADDLE_VEL
                    # increase ball velocity
                   

                elif event.key == pygame.K_s:
                    paddle_left.velocity = PADDLE_VEL
                      # increase ball velocity
                   

                elif event.key == pygame.K_ESCAPE:
                    if paused:
                        start_music.play()
                        paused = False
                    else:
                        paused = True
                elif event.key == pygame.K_RETURN:
                    if paused:
                        start_music.play()
                        paused = False
                    if not screen2 and screen1:
                        screen2 = True
                        screen1 = False
                        start_music.play()

                    
                    if game_over:
                        paddle_left.reset()
                        paddle_right.reset()
                        start_music.play()
                        ball.reset()
                        ball2.reset()
                        game_over = False
                        paused = True
               
                    
                elif event.key == pygame.K_SPACE:
                    if paused:
                        start_music.play()
                        paused = False
                    if not screen1 and screen2:
                        screen2 = False
                        paused = True
                        start_music.play()
                     

                elif event.key == pygame.K_q:
                     sys.exit()
                    #  else:
                    #     paused = True
                    # sys.exit()
                    

                    


                # paddle right
                if event.key == pygame.K_UP:
                    paddle_right.velocity = -PADDLE_VEL
                elif event.key == pygame.K_DOWN:
                    paddle_right.velocity = PADDLE_VEL


            # User released a key 
            # paddle left
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_left.velocity = 0
            # paddle right
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_right.velocity = 0
        
        # background
        MAIN_WINDOW.fill(BLACK)

       
# if start mot true:
        if screen1 and not screen2:
            MAIN_WINDOW.fill(BLACK)

            # snowing
            draw_snow()
            MAIN_WINDOW.blit(start_text1, [250, 100])
            MAIN_WINDOW.blit(start_text2,[70, 200])
            MAIN_WINDOW.blit(start_text3,[70, 300])
            MAIN_WINDOW.blit(new_game_text,[350, 400])
            MAIN_WINDOW.blit(quit_text,[350, 500])
            
            

       
        if screen2 and not screen1:
            MAIN_WINDOW.fill(BLACK)
            draw_snow()
            MAIN_WINDOW.blit(start_text4, [100, 100])
            MAIN_WINDOW.blit(start_text5,[70, 200])
            MAIN_WINDOW.blit(start_space,[350, 300])
            MAIN_WINDOW.blit(quit_text,[400, 500])
            
            

# check if game is paused
        if not paused and not screen1 and not screen2:
            # logic goes here
            

            left_score_text = font3.render("Score " + str(left_score), True, RED)
            right_score_text = font3.render("Score " + str(right_score), True, BLUE)
            # snow
            draw_snow()
            # draw scores
            MAIN_WINDOW.blit(left_score_text,[100, 20])
            MAIN_WINDOW.blit(right_score_text,[800, 20])
            


            # paddles
            paddle_left.create_paddle(20,150)
            paddle_left.move()

            paddle_right.create_paddle(20, 150)
            paddle_right.move()

            # update speed
          

            # move ball
            ball.create_ball(radius=30)
            ball2.create_ball(radius=20)

            ball.move()
            ball2.move()

            

        

            # collision
            if ball.ball.colliderect(paddle_left.paddle):
                ball.move(True)
                ball2.move(True)
                

            if ball.ball.colliderect(paddle_right.paddle):
                ball.move(True)
                ball2.move(True)

            # endgame when ball goes away
            if ball.cord_x > 980:
                miss_sound.play()
                left_score += 1
                ball.reset()
                ball2.reset()
                
                if left_score == 5:
                    game_over = True
                    left_score = 0
                    winner = "RED"
                

            if ball.cord_x < 20:
                miss_sound.play()
                right_score += 1
                ball.reset()
                ball2.reset()
                
                if right_score == 5:
                    game_over = True
                    right_score = 0
                    winner = "BLUE"
                
                
# condition if paused
        if paused:
            # snowing 
            draw_snow()
            # paddles
            
            paddle_left.create_paddle(20,150)
            paddle_left.move(stop=True)

            paddle_right.create_paddle(20, 150)
            paddle_right.move(stop=True)

            ball.create_ball(radius=30)
            ball2.create_ball(radius=20)
            ball.move(stop=True)
            ball2.move(stop=True)


            draw_text("PAUSED", RED)
            
                # green = False

                
            # else:
            #     MAIN_WINDOW.blit(paused_text2, [320, 200])
            #     green = True
# custom pause


# condition for game over
        if game_over:
            
            if playing:
                endmusic.play()
                playing = False

            ball.reset()
            ball2.reset()
            MAIN_WINDOW.fill(BLACK)
            if winner == "RED":
                win = font50.render(winner + " Won!", True, RED)
            else:
                # 
                win = font50.render(winner + " Won!", True, BLUE)

            # snowing
            draw_snow()

           


            MAIN_WINDOW.blit(game_over_text, [250, 80])
            MAIN_WINDOW.blit(win, [350, 250])
            MAIN_WINDOW.blit(new_game_text,[350, 400])
            MAIN_WINDOW.blit(quit_text,[400, 500])
            
            right_score = 0
            left_score = 0

        # update screen
        pygame.display.flip()

        clock.tick(60)


play()


