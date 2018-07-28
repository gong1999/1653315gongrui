class parent(object):
    def altered(self):
            print "parent altered()"
class child(parent):
    def altered(self):
            print "child altered()"
            super(child,self).altered()

dad=parent()
son=child()
dad.altered()
son.altered()
