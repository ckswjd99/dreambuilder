import pygame

class font:
    def __init__(self, filename):
        self.resource = pygame.image.load(filename)
        self.letters = ['', '!', '"', '#', '$', '%', '&', '\'', '(', ')', ',', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ';', ':', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        self.word_space = 2
    
    def letter(self, c):
        index = self.letters.index(c)
        if index == -1:
            index = 0
        
        index_now = 0
        start_loc = 0
        end_loc = 1
        while self.resource.get_at((end_loc, 0)) != (237, 28, 36):
            end_loc += 1

        while index_now != index:
            start_loc = end_loc + 1
            end_loc += 1
            while self.resource.get_at((end_loc, 0)) != (237, 28, 36):
                end_loc += 1
            index_now += 1
        
        end_loc -= 1
        result_image = self.resource.subsurface(pygame.Rect((start_loc, 0), (end_loc-start_loc, self.resource.get_height())))
        return result_image

    def line(self, l, color):
        letters = []
        for c in l:
            letters.append( self.letter(c) )
        
        width = 0
        for c in letters:
            width += c.get_width()
        width += (len(letters)-1)*self.word_space
        height = letters[0].get_height()

        result_image = pygame.Surface((width, height))
        result_image.fill((255,255,255))
        add_index = 0
        for c in letters:
            result_image.blit(c, (add_index, 0))
            add_index += c.get_width()
            add_index += self.word_space

        for i in range(result_image.get_width()):
            for j in range(result_image.get_height()):
                if result_image.get_at((i,j)) == (0,0,0):
                    result_image.set_at((i,j), color)

        result_image.set_colorkey((255,255,255))

        return result_image
