import pygame
from string import ascii_uppercase
from getpass import getpass

#RGB colors for drawing
white = (255, 255, 255)
black = (0,0,0)
green = (0,255, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

def main():
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
                if pos[0] in range(500,626):
                    if pos[1] in range(200,241):
                        count += 1
                        word = getWord()
            if e.type == pygame.MOUSEBUTTONDOWN and playAgain(win, word, count, lettersGuessed):
                pos = pygame.mouse.get_pos()
                if pos[0] in range (550,701):
                    if pos[1] in range (350,391):
                        count = 0
                        lettersGuessed = []
                    if pos[1] >= 400 and pos[1] <= 440:
                        return 
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(20,121):
                    if pos[1] in range(20,59):
                        return
            if e.type == pygame.MOUSEBUTTONDOWN and count >0:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(20,121):
                    if pos[1] in range(68,107):
                        count = 0
            if e.type == pygame.KEYDOWN:
                if chr(e.key).upper() not in lettersGuessed and count >0:
                    lettersGuessed.append(chr(e.key).upper())
                    if chr(e.key).upper() not in word.upper():
                        count += 1
        
        # All drawing to occur after win.fill or else it will be erased.
        win.fill(white)
        if count >0 and count <= 8:
            displayWord(win, word, lettersGuessed, count)
            livesRemaining(win, count)           
        header = pygame.font.SysFont("arial", 65)
        title = header.render("Hangman",1,black)
        win.blit(title,(240,10))
        quitButton(win)
        homeButton(win, count)
        youLoseText(win, count)
        youWinText(win, word, count, lettersGuessed)
        playAgain(win, word, count, lettersGuessed)
        pygame.draw.line(win,black,(0,450),(750,450),)
        drawHang(win, count)
        drawMan(win, count)
        guessedLetters(win, lettersGuessed, count)
        numPlayerSelect(win, count)
        pygame.display.update()
        clock.tick(60)

def numPlayerSelect(win, count):
    myfont = pygame.font.SysFont("arial",30)
    if count == 0:
        pos = pygame.mouse.get_pos()
        color = black
        rectTwoColor = black
        rectTwoSize = 2
        if pos[0] in range(500,626):
            if pos[1] in range(200,241):
                rectTwoColor = green
                rectTwoSize = 4
    else: 
        rectTwoColor = white
        rectTwoSize = 2
        color = white
    pygame.draw.rect(win,rectTwoColor,(500,200,125,40),rectTwoSize)
    p2 = myfont.render("PLAY",1,color)
    win.blit(p2,(527,205))


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
        rope = head = body = leftLeg = rightLeg = leftArm = rightArm = green
    elif count == 1:
        rope = head = body = leftLeg = rightLeg = leftArm = rightArm = white
    elif count == 2:
        rope = black
        head = body = leftLeg = rightLeg = leftArm = rightArm = white
    elif count == 3:
        rope = head = black
        body = leftLeg = rightLeg = leftArm = rightArm = white
    elif count == 4:
        rope = head = body = black
        leftLeg = rightLeg = leftArm = rightArm = white
    elif count == 5:
        rope = head = body = leftLeg = black
        rightLeg = leftArm = rightArm = white
    elif count == 6:
        rope = head = body = leftLeg = rightLeg = black
        leftArm = rightArm = white
    elif count == 7:
        rope = head = body = leftLeg = rightLeg = leftArm = black
        rightArm = white
    else:
        rope = head = body = leftLeg = rightLeg = leftArm = rightArm = black
    # Draw Rope
    pygame.draw.line(win,rope, (340,107),(340,150), 2)
    # Draw the head
    pygame.draw.circle(win,head,(340,170),20)
    # Draw the body
    pygame.draw.line(win,body, (340,190),(340,265), 2)
    # Draw Left Leg
    pygame.draw.line(win,leftLeg, (340,265),(305,300), 2)
    # Draw Right Leg
    pygame.draw.line(win,rightLeg, (340,265),(375,300), 2)
    #Draw Left Arm
    pygame.draw.line(win,leftArm, (340,215),(305,250), 2)
    # Draw Right Arm
    pygame.draw.line(win,rightArm, (340,215),(375,250), 2)

def youLoseText(screen, count):
    if count >= 8:
        font = pygame.font.SysFont("arial", 45)
        text = "YOU LOSE! :("
        display = font.render(text,1,red)
        screen.blit(display, (400,250))
        return True
    return False

def youWinText(screen, word, count, guesses):
    winCount = 0
    if count > 0 and count <8:
        for abc in word.upper():
            if abc in guesses:
                winCount += 1
        if winCount == len(word):
            font = pygame.font.SysFont("arial", 45)
            text = "YOU WIN!!!!"
            display = font.render(text,1,green)
            screen.blit(display, (400,250))
            return True
    return False

def displayWord(screen, word, guesses, count):
    font = pygame.font.SysFont("Arial", 20)
    disp = []
    for abc in word:
        if abc.upper() in guesses:
            disp.append(" "+abc.upper()+" ")
        else:
            disp.append("__ ")
    if youLoseText(screen, count):
        disp = []
        for abc in word:
            disp.append(" "+abc.upper()+" ")
    lenWord = len(disp)
    widthRect = (27.5 * lenWord) + 15
    rectStart = 375- (widthRect/2)
    pygame.draw.rect(screen, black, (rectStart,400,widthRect,40),2)
    display = font.render("".join(disp),1, black)
    screen.blit(display,(rectStart + 15,412))

def getWord():
    word = getpass("Enter your Word: ")
    return word

def guessedLetters(win, p, count):
    guessFont= pygame.font.SysFont("arial",25)
    x_start = 15
    y = 475
    letters = ascii_uppercase
    for abc in letters:
        text = guessFont.render(abc,1,black)
        win.blit(text,(x_start,y))
        if abc in p and count < 8:
            pygame.draw.line(win,black,(x_start,487),(x_start+20,487),3)
        x_start += 28

def livesRemaining(screen, count):
    font = pygame.font.SysFont("arial", 20)
    if count <= 8:
        lives = 8 - count
    else:
        lives = 0
    text = font.render("Lives: %i" %(lives),1,black)
    screen.blit(text, (625,40))
            
def playAgain(screen, word, count, guess):
    myfont = pygame.font.SysFont("arial", 28)
    pos = pygame.mouse.get_pos()
    if youWinText(screen, word, count, guess) or youLoseText(screen,count):
        
        pgColor = quitColor = black
        pgSize = quitSize = 2
        if pos[0] in range(550,701):
            if pos[1] in range(350,391):
                pgColor = green
                pgSize = 4
            if pos[1] in range (400,441):
                quitColor = red
                quitSize = 4
        #Play Again Button
        pygame.draw.rect(screen,pgColor,(550,350,150,40),pgSize)
        playAgain = myfont.render("Play Again",1,black)
        screen.blit(playAgain,(560,355))
        #Quit Button
        pygame.draw.rect(screen,quitColor,(550,400,150,40),quitSize)
        quitGame = myfont.render("QUIT",1,black)
        screen.blit(quitGame,(587,407))
        return True
    return False

def quitButton(screen):
    myfont = pygame.font.SysFont("arial", 35)
    pos = pygame.mouse.get_pos()
    buttonColor = black
    buttonSize = 2

    if pos[0] in range(20,121):
        if pos[1] in range(20,59):
            buttonColor = red
            buttonSize = 4
    
    pygame.draw.rect(screen,buttonColor,(20,20,100,38),buttonSize)
    buttonText=myfont.render("QUIT",1,buttonColor)
    screen.blit(buttonText,(30,20))

def homeButton(screen, count):
    if count >0:
        myfont = pygame.font.SysFont("arial", 30)
        pos = pygame.mouse.get_pos()
        buttonColor = black
        buttonSize = 2

        if pos[0] in range(20,121):
            if pos[1] in range(68,107):
                buttonColor = green
                buttonSize = 4
        
        pygame.draw.rect(screen,buttonColor,(20,68,100,38),buttonSize)
        buttonText=myfont.render("HOME",1,buttonColor)
        screen.blit(buttonText,(25,70))

if __name__ == '__main__':
    main()
    pygame.quit()