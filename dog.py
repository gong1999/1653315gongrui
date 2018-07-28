class organism(object):
    def __init__(self):
        self.status="alive"
    def say1(self):
        print"I belong to organism."

class animal(organism):
    def __init__(self):
        super(animal,self).__init__()
        self.mitochondria=True
    def say2(self):
        print"I belong to animal."
        
class vertebrate(animal):
    def __init__(self):
        super(vertebrate,self).__init__()
        self.spine=True
    def say3(self):
        print"I belong to vertebrate."

class mammal(vertebrate):
    def __init__(self):
        super(mammal,self).__init__()
        self.lactation=True
    def say4(self):
        print"I belong to mammal."

class dog(mammal):
    def __init__(self):
        super(dog,self).__init__()
        self.name=""
        self.owner=""
    def say5(self):
        print"I belong to dog and I can wangwang."
