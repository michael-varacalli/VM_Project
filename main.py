PUSH = 0x01
ADD = 0x02
SUB = 0x03
MUL = 0x04
DIV = 0x05


class VM:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def show_stack(self):
        print(self.stack)

    def add(self):
        num2 = self.pop()
        num1 = self.pop()
        result = num1 + num2
        self.push(result)

    def sub(self):
        num2 = self.pop()
        num1 = self.pop()
        result = num1-num2
        self.push(result)
    def mult(self):
        num2 = self.pop()
        num1 = self.pop()
        self.push(num1*num2)
    def div(self):
        num2 = self.pop()
        num1 = self.pop()
        self.push(num1/num2)
    def run(self, program):
        for instruction in program:
            operation = instruction[0]
            if operation == 0x01:
                self.push(instruction[1])
            if operation == 0x02:
                self.add()
            if operation == 0x03:
                self.sub()
            if operation == 0x04:
                self.mult()
            if operation == 0x05:
                self.div()





# --------- run program --------

program = [
    (PUSH,50),
    (PUSH,10),
    (ADD,)
]

vm = VM()
vm.run(program)
print (program)
vm.show_stack()
