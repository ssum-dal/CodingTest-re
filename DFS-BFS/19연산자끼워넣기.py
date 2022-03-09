import sys

input = sys.stdin.readline

def dfs(num, index):
    if index == n:
        result.append(num)
        return

    if operator[0] != 0:
        operator[0] -= 1
        dfs(num+number[index], index+1)
        operator[0] += 1
    
    if operator[1] != 0:
        operator[1] -= 1
        dfs(num-number[index], index+1)
        operator[1] += 1
    
    if operator[2] != 0:
        operator[2] -= 1
        dfs(num*number[index], index+1)
        operator[2] += 1
    
    if operator[3] != 0:
        operator[3] -= 1
        if num >= 0:
            dfs(num // number[index], index+1)
        else:
            dfs((num*-1 // number[index])*-1, index+1)
        operator[3] += 1

n = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))
result = []

dfs(number[0], 1)

print(max(result))
print(min(result))

