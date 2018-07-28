#calculate the circumference of the Earth's equator and the Earth's surface area
from sys import argv
script,r=argv#input the radius of the Earth's equator(m)
pi=3.14#define pi
r=float(r)*1000#change the unit
c=2*pi*r#calculate the circumference of the Earth's equator
s=4*pi*r**2#calculate the Earth's surface area
print "\n\tthe circumference of the Earth's equator is %d m\n\tthe Earth's surface area is %d m^2\n"%(c,s)#output result

r=float(raw_input("please input the radius of the Earth's equator(km):"))*1000#input the radius of the Earth's equator(m)
c=2*pi*r#calculate the circumference of the Earth's equator
s=4*pi*r**2#calculate the Earth's surface area
print "\n\tthe circumference of the Earth's equator is %d m\n\tthe Earth's surface area is %d m^2\n"%(c,s)#output result
