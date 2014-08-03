__author__ = 'sergey'


class AbstractDuck:

    def __init__(self, name):
        self.name = name

    def setFly(self, method):
        self.fly = method
        #raise NotImplementedError()


class Swiming:
    def __call__(self, *args, **kwargs):
        print "I'm swimming"


class Flying:
    def __call__(self, *args, **kwargs):
        print "I'm fly"

    def fly(self):
        print "I'm fly"


class Quacking:
    def __call__(self, *args, **kwargs):
        print "quack-quack"


class DuckRedCrestedPochard(AbstractDuck):
    swim = Swiming()
    # def swim(self):
    #     Swiming()


class SantaCruz(AbstractDuck):
    def __init__(self, name):
        AbstractDuck.__init__(self, name)
        fly_instance = Flying()
        self.setFly(fly_instance)


    # def swim(self):
    #     Swim.swim()


if __name__ == '__main__':
    # FredyDuck = DuckRedCrestedPochard('FredyDuck')
    # FredyDuck.swim()
    # #FredyDuck.fly()

    AlphaDuck = SantaCruz('AlphaDuck')
    #AlphaDuck.swim()
    AlphaDuck.fly()

