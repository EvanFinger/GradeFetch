
class Stack:
    stack = []
    
    def __init__(self, initValue = None):
        self.stack.append(initValue)
    
    def push(self, item):
        """Push an element on top of the stack

        Args:
            item (any): element to be pushed onto the stack
        """
        self.stack.append(item)
        
    def pop(self):
        """Discards the top element of the stack

        Returns:
            any: The element discarded from stack
        """
        return self.stack.pop()
        
    def top(self):
        """Returns the top element of the stack

        Returns:
            any: The top element of the stack
        """
        return self.stack[len(self.stack) - 1]
    
    def size(self):
        """Returns the size of the stack

        Returns:
            int: Number of elements in the stack
        """
        return len(self.stack)
    
    def empty(self):
        """Returns whether or not the stack is empty

        Returns:
            Boolean: True if the stack is empty, False otherwise
        """
        return len(self.stack) == 0
    
    