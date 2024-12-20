#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Enemy3 import Enemy3
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):  #Level images number
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):  #Level images number
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 50))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 50))
            case 'Enemy1':
                enemy = Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
                return enemy
                #return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                enemy = Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
                return enemy

            case 'Level3Bg':
                list_bg = []
                for i in range(5):  # Level images number
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Enemy3':
                return Enemy3('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

