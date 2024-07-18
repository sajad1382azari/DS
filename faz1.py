import math

class operandNude(Node):
    def__init__(self,operator,left,right):
        self.operator=operator
        self.left=left
        self.right=right
def evaluate(self,x):
    if self.operator=="+":
        return self.left.evaluate(x)+self.right.evaluate(x)
    elif self.operator=="-":
        return self.left.evaluate(x)-self.right.evaluate(x)
    elif self.operator=="*":
        return self.left.evaluate(x)*self.right.evaluate(x)
    elif self.operator=="/":
        return self.left.evaluate(x)/self.right.evaluate(x)
