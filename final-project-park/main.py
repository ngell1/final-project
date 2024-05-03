import pygame

from controller import controller

def main():
    pygame.init()
    x = controller()
    x.mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/

if __name__ == '__main__':
    main()
