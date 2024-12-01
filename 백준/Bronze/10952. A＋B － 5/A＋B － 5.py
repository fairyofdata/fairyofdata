while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break  # 입력이 0, 0일 경우 루프를 종료합니다.
    print(A + B)