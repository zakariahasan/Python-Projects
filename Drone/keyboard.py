import pygame


def init():
    pygame.init()
    window = pygame.display.set_mode((400, 400))

def getkey(K_Name):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    mykey = getattr(pygame, 'K_{}'.format(K_Name))
    print('K_{}'.format(K_Name))
    if keyInput[mykey]:
        ans = True
    pygame.display.update()
    return ans
def main():
    if getkey('LEFT'):
        print('Left key pressed')
    if getkey('RIGHT'):
        print('Right key pressed')


if __name__ == '__main__':
    init()

    while True:
        main()
