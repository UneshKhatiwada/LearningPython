class Box:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h
        self.volume = self.length * self.breadth * self.height 

b1 = Box(l=8.2, b=5, h=6.3)
print(f"The volume of  box is: {b1.volume}")
