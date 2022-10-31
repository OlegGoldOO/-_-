import math
class courier:
    def __init__(self, crd_x, crd_y):
        self.crd_x = crd_x
        self.crd_y = crd_y
class point:
    def __init__(self,crd_x,crd_y):
        self.crd_x=crd_x
        self.crd_y=crd_y
    def dist(x1, y1, x2, y2):
        dist = math.hypot(x2 - x1,y2 - y1)
        return dist


k=point.dist(1,2,3,4,)
