s = "3[a]2[bc]"
stack=[]
for char in s:
    if char=='[':
        stack.append(char)
    elif char.isalpha():
        stack.append(char)
    elif char==']':
        res=''
        while stack and stack[-1]!='[':
            res=stack.pop()+res
        if stack:
            stack.pop()
        num=''
        while stack and stack[-1].isdigit():
            num=stack.pop()+num
        repeat_count=int(num)
        stack.append(res*repeat_count)
    else:
        stack.append(char)
print(''.join(stack))