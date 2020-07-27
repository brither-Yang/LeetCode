class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            if self.min_stack[-1] > x:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.stack:
            return
        else:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return

    def getMin(self):
        return self.min_stack[-1]
