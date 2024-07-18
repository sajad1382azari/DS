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
        
# Example 1: y = sin(x) + cos(x)
example1 = OperandNode('+', FunctionNode('sin', VariableNode()), FunctionNode('cos', VariableNode()))

# Example 2: y = tanh(x) * (x + 1)
example2 = OperandNode('*', FunctionNode('tanh', VariableNode()), OperandNode('+', VariableNode(), ConstantNode(1)))

# Example 3: y = (x - 3) / (x + 2)
example3 = OperandNode('/', OperandNode('-', VariableNode(), ConstantNode(3)), OperandNode('+', VariableNode(), ConstantNode(2)))

# Function to evaluate an expression
def evaluate_expression_tree(tree, x):
    return tree.evaluate(x)

# Test the examples
x_values = [0, 1, 2, 3]

print("Example 1: y = sin(x) + cos(x)")
for x in x_values:
    print(f"x = {x}, y = {evaluate_expression_tree(example1, x)}")

print("\nExample 2: y = tanh(x) * (x + 1)")
for x in x_values:
    print(f"x = {x}, y = {evaluate_expression_tree(example2, x)}")

print("\nExample 3: y = (x - 3) / (x + 2)")
for x in x_values:
    print(f"x = {x}, y = {evaluate_expression_tree(example3, x)}")

        
            
        
            
            






        
