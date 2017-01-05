# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Uma classe que representa um único alienígena
    """

    def __init__(self, ai_settings, screen):
        """
        Inicializa o alienígena e define sua posição inicial
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.som_explosao = pygame.mixer.Sound("bounce.wav")


        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('images/alien_yellow.png').convert_alpha()
        # self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)
        self.pontuacao = 100

    def blitme(self):
        """
        Desenha o alienígena na sua posição atual
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Move o alienígena para a direita ou para a esquerda
        :return:
        """
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """
        Retorna True se o alienígena estiver na borda da tela
        :return:
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def play_explosion(self):
        channel = self.som_explosao.play()

        if channel is not None:
            # Obtem os volumes da esquerda e da direita
            left, right = 0.5, 0.5
            channel.set_volume(left, right)


class Alien2(Alien):
    """
    Cria um novo alien vermelho
    """
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)
        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('images/alien_red.png').convert_alpha()
        self.pontuacao = 70


class Alien3(Alien):
    """
    Cria um novo alien verde
    """
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)
        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('images/alien_green.png').convert_alpha()
        self.pontuacao = 50