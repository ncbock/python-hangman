import pygame

#RGB colors for drawing
white = (255, 255, 255)
black = (0,0,0)
green = (0,255, 0)



def main():
    #word = getWord()
    pygame.init()

    win = pygame.display.set_mode((750, 750))

    pygame.display.set_caption("hello")

    clock = pygame.time.Clock()

    #Track the count of wrong guesses the player has made and to start the game.
    count = 0

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.MOUSEBUTTONDOWN and count < 1:
                pos = pygame.mouse.get_pos()
                if pos[0]>= 500 and pos[0]<= 625:
                    if pos[1]>= 150 and pos[1]<=190:
                        print("1 Player mode Selected")
                    elif pos[1]>=200 and pos[1]<= 240:
                        print("2 Player mode Selected")
                count += 1
        win.fill(white)
        pygame.draw.line(win,black,(0,450),(750,450),)
        drawHang(win, count)
        drawMan(win, count)
        # get_spaces = drawWord(win,len(word))
        # displayWord(win, get_spaces, word)
        numPlayerSelect(win, count)
        pygame.display.update()
        clock.tick(60)

def numPlayerSelect(win, count):
    #1 Player
    if count == 0:
        color = black
    else: 
        color = white
    pygame.draw.rect(win,color,(500,150,125,40),2)

    #2 Players
    pygame.draw.rect(win,color,(500,200,125,40),2)


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
    # Draw Rope
    pygame.draw.line(win,color, (340,100),(340,150), 2)

def drawMan(win, count):
    if count == 0:
        color = white
    else:
        color = black
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

# def drawWord(screen, lenWord):
#     start_x =15
#     end_x = 35
#     y = 490
#     locations = []
#     for i in range(lenWord):
#         x_avg = (start_x + end_x)/2
#         locations.append([x_avg,y-10])
#         pygame.draw.line(screen,(0,0,0),(start_x,y),(end_x,y))
#         start_x = end_x + 5
#         end_x = start_x + 20
#     return locations

def displayWord(screen, locations, word):
    font = pygame.font.Font(None, 20)
    for letters in word:
        text = font.render(letters, True, (0,0,0), (255,255,255))
        textRect = text.get_rect()
        for spaces in locations:
            textRect.center = (spaces[0], spaces[1])
        screen.blit(text, textRect)


# def getWord():
#     word = input("What word are we making?\n\n")
#     print(chr(27)+"[2J")
#     return word











if __name__ == '__main__':
    main()
    pygame.quit()