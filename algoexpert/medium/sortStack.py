def sortStack(stack):

    tempStack = []
    answer = []

    while stack:
        top = stack.pop()
        if not answer:
            answer.append(top)
        else:
            while answer and answer[-1] >= top:
                stack.append(answer.pop())
            answer.append(top)
            # while tempStack:
            #     answer.append(tempStack.pop())

    return answer

