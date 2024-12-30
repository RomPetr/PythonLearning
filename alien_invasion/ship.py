import pygame
from settings import Settings

class Ship():
    ''' Класс для управления кораблем '''
    def __init__(self, ai_game):
        ''' Инициализирует корабль и создает его начальную позицию '''
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()
        self.settings = Settings()


        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        ''' Обновляет позицию корабля с учетом флага '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.sheep_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.sheep_speed
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        ''' Рисует корабль в текущей позиции '''
        self.screen.blit(self.image, self.rect)

