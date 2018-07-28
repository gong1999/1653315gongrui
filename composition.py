class parent(object):
    def fun(self):
        print "parent fun()"
class child(object):
    def __init__(self):
        self.parent=parent()
    def fun(self):
        self.parent.fun()

dad=parent()
son=child()
dad.fun()
son.fun()
