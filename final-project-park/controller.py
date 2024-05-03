import pygame
from classes import buttons, gamestate, testScreen, startMenu, pauseS 
import nltk
import string
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
import random
width = 800 
height = 500
timer = pygame.time.Clock()
typed = 'sample text'
typecomplete = ''
begin = True
paused = False
char = ['a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z','A',
'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W','X','Y','Z','.',',',':',';','!']


def sentence_generator(punc,cap,surface):
    with open('maninthehighcastle.txt') as file:
        raw_text = file.read()
    list = sent_tokenize(raw_text)
    sorted_list = []
    for i in list:
        if len(i) > 95 and len(i) > 125:
            sorted_list.append(i)
    #lenfth = 54

    sent = random.choice(sorted_list)
    if punc == False:
        remove_punct = str.maketrans("", "", string.punctuation)
        sent = sent.translate(remove_punct)
    if cap == False:
        sent == sent.lower()


    sent = sent.translate(remove_punct)
    dashremove = sent.split("â€”")
    sent = " ".join(dashremove)
    
    wordlist = word_tokenize(sent)
    sent1 = " ".join(wordlist[:10])
    sent2 =" ".join(wordlist[11:20])
    sent3 = " ".join(wordlist[21:31])

    
    font = pygame.font.SysFont('mspgothic', 16)

    full = [sent1,sent2,sent3]
    #full is what it should be 

    newlines = []
    
    for i in full:
        xvar = 54
        yvar = 180+((full.index(i))*30) 
        line = i
        newline = screenline(i, xvar, yvar, surface)
        # i is what it should be (a sentence)


        newlines.append(newline)
        #current tasks: make newlines a not a NoneType object!!!
        #so, we must go to screenline and fix this issue 
    print(f'newlines:{newlines}')
        

    return newlines

class screenline:#Word
    def __init__(self, line, xvar, yvar, surface):
        self.line = str(line)
        self.yvar = yvar
        self.xvar = xvar

        self.surface = surface
        #it only sets values for these four arguments! when saved, and used with lineblit(), it should work
 
    def lineblit(self):
        self.font = pygame.font.SysFont('mspgothic', 16)
        xvar = 54
        yvar = 180 
        text =self.font.render(self.line,True, "white" )
        self.surface.blit(text, (xvar, yvar ))
        len_typed = len(typed)
        if typed == self.line[:len_typed]:
            text = self.font.render(typed,True, "green" )
            self.surface.blit(text, (xvar, yvar))
    #screenline doesnt return anything!

        
class controller:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.backround = pygame.Surface((width,height))
        self.timer = pygame.time.Clock()
        self.fps = 60
        pygame.display.set_caption('Typing Test')
        self.screen.fill('black')
        self.timer.tick(self.fps)

        self.gamestate = gamestate('startMenu')
        self.testScreen = testScreen(self.screen, self.gamestate)
        self.startMenu = startMenu(self.screen, self.gamestate)
        self.pauseS = pauseS(self.screen, self.gamestate)

        self.states = {'testScreen':self.testScreen, 'startMenu':self.startMenu, 'pauseS':self.pauseS}
        
    def mainloop(self):
        begin = True
        paused = False
        typed = ''
        typecomplete = ''
        queuelevel = True



        run = True
        while run:
            
            if paused:
                pass
                #self.gamestate.change('pauseS') #right version of gamestate?
            # elif que_next:
            #     sentences = sentences.getsent(self.state, False, False, self.screen,typed)
            #     que_next = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            L = self.states[self.gamestate.check()].run()
            if L == "quit":
                pygame.quit()
            if L: #probably wrong
                paused = True
                pass


            pygame.display.flip()
        pygame.quit()






        




        
