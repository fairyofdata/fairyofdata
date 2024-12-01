X = int(input())

for I in range(1,X+1):
    a,b = map(int, input().split())
    print(f'Case #{I}: {a} + {b} = {a+b}')