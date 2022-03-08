'''
완전탐색
'''

def solution(s):
    result = len(s)
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2+1):
        tmp = s[ : i]
        answer = ''
        num = 1

        for j in range(i, len(s), i):
            if tmp == s[j : j+i]:
                num += 1
            else:
                if num == 1:
                    answer += tmp
                else:
                    answer += str(num) + tmp
                
                tmp = s[j : j+i]
                num = 1
        
        if num == 1:
            answer += tmp
        else:
            answer += str(num) + tmp
            
        result = min(result, len(answer))
       

    return result