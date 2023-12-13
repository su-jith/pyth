import math

def area(r):
    area=4*math.pi*r**2
    return area
def volume(r):
    volume=(4*math.pi*r**3)/3
    return volume
r=int(input('enter the radius of the circle'))
l=int(input('enter the length of the cuboid'))
w=int(input('enter the width of the cuboid'))
h=int(input('enter the height of the cuboid'))
n=int(input('enter the radius of the sphere'))

print('area of circle is:',circle.area(r))
print('perimerter of circle is:',circle.perimeter(r))
print('area of cuboid is:',cuboid.area(l,w,h))
print('volume of cuboid is:',cuboid.volume(l,w,h))
print('area of sphere is:',sphere.area(n))
print('volume of sphere is:',sphere.volume(n))
