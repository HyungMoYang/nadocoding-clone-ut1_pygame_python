
# 버그내역 - 이중 for문 때문에 공이 하나만 사라지는 경우의 버그 픽스
# 이중 for문을 한꺼번에 탈출하는 일종의 트릭 사용

balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print(f"ball: {ball_val}")
    for weapon_idx, weapon_val in enumerate(weapons):
        print(f"weapons: ", weapon_val)
        if ball_val == weapon_val:  # 충돌 체크
            print("공과 무기가 충돌")
            break
    else:
        continue
    print("바깥 for문 break")
    break
