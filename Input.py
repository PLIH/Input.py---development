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
    def label(self, toPrint):
        font = pygame.font.SysFont("None", 10)
        myText = font.render(toPrint, 1, (0,0,0))
        return myText

    #draw/create
    def create(self, surface, colour, length, height, x, y):
        pygame.draw.rect(surface,(255,255,255), (x,y,length,height),0)
        pygame.draw.rect(surface,(0,0,0),(x,y,length,height),1)
        self.rect = pygame.Rect(x,y,length,height)
        #return surface

    #Take input
    def takeInput(self, surface):
        keepGoing = True
        text = ""
        x = self.rect.topleft[0]
        y = self.rect.topleft[1]
        while keepGoing:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        keepGoing = False
                    elif event.key == pygame.K_0:
                        text += "0"
            myText = self.label(text)
            surface.blit(myText, (x,y))
        return text
     #problem: cannot see input inside textbox being written
    #b/c txtbox.blit in main keeps over writting it.
    # must find way to suspend txtbox.blit, and blit with this instead
    # perhaps returning a parital text?
        # would have to run input loop in the main.... ick.

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
