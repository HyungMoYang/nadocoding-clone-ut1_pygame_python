import pygame
import os


def init_game():
    # 기본 초기화 (반드시 해야 하는 것들)
    pygame.init()  # pygame 초기화 (반드시 필요)

    # 화면 크기 설정
    screen_width = 640  # 가로 크기
    screen_height = 480  # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 화면 타이틀 설정 - 윈도우 타이틀
    pygame.display.set_caption("Nado Pang")  # 게임 타이틀

    # FPS
    clock = pygame.time.Clock()


init_game()
