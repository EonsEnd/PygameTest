import pygame
import pygame.locals
import configparser



class Level(object):
    def load_file(self, filename="assets/example.map"):
        self.map = []
        self.key = {}
        parser = ConfigParser.ConfigParser()
        parser.read(filename)
        self.tileset = parser.get("level", "tileset")
        self.map = parser.get("level", "map").split("\n")
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                self.key[section] = desc
        self.width = len(self.map[0])
        self.height = len(self.map)

    def get_tile(self, x, y):
        try:
            char = self.map[y][x]
        except IndexError:
            return {}
        try:
            return self.key[char]
        except KeyError:
            return {}



def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    print("image width:", image_width)
    print("width:", width)
    print("w / w: ", int(image_width/width))
    for tile_x in range(0, int(image_width/width)):
        print("entered for loop")
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height/height)):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table


if __name__=='__main__':
  
    pygame.init()
    screen = pygame.display.set_mode((128, 98)) #default - 128,98
    screen.fill((255, 255, 255))
    table = load_tile_table("assets/tilechart.png", 16, 16)
    print("hellooooo")
    print(get_tile(0,0))
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*32, y*24))
            
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass
