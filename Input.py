#Source File Name: Input.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-06-10
#Program Description: An importable class to create input boxes in pygame
#Revision History:
#

import pygame

pygame.init()

class Textbox:
        
    #output the content
    def label(self, surface, toPrint, colour, size, x, y):
        font = pygame.font.SysFont("None", size)
        myText = font.render(toPrint, 1, colour)
        surface.blit(myText, (x,y))

    #draw/create
    def create(self, surface, colour, length, height, x, y):
        pygame.draw.rect(surface,(255,255,255), (x,y,length,height),0)
        pygame.draw.rect(surface,(0,0,0),(x,y,length,height),1)
        self.rect = pygame.Rect(x,y,length,height)
        return surface

    #
    def onClick(self,mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
