import pygame

WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Window")
WHITE = (255,255,255)
FPS = 30

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, int(image_width/width)):
        print("entered for loop")
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height/height)):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table


def drawWindow():
    WIN.fill(WHITE)
    pygame.display.update()
    

def main():
    clock = pygame.time.Clock()
    run = True
    table = load_tile_table("assets/tilechart.png", 16, 16)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawWindow()

    pygame.quit()



if __name__=='__main__':
    main()