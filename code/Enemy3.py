from code.Const import WIN_HEIGHT, ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot


class Enemy3(Enemy):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed_y = 2
        self.direction_y = 1
        self.speed_x = ENTITY_SPEED.get(name, 1)
        self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 70)

    def move(self):
        self.rect.centerx -= self.speed_x
        self.rect.y += self.speed_y * self.direction_y

        if self.rect.top <= 0:
            self.direction_y = 1
            self.speed_y = 4
        elif self.rect.bottom >= WIN_HEIGHT:
            self.direction_y = -1
            self.speed_y = 2
    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 70)
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))