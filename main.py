class SnakeEye:
    def __init__(self):
        self.length = 5

    def __gt__(self, other):
        return self

    def __sub__(self, other):
        self.length += 2
        return self
    
    def __len__(self):
        res, self.length = self.length, 5 
        return res
    
o = SnakeEye()

print(len((o > o) - 0 - 0 - 0 - 0))
print(len((o > o) - 0 - 0 - 0 - 0 - 0 - 0 - 0 - 0))