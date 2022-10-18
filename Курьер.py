class point:
    def __init__(self,crd_x,crd_y):
        self.crd_x=crd_x
        self.crd_y=crd_y
    def __str__(self):
        return f'Координаты точки{self.crd_x}, {self.crd_y}'
k=point(1,2)
print(k)