import math
f=open('okl.txt','r')
arr_points=[]
for i in range(0,len(f)+1):
    c=f.readline()
    arr_points.append([c[0],c[1]])
arr_couriers=[]
for i in range(0,len(f)+1):
    c=f.readline()
    arr_couriers.append([c[0],c[1]])
f.close()
class point:
    def __init__(self,crd_x,crd_y):
        self.crd_x=crd_x
        self.crd_y=crd_y

class courier:
    def __init__(self, crd_x, crd_y):
        self.crd_x = crd_x
        self.crd_y = crd_y
    def delivery(self):
        self.crd_x = 0
        self.crd_y = 0
    def get_distance(self,other_point):
        x1= self.crd_x
        y1 = self.crd_y
        x2 = other_point.crd_x
        y2 = other_point.crd_y
        dist = math.hypot(x2 - x1, y2 - y1)
        return dist
    def near(self):
        near_dist=1000000000000000
        for i in range(len(arr_points)+1):
            now_dist=self.get_distance(arr_points[i])
            if now_dist < near_dist:
                near_dist = now_dist
        return near_dist



c1=courier(1,2)
k=c1.delivery
print(k)

