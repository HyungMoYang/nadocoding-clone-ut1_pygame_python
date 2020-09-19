
import pygame
import os

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

##################################################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트, 등)

current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환

# 현재 위치+images파일: images 폴더위치 반환
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 스테이지 위에 캐릭터를 두기 위해서

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height - stage_height  # 스테이지 위

running = True
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # 게임화면을 다시 그리기 - pygame에선 배경을 계속 업데이트 해주어야함

# pygame 종료
pygame.quit()
