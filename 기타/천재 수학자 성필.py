from collections import deque

class Calculator:
    def __init__(self):
        self.num_stack = deque()

    def plus(self):
        x = self.num_stack.pop()
        y = self.num_stack.pop()
        self.num_stack.append(x+y)

    def minus(self):
        x = self.num_stack.pop()
        y = self.num_stack.pop()
        self.num_stack.append(y-x) # 순서 주의

    def mul(self):
        x = self.num_stack.pop()
        y = self.num_stack.pop()
        self.num_stack.append(x*y)

    def div(self):
        x = self.num_stack.pop()
        y = self.num_stack.pop()
        self.num_stack.append(y//x) # 순서 주의

    def cal(self, data):
        ops = ['+', '-', '*', '/']
        for i in data:
            if i not in ops: # 숫자라면
                self.num_stack.append(int(i))
            else: # 연산자라면
                if i == '+':
                    self.plus()
                elif i == '-':
                    self.minus()
                elif i == '*':
                    self.mul()
                elif i == '/':
                    self.div()

        return self.num_stack.pop()

n = input().rstrip()
cal = Calculator()
print(cal.cal(n))
