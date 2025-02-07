from enum import Enum

import numpy as np
import pygame

import gymnasium as gym
from gymnasium import spaces

class Actions(Enum):
    """
    Thay vi doc ca ma tran, thi co the thiet lap cho no di chuyen.
    Dung yen de no co the suy nghi ra hanh dong khac.
    Di chuyen den cac o khac va dat 0 tuong ung voi x, 1 tuong ung voi o vuong.
    """
    STAY = 0 
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    PLACE_0 = 5
    PLACE_1 = 6

class NonogramEnv(gym.Env):

    def __init__(self):
        pass
    