class parent(object):
    def override(self):
            print "parent override()"
class child(parent):
    def override(self):
            print "child override()"

dad=parent()
son=child()
dad.override()
son.override()
