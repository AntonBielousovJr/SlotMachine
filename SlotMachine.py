import pygame, sys
import random
import time
white = (255, 255, 255)

pygame.init()



# Create the window
window_size = (450, 600)
screen = pygame.display.set_mode(window_size)
screen.fill(white)
pygame.display.set_caption("3 by 3 Slot Machine")

# Load images
cherry = pygame.image.load('cherry.png')
cherry = pygame.transform.scale(cherry, (150,150))
cherryrect = cherry.get_rect()

lemon = pygame.image.load('lemon.png')
lemon = pygame.transform.scale(lemon, (150,150))
lemonrect = lemon.get_rect()

seven = pygame.image.load('seven.png')
seven = pygame.transform.scale(seven, (150,150))
sevenrect = seven.get_rect()

balance = 500

red = (255,0,0)

reward = 0

A1symbol = seven
A2symbol = cherry
A3symbol = seven
B1symbol = cherry
B2symbol = seven
B3symbol = cherry
C1symbol = seven
C2symbol = cherry
C3symbol = seven
    

spinonce = 0
    
    
def labels():
    
    pygame.draw.rect(screen, white, (0, 450, 450, 150))
    
    bet_text = font.render("Balance: " + str(balance), True, (0, 0, 0))
    screen.blit(bet_text, (10, 460))


    balance_text = font.render("Bet: " + str(bet_size), True, (0, 0, 0))
    screen.blit(balance_text, (350, 460))

    pygame.display.update(0, 450, 450, 200)

def spin():
    global reward_text
    global balance
    global reward

    global A1symbol 
    global A2symbol 
    global A3symbol 
    global B1symbol 
    global B2symbol 
    global B3symbol 
    global C1symbol 
    global C2symbol 
    global C3symbol 



    screen.fill(white)
    labels()

    #A1
    rand = random.randint(1, 3)
    if rand == 1:
        A1symbol = cherry
    elif rand == 2:
        A1symbol = lemon
    else:
        A1symbol = seven

    #B1
    rand = random.randint(1, 3)
    if rand == 1:
        B1symbol = cherry
    elif rand == 2:
        B1symbol = lemon
    else:
        B1symbol = seven

    #C1
    rand = random.randint(1, 3)
    if rand == 1:
        C1symbol = cherry
    elif rand == 2:
        C1symbol = lemon
    else:
        C1symbol = seven

    #A2
    rand = random.randint(1, 3)
    if rand == 1:
        A2symbol = cherry
    elif rand == 2:
        A2symbol = lemon
    else:
        A2symbol = seven

    #B2
    rand = random.randint(1, 3)
    if rand == 1:
        B2symbol = cherry
    elif rand == 2:
        B2symbol = lemon
    else:
        B2symbol = seven

    #C2
    rand = random.randint(1, 3)
    if rand == 1:
        C2symbol = cherry
    elif rand == 2:
        C2symbol = lemon 
        C2symbol = seven

    #A3
    rand = random.randint(1, 3)
    if rand == 1:
        A3symbol = cherry
    elif rand == 2:
        A3symbol = lemon
    else:
        A3symbol = seven

    #B3
    rand = random.randint(1, 3)
    if rand == 1:
        B3symbol = cherry
    elif rand == 2:
        B3symbol = lemon
    else:
        B3symbol = seven

    #C3
    rand = random.randint(1, 3)
    if rand == 1:
        C3symbol = cherry
    elif rand == 2:
        C3symbol = lemon
    else:
        C3symbol = seven  

    

    


    


    #draw symbols
    screen.blit(A1symbol, (0, 300))
    pygame.display.update() 
    time.sleep(0.05)
    screen.blit(A2symbol, (0, 150))
    pygame.display.update()
    time.sleep(0.05)
    screen.blit(A3symbol, (0, 0))
    pygame.display.update()
    time.sleep(0.2) 

    screen.blit(B1symbol, (150, 300)) 
    pygame.display.update()
    time.sleep(0.05)
    screen.blit(B2symbol, (150, 150))
    pygame.display.update()
    time.sleep(0.05)
    screen.blit(B3symbol, (150, 0))
    pygame.display.update()
    time.sleep(0.2)

    screen.blit(C1symbol, (300, 300)) 
    pygame.display.update()
    time.sleep(0.05)
    screen.blit(C2symbol, (300, 150))
    pygame.display.update()
    time.sleep(0.05)
    screen.blit(C3symbol, (300, 0))
    pygame.display.update()
    time.sleep(0.5)

    if A1symbol == B1symbol == C1symbol:
        if A1symbol == lemon:
            reward = wager * 1
        
        elif A1symbol == cherry:
            reward = wager * 2
        elif A1symbol == seven:
            reward = wager * 5
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 375, 430, 16), 8, 8)
    
    
    if A2symbol == B2symbol == C2symbol:
        if A2symbol == lemon:
            reward = wager * 1 + reward
        elif A2symbol == cherry:
            reward = wager * 2 + reward
        elif A2symbol == seven:
            reward = wager * 5 + reward
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 225, 430, 16), 8, 8)
    
    if A3symbol == B3symbol == C3symbol:
        if A3symbol == lemon:
            reward = wager * 1 +reward
        elif A3symbol == cherry:
            reward = wager * 2 + reward
        elif A3symbol == seven:
            reward = wager * 5 + reward
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 75, 430, 16), 8, 8)
    
    balance = balance + reward

    pygame.display.update()

    if reward > 0:
        print(reward)
        reward_text = font.render("You Won: " + str(reward), True, (0, 0, 0))
        labels() 
        screen.blit(reward_text, (155, 575))
        pygame.display.update()
        time.sleep(1)
        reward = 0
    



bet_size = 1




# Set the font
font = pygame.font.Font(None, 36)



# fps
FPS = 60

# Set the spinning flag
spinning = True
spinning = not spinning

# Set the clock
clock = pygame.time.Clock()

labels()

# Main loop
while True:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spinning = not spinning
            elif event.key == pygame.K_UP:
                if not spinning:
                    bet_size += 1
                    labels()
                    
            elif event.key == pygame.K_DOWN:
                if not spinning:
                    bet_size = max(1, bet_size - 1)
                    labels()
            elif event.key == pygame.K_RIGHT:
                if not spinning:
                    bet_size = max(1, bet_size + 10)
                    labels()

            elif event.key == pygame.K_LEFT:
                if not spinning:
                    bet_size = max(1, bet_size - 10)
                    labels()
            elif event.key == pygame.K_m:
                if not spinning:
                    bet_size = balance
                    labels()
            elif event.key -- pygame.K_RETURN:
                if spinonce == 0:   
                    if not spinning:
                    
                        spinonce = 1



    # Spin the reels
    if spinning:
        if (balance - bet_size >= 0):

            balance = balance - bet_size
            wager = bet_size
            spin()
        
            time.sleep(0.5)
            
        else: 
            print("balance is too low")
            balancelow_text = font.render("Balance is too low: ", True, (0, 0, 0))
            labels() 
            screen.blit(balancelow_text, (130, 225))
            pygame.display.update()
            spinning = not spinning


    if spinonce == 1:
        if (balance - bet_size >= 0):

            balance = balance - bet_size
            wager = bet_size
            spin()
        
            
            spinonce = 0
            
        else: 
            print("balance is too low")
            balancelow_text = font.render("Balance is too low: ", True, (0, 0, 0))
            labels() 
            screen.blit(balancelow_text, (130, 225))
            pygame.display.update()
        
    


    # Update the display
    pygame.display.update()


    clock.tick(60)
