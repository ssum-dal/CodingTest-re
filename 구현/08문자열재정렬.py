import sys

input = sys.stdin.readline

s = list(input().rstrip())
num = 0
answer = ''

s.sort()

for i in s:
    if ord(i) < 65:
        num += int(i)
    else:
        answer += i

if num == 0:
    print(answer)
else:
    print(answer+str(num))