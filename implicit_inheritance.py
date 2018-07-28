class parent(object):
    def implicit(self):
            print "parent implicit()"
class child(parent):
    pass

dad=parent()
son=child()
dad.implicit()
son.implicit()
