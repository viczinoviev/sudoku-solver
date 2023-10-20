class Cube:
    rows = 9
    cols = 9
    
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.temp = 0
        
    def draw(self, screen):
        font = pygame.font.SysFont("comicsans, 40")
        
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap
        
        if self.temp != 0 and self.value == 0:
            num = font.render(str(self.temp), 1, (128, 128, 128))
            screen.blit(num, (x + (gap/2 - font.get_width()/2) , y + (gap/2 - font.get_height()/2)))
        elif not self.value == 0:
            num = font.render(str(self.value), 1, (0, 0, 0))
            screen.blit(num, (x + (gap/2 - font.get_width()/2) , y + (gap/2 - font.get_height()/2)))
            
        if self.selected:
            pygame.draw.rect(screen, (255,0,0), (x, y, gap, gap), 3)
            
    def draw_backtrack(self, window, valid=True):
        font = pygame.font.SysFont("comicsans, 40")
        
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap
        
        pygame.draw.rect(screen, (255, 255, 255), (x, y, gap, gap))
        
        num = font.render(str(self.temp), 1, (128, 128, 128))
        screen.blit(num, (x + (gap/2 - font.get_width()/2) , y + (gap/2 - font.get_height()/2)))
        if valid:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, gap, gap), 3)
            
    def setValue(self, value):
        self.value = value
        
    def setTemp(self, value):
        self.temp = value
        
        
        