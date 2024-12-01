def solve(k, signs):
    def backtrack(idx, used, current):
        if idx == k + 1:
            result = ''.join(map(str, current))
            return result, result
        
        min_val, max_val = '9' * (k + 1), '0' * (k + 1)
        
        for num in range(10):
            if num not in used:
                if idx == 0 or (signs[idx-1] == '<' and current[-1] < num) or (signs[idx-1] == '>' and current[-1] > num):
                    used.add(num)
                    current.append(num)
                    min_sub, max_sub = backtrack(idx + 1, used, current)
                    min_val = min(min_val, min_sub)
                    max_val = max(max_val, max_sub)
                    current.pop()
                    used.remove(num)
        
        return min_val, max_val

    min_value, max_value = backtrack(0, set(), [])
    return max_value, min_value

# 입력 받기
k = int(input().strip())
signs = input().strip().split()

# 결과 계산 및 출력
max_value, min_value = solve(k, signs)
print(max_value)
print(min_value)
