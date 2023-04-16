import pygame

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        super().__init__()
        img = pygame.image.load(image_path)
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.move_speed = 0.3
        self.rect.center = position

    def update(self, dt):
        self.rect.move_ip(0, -self.move_speed * dt)
        if self.rect.bottom < 0:
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        super().__init__()
        img = pygame.image.load(image_path)
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.move_speed = 0.3
        self.rect.center = position

    def update(self, dt):
        self.rect.move_ip(0, self.move_speed * dt)
        if self.rect.top > 800:
            self.kill()