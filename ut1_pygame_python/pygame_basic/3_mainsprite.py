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

# 캐릭터 불러오기
# 캐릭터(스트라이프) 생성
character = pygame.image.load(
    "C:/Users/yhmsm/workspace/nadocoding/ut1_pygame_python/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 가로 크기 계산후 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기의 가장 아래에 위치

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생했는가?
            running = False  # 게임 종료 - 게임이 진행중이 아님.

    screen.blit(background, (0, 0))  # 배경 그리기 (배경, 좌표)
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()  # 게임화면을 다시 그리기 - pygame에선 배경을 계속 업데이트 해주어야함

# pygame 종료
pygame.quit()
