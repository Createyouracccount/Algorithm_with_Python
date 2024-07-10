

def solution(s):
    count = 0
    length = len(s)
    
    for i in range(length):
        rotated_s = s[i:] + s[:i]
        stack = []
        
        for char in rotated_s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack:
                    break
                top = stack.pop()
                if char == ')' and top != '(':
                    break
                elif char == ']' and top != '[':
                    break
                elif char == '}' and top != '{':
                    break
        else:
            if not stack:
                count += 1
    
    return count