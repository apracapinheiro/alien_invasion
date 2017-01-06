# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """
        Inicializa a nave e define sua posição inicial
        """
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.som_tiro = pygame.mixer.Sound("Zap.wav")
        self.explosion = pygame.mixer.Sound("ship_explosion.wav")

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship_color.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena uma valor decimal para o centro da nave
        self.center = float(self.rect.centerx)

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Atualiza a posição da nave de acordo com a flag de movimento
        :return:
        """

        # Atualiza o valor do centro da nave e não o retângulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center

    def blitme(self):
        """
        Desenha a nave em sua posição atual
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """
        Centraliza a nave na tela
        :return:
        """
        self.center = self.screen_rect.centerx

    def shot_sound(self):
        channel = self.som_tiro.play()

        if channel is not None:
            # Obtem os volumes da esquerda e da direita
            left, right = 0.5, 0.5
            channel.set_volume(left, right)


    def ship_explosion(self):
        channel = self.explosion.play()

        if channel is not None:
            # Obtem os volumes da esquerda e da direita
            left, right = 0.6, 0.6
            channel.set_volume(left, right)