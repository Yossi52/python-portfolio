import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        super().__init__()
        img = pygame.image.load(image_path)
        self.image = pygame.transform.scale(img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.move_speed = 0.1
        self.shoot_delay = 1500
        self.last_shoot = pygame.time.get_ticks()

    def update(self, dt):
        self.rect.move_ip(self.move_speed * dt, 0)
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.move_speed *= -1
            return self.rect.center

