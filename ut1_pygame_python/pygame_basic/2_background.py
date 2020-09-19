import pygame


pygame.init()  # pygame 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("NADO Game")  # 게임 타이틀

# 배경 이미지 불러오기, 경로에 '\' 신경쓸 것
background = pygame.image.load(
    "C:/Users/yhmsm/workspace/nadocoding/ut1_pygame_python/background.png")

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생했는가?
            running = False  # 게임 종료 - 게임이 진행중이 아님.

    # screen.fill((0, 0, 255))  # RGB 값으로 배경 채우기
    screen.blit(background, (0, 0))  # 배경 그리기 (배경, 좌표)

    pygame.display.update()  # 게임화면을 다시 그리기 - pygame에선 배경을 계속 업데이트 해주어야함

# pygame 종료
pygame.quit()
