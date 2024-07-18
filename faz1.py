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
class FunctionNode(Node):
    def __init__(self,function,child):
        self.function = function
        self.child = child

    def evaluate(self,x):
        value = self.child.evaluate(x)
        if self.function == "tanh" :
            return  math.tanh(value)
        if self.function == "sin" :
            return  math.sin(value)
        if self.function == "cos" :
            return  math.cos(value)
class VariableNode(Node) :
    def evaluate(self,x) :
        return x
class ConstantNode(Node):
    def __init__(self,value):
        self.value = value

    def evaluate(self,x):
        return self.value
        
            
        
            
            






        
