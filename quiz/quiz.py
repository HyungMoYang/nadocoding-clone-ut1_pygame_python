##################################################################################

# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하던 게임 종료
# 5. FPS는 30 으로 고정

# [게임 이미지]
# 1. 배경: 640 * 480(세로 가로) - background.png
# 2. 캐릭터: 70 * 70 - character.png
# 3. 똥: 70 * 70 - enemy.png

##################################################################################
import pygame
import random
##################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()  # pygame 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 - 윈도우 타이틀
pygame.display.set_caption("게임 이름")  # 게임 타이틀

# FPS
clock = pygame.time.Clock()
##################################################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트, 등)

# 배경 이미지 불러오기, 경로에 '\' 신경쓸 것
background = pygame.image.load(
    "C:/Users/yhmsm/workspace/nadocoding/ut1_pygame_python/quiz/background_image.png")

# 캐릭터 이미지 불러오기
character = pygame.image.load(
    "C:/Users/yhmsm/workspace/nadocoding/ut1_pygame_python/quiz/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

# 적(dong) 이미지 불러오기
dong = pygame.image.load(
    "C:/Users/yhmsm/workspace/nadocoding/ut1_pygame_python/quiz/dong.png")
dong_size = dong.get_rect().size
dong_width = dong_size[0]
dong_height = dong_size[1]
dong_x_pos = random.randint(0, screen_width - dong_width)
dong_y_pos = 0
dong_speed = 10

# 이동속도
character_speed = 10

# 이동좌표
to_x = 0
to_y = 0

running = True
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    dong_y_pos += dong_speed  # dong이 아래로 조금씩 내려옴

    # 경계선 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # dong이 다 떨어졌을 때, 재생성
    if dong_y_pos > screen_height:
        dong_y_pos = 0
        dong_x_pos = random.randint(0, screen_width - dong_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    dong_rect = dong.get_rect()
    dong_rect.left = dong_x_pos
    dong_rect.top = dong_y_pos

    if character_rect.colliderect(dong_rect):
        print("Collision")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(dong, (dong_x_pos, dong_y_pos))

    pygame.display.update()  # 게임화면을 다시 그리기 - pygame에선 배경을 계속 업데이트 해주어야함

# pygame 종료
pygame.quit()
