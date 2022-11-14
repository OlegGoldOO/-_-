import math
#f=open('okl.txt','r')



#f.close()

class point:
    def __init__(self, number, crd_x, crd_y):
        self.number = number
        self.crd_x = crd_x
        self.crd_y = crd_y

    def get_cords(self):
        return f'Координаты точки: {self.crd_x}, {self.crd_y}'

    def success(self):
        return 0

class courier:

    def __init__(self, name, crd_x, crd_y):
        self.name = name
        self.crd_x = crd_x
        self.crd_y = crd_y

    def get_cords(self):
        return f'Координаты курьера: {self.crd_x}, {self.crd_y}'

    def position(self,point):
        self.crd_x = point.crd_x
        self.crd_y = point.crd_y

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
        near_dist=self.get_distance(arr_points[0])
        near_zak = arr_points[0]
        for i in range(0,len(arr_points)):
            now_dist=self.get_distance(arr_points[i])
            if now_dist < near_dist:
                near_dist = now_dist
                near_zak = i
        return near_zak

'''''
#Формирование массива заказов
arr_points=[]
print("Количество заказов")
f=int(input())
for i in range(0,f):
    c1 = int(input())
    c2 = int(input())
    c3 = int(input())
    p=point(c1,c2,c3)
    arr_points.append(p)

#Формирование массива курьеров
arr_couriers=[]
print("Количество курьеров")
f=int(input())
for i in range(0,f):
    c1 = int(input())
    c2 = int(input())
    c3 = int(input())
    arr_couriers.append(courier(c3,c1,c2))

'''''

o1 = point(1,2,2)
o2 = point(2,2,3)
o3 = point(3,2,1)
o4 = point(4,4,3)
o5 = point(5,7,1)

c1 = courier("Max",2,3)
c2 = courier("Alex",6,2)
'''''
c3 = courier("Rob",8,3)
c4 = courier("Fred",5,2)
c5 = courier("Tim",3,3)
'''
arr_couriers = []
arr_couriers.append(c1)
arr_couriers.append(c2)
'''''
arr_couriers.append(c3)
arr_couriers.append(c4)
arr_couriers.append(c5)
'''
arr_points=[]
arr_points.append(o1)
arr_points.append(o2)
arr_points.append(o3)
arr_points.append(o4)
arr_points.append(o5)



while True:
    for i in range(0, len(arr_couriers) + 1):
        zak=arr_couriers[i].near()
        arr_points.pop(zak)
        arr_couriers[i].delivery()
        if len(arr_points)==0:
            break



