import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

class Man(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("Man.png")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 240
        
        self.dx = 0
        self.dy = 3
        
    def update(self):
        self.rect.centery += self.dy
        
        if self.rect.top <= 0:
            self.dy = -self.dy
            
        if self.rect.bottom >= screen.get_height():
            self.dy = -self.dy
        
def main():
    pygame.display.set_caption("Do the vertical man!")
    background = pygame.Surface(screen.get_size())
    background.fill("green")
    screen.blit(background, (0, 0))
        
    man = Man()
    allSprites = pygame.sprite.Group(man)
        
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                    
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
            
        pygame.display.flip()
            
if __name__ == "__main__":
    main()
    pygame.quit()