#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 0)
        print(f"[DEBUG] Enemy {self.name} created at position {self.rect.topleft}")  # Log de criação
        # Verifique se a velocidade de movimento é maior que zero
        if ENTITY_SPEED.get(self.name, 0) == 0:
            print(f"[ERROR] Invalid movement speed for {self.name}. Check ENTITY_SPEED configuration") # Log de erro
    def move(self, ):
        # Verifique a posição antes de mover
        print(f"[DEBUG] Enemy {self.name} current position: {self.rect.topleft}") # Antes de mover
        if self.rect.right > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        else:
            self.health = 0
        print(f"[DEBUG] Enemy {self.name} moved to: {self.rect.topleft}") # Depois de mover

    def shoot(self, ):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
