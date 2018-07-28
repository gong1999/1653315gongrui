a=[0,1,2]
b=(0,1,2)
a[0]="asz";
print a[0],a[1],a[2],"\n",b[0],b[1],b[2],"\n"

c=range(3)
print c,"\n"

x='apple'
y="apple"
print x[0],y[0],"\n"

things="apple orange banana grape pear"
stuff=things.split(' ')
print stuff
print ' '.join(stuff),"\n"

stuff=things.split(',')
print stuff
print ','.join(stuff)
