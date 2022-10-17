# if operand: add to answer
# if ( : push to stack 
# if ) : pop from stack and add to answer until ( is found
# if operator : pop from stack until stack is not empty and and 
#               operator with less precedence is found at the top of the stack

def find_precedence(symbol):

    if symbol == '^':
        return 4
    elif symbol == '/' or symbol == '*':
        return 3
    elif symbol == '+' or symbol == '-':
        return 2
    else:
        return 1


def infix_to_prefix(string:str) -> str:
    print("input",string)
    stack = []   
    res = ""
    string = list(string[::-1])

    for idx,val in enumerate(string):
        if val == '(':
            string[idx] = ')'
        elif val == ')':
            string[idx] = '('

    string = "".join(string)

    for char in string:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            res += char
        
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                res +=stack.pop()
            stack.pop()
        else:
            while len(stack) and ( find_precedence(stack[-1]) >= find_precedence(char)):
                res += stack[-1]
                stack.pop()
            stack.append(char)

    
    while stack:
        res += stack.pop()
    
    return res[::-1]

def infix_to_postfix(string:str)->str:
    print("input",string)
    stack = []
    res = ""
 
    for char in string:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            res += char
        
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                res +=stack.pop()
            
            stack.pop()
        

        else:
            # print(char,stack)
            while len(stack) and ( find_precedence(stack[-1]) >= find_precedence(char)):
                res += stack[-1]
                stack.pop()
            stack.append(char)

    
    while stack:
        res += stack.pop()
    
    return res

print(infix_to_prefix("(A-B/C)*(A/K-L)"))
print(infix_to_postfix("(A-B/C)*(A/K-L)"))


