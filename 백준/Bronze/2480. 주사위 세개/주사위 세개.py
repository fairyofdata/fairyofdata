A, B, C = map(int, input().split())
prize = 0

# 주사위 눈의 범위를 확인하여 상금 계산
if 1 <= A <= 6 and 1 <= B <= 6 and 1 <= C <= 6:
    if A == B == C:
        prize = 10000 + A * 1000
    elif A == B and B != C:
        prize = 1000 + A * 100
    elif B == C and C != A:
        prize = 1000 + B * 100
    elif A == C and A != B:
        prize = 1000 + C * 100
    else:
        prize = max(A, B, C) * 100
else:
    print("주사위 눈은 1 이상 6 이하의 정수여야 합니다.")

print(prize)


# 랜덤으로 세 숫자 생성 (1부터 6 중에서)
# 상금 초기값 설정 x=0
# if  A=B=C이면, X = X + 10000+ A*1000
# else if (A=B and B=|C) 이면, X = X+ A*100
# else if (B=C and A=|C) 이면, X = X+ B*100
# else if (A=C and B=|A) 이면, X = X+ C*100
# else if A=|B=|C 이면, X = X+ max(A,B,C)*100
