import pygame as pg
from wonderwords import RandomWord
import time
from python_spell.checker import SpellChecker


pg.init()

font = pg.font.SysFont(None, 80)
font2 = pg.font.SysFont(None, 40)
img = pg.image.load('Wordle.png')
pg.display.set_icon(img)
word_master = RandomWord()
width = 500
height = 500
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Wordle')


def draw_grid():
    screen.fill((255, 255, 255))
    # Vertical
    pg.draw.rect(screen, (84, 84, 84), pg.Rect(15, 15, 470, 470))
    pg.draw.line(screen, (255, 255, 255), (100, 0), (100, 500), 5)
    pg.draw.line(screen, (255, 255, 255), (200, 0), (200, 500), 5)
    pg.draw.line(screen, (255, 255, 255), (300, 0), (300, 500), 5)
    pg.draw.line(screen, (255, 255, 255), (400, 0), (400, 500), 5)

    #Horizontal 
    pg.draw.line(screen, (255, 255, 255), (0, 100), (500, 100), 5)
    pg.draw.line(screen, (255, 255, 255), (0, 200), (500, 200), 5)
    pg.draw.line(screen, (255, 255, 255), (0, 300), (500, 300), 5)
    pg.draw.line(screen, (255, 255, 255), (0, 400), (500, 400), 5)

def new_word():
    word = word_master.word(word_min_length = 5, word_max_length = 5)
    return word
def draw_letter(letter, pos, colour=(255,255,255)):
    word = font.render(letter, True, colour)
    screen.blit(word, pos)

    
def check_word(word):
    word_flag = True
    master = SpellChecker(word, 'english')
    if master.get_typos() != []:
        word_flag = False
    return word_flag

txt = font2.render('Word not found', True, (255, 255, 255))
in_notword = False
game_over = False
guess = ''
draw_grid()
word = "jolly"
row = 1
count = 0
positions = [(50, 50), (150, 50), (250, 50), (350, 50), (450, 50)]
positions1 = [(25, 150), (120, 150), (220, 150), (320, 150), (420, 150)]
positions2 = [(25, 250), (120, 250), (220, 250), (320, 250), (420, 250)]
positions3 = [(25, 350), (120, 350), (220, 350), (320, 350), (420, 350)]
positions4 = [(25, 425), (120, 425), (220, 425), (320, 425), (420, 425)]
run = True
while run:
    if count == 5:
        if check_word(guess) == False:
            screen.blit(txt, (125, 50))
            in_notword = True
        guess_compare = guess
        if guess_compare == word:
            win = font.render('You Won!', True, (0, 255, 0))
            screen.blit(win, (100, 200))
            run = False
        guess = ''
        count = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                draw_grid()
                word = new_word()
                row = 1
                count = 0
                in_notword = False
                
            if pg.K_a <= event.key <= pg.K_z:
                if in_notword == False:
                    if row == 1:
                        check = True
                        letter = chr(event.key).lower()
                        guess += chr(event.key).lower()
                        if letter in word:
                            draw_letter(letter, positions[count], (255, 255, 0))
                            check = False
                            if word.find(letter) == 1:
                                draw_letter(letter, positions[count], (0, 255, 0))
                                check = False
                            else:
                                if guess[count] == word[count]:
                                    draw_letter(letter, positions[count], (0, 255, 0))
                                    check = False
                                    
                        if check:
                            draw_letter(letter, positions[count])
                        count += 1
                        if count >= 5:
                            row += 1
                            
                    elif row == 2:
                        check = True
                        letter = chr(event.key).lower()
                        guess += chr(event.key).lower()
                        if letter in word:
                            draw_letter(letter, positions1[count], (255, 255, 0))
                            check = False
                            if word.find(letter) == 1:
                                draw_letter(letter, positions1[count], (0, 255, 0))
                                check = False
                            else:
                                if guess[count] == word[count]:
                                    draw_letter(letter, positions1[count], (0, 255, 0))
                                    check = False
                                    
                        if check:
                            draw_letter(letter, positions1[count])
                        count += 1
                        if count >= 5:
                            row += 1
                            
                    elif row == 3:
                        check = True
                        letter = chr(event.key).lower()
                        guess += chr(event.key).lower()
                        if letter in word:
                            draw_letter(letter, positions2[count], (255, 255, 0))
                            check = False
                            if word.find(letter) == 1:
                                draw_letter(letter, positions2[count], (0, 255, 0))
                                check = False
                            else:
                                if guess[count] == word[count]:
                                    draw_letter(letter, positions2[count], (0, 255, 0))
                                    check = False
                                    
                        if check:
                            draw_letter(letter, positions2[count])
                        count += 1
                        if count >= 5:
                            row += 1 
                            
                    elif row == 4:
                        check = True
                        letter = chr(event.key).lower()
                        guess += chr(event.key).lower()
                        if letter in word:
                            draw_letter(letter, positions3[count], (255, 255, 0))
                            check = False
                            if word.find(letter) == 1:
                                draw_letter(letter, positions3[count], (0, 255, 0))
                                check = False
                            else:
                                if guess[count] == word[count]:
                                    draw_letter(letter, positions3[count], (0, 255, 0))
                                    check = False
                                    
                        if check:
                            draw_letter(letter, positions3[count])
                        count += 1
                        if count >= 5:
                            row += 1
                            
                    elif row == 5:
                        check = True
                        letter = chr(event.key).lower()
                        guess += chr(event.key).lower()
                        if letter in word:
                            draw_letter(letter, positions4[count], (255, 255, 0))
                            check = False
                            if word.find(letter) == 1:
                                draw_letter(letter, positions4[count], (0, 255, 0))
                                check = False
                            else:
                                if guess[count] == word[count]:
                                    draw_letter(letter, positions4[count], (0, 255, 0))
                                    check = False
                                    
                        if check:
                            draw_letter(letter, positions4[count])
                        count += 1
                        if count >= 5:
                            if guess == word:
                                win = font.render('You Won!', True, (0, 255, 0))
                                screen.blit(win, (100, 200))
                                run = False
                            else:
                                lose = font.render('You Lost!', True, (255, 0, 0))
                                screen.blit(lose, (100, 200))
                                game_over = True
                            
                if game_over:
                    run = False
    pg.display.flip()

time.sleep(2)
pg.quit()