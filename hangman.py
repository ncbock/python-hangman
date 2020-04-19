import pygame
from string import ascii_uppercase
from getpass import getpass

#RGB colors for drawing
white = (255, 255, 255)
black = (0,0,0)
green = (0,255, 0)

clock = pygame.time.Clock()

def main():
    #word = getWord()
    pygame.init()

    win = pygame.display.set_mode((750, 525))

    pygame.display.set_caption("Hang Man")

    #Track the count of wrong guesses the player has made and to start the game.
    count = 0

    lettersGuessed = []
    
    word = ""

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.MOUSEBUTTONDOWN and count < 1:
                pos = pygame.mouse.get_pos()
                if pos[0]>= 500 and pos[0]<= 625:
                    if pos[1]>= 150 and pos[1]<=190:
                        print("1 Player mode Selected")
                        count += 1
                    elif pos[1]>=200 and pos[1]<= 240:
                        print("2 Player mode Selected")
                        count += 1
                        word = getWord()
            if e.type == pygame.KEYDOWN:
                if chr(e.key).upper() not in lettersGuessed and count >0:
                    lettersGuessed.append(chr(e.key).upper())
                    if chr(e.key).upper() not in word.upper():
                        count += 1
        
        # All drawing to occur after win.fill or else it will be erased.
        win.fill(white)
        if count >0:
            displayWord(win, word, lettersGuessed)
        header = pygame.font.SysFont("arial", 65)
        title = header.render("Hangman",1,black)
        win.blit(title,(240,10))
        pygame.draw.line(win,black,(0,450),(750,450),)
        drawHang(win, count)
        drawMan(win, count)
        guessedLetters(win, lettersGuessed)
        numPlayerSelect(win, count)
        pygame.display.update()
        clock.tick(60)

def numPlayerSelect(win, count):
    #1 Player
    myfont = pygame.font.SysFont("monosapce",35)
    if count == 0:
        color = black
    else: 
        color = white
    pygame.draw.rect(win,color,(500,150,125,40),2)
    p1 = myfont.render("1 Player",1,color)
    win.blit(p1,(515,160))
    #2 Players
    pygame.draw.rect(win,color,(500,200,125,40),2)
    p2 = myfont.render("2 Player",1,color)
    win.blit(p2,(515,210))


def drawHang(win, count):
    if count == 0:
        color = green
    else:
        color = black
    # Draw base of hanger
    pygame.draw.line(win,color,(100,350),(300,350),12)
    # Draw Vertical
    pygame.draw.line(win,color,(200,100),(200,350),12)
    # Draw Horizontal
    pygame.draw.line(win,color,(195,100),(350,100),12)
  
def drawMan(win, count):
    if count == 0:
        color = green
    else:
        color = black

     # Draw Rope
    pygame.draw.line(win,color, (340,100),(340,150), 2)
    # Draw the head
    pygame.draw.circle(win,color,(340,170),20)
    # Draw the body
    pygame.draw.line(win,color, (340,190),(340,265), 2)
    # Draw Left Leg
    pygame.draw.line(win,color, (340,265),(305,300), 2)
    # Draw Right Leg
    pygame.draw.line(win,color, (340,265),(375,300), 2)
    #Draw Left Arm
    pygame.draw.line(win,color, (340,215),(305,250), 2)
    # Draw Right Arm
    pygame.draw.line(win,color, (340,215),(375,250), 2)

def displayWord(screen, word, guesses):
    font = pygame.font.SysFont("Arial", 20)
    disp = []
    for abc in word:
        if abc.upper() in guesses:
            disp.append(" "+abc.upper()+" ")
        else:
            disp.append("__ ")
    lenWord = len(disp)
    widthRect = (27.5 * lenWord) + 15
    rectStart = 375- (widthRect/2)
    pygame.draw.rect(screen, black, (rectStart,400,widthRect,40),2)
    display = font.render("".join(disp),1, black)
    screen.blit(display,(rectStart + 15,412))

def getWord():
    word = getpass("Enter your Word: ")
    return word

def guessedLetters(win, p):
    guessFont= pygame.font.SysFont("arial",25)
    x_start = 15
    y = 475
    letters = ascii_uppercase
    for abc in letters:
        text = guessFont.render(abc,1,black)
        win.blit(text,(x_start,y))
        if abc in p:
            pygame.draw.line(win,black,(x_start,487),(x_start+20,487),3)
        x_start += 28

if __name__ == '__main__':
    main()
    pygame.quit()