#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame.image
import pygame.mixer_music
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        self.alunos = [
            {"ru": "4411784", "name": "Jackson"},
            {"ru": "1234", "name": "Ilka"},
            {"ru": "1234", "name": "Gabriel"},
            {"ru": "1234", "name": "Voltaire"},
         ]


    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES / Desenhar imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50,"Mountain", C_ORANGE, (WIN_WIDTH / 2, 70))
            self.menu_text(50, "Shooter", C_ORANGE, (WIN_WIDTH / 2, 120))

            # View menu options
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, (WIN_WIDTH / 2, 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, (WIN_WIDTH / 2, 200 + 25 * i))
            y_pos = 10
            for aluno in self.alunos:
                self.menu_text(12, f"{aluno['name']}-RU: {aluno['ru']}", C_YELLOW,
                               (WIN_WIDTH - 15, y_pos),align="right")
                y_pos += 20
            pygame.display.flip()

           ## Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window
                    quit() #End pygame

                # Quando pressionado a tecla seta para baixo movimentar no menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #Seta para Baixo DOWN KEY
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:# seta para cima UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION [menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, align="center"):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        
        
        if align == "right":
            text_rect.topright = text_center_pos
        else:
            text_rect.center = text_center_pos
        self.window.blit(source=text_surface, dest=text_rect)

