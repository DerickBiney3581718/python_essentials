class Stack:
    def __init__(self):
        self.__stack_list = []
        print('Well, hello there')

    def push(self, val):
        self.__stack_list.append(val)
    
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
    def __str__(self):
        return str(self.__stack_list)
stack1 = Stack()
stack1.push(2)
stack1.push(4)
stack1.push(6)

stack1.pop()
print(stack1)

    