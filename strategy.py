__author__ = 'sergey'


class AbstractDuck:
    def __init__(self, name):
        self.name = name
        print "I'm " + name

    def setFly(self, method):
        self.fly = method

    def setQuack(self, method):
        self.quack = method

    def swim(self):
        print "\tAll ducks float!"


# to call a method through the "fly" of the object
class Flying:
    # def __call__(self, *args, **kwargs):
    #     print "I'm fly"

    def fly(self):
        print "\tI'm fly-method"


# to call a method through the object
class Quacking:
    def __call__(self, *args, **kwargs):
        print "\t... quack-quack ..."


class DuckRedCrestedPochard(AbstractDuck):
    def __init__(self, name):
        AbstractDuck.__init__(self, name)

        fly_instance = Flying()
        self.setFly(fly_instance.fly)

        quack_instance = Quacking()
        self.setQuack(quack_instance)


class SantaCruz(AbstractDuck):
    def __init__(self, name):
        AbstractDuck.__init__(self, name)

        fly_instance = Flying()
        self.setFly(fly_instance.fly)

        quack_instance = Quacking()
        self.setQuack(quack_instance)


class WoodDuck(AbstractDuck):
    def __init__(self, name):
        AbstractDuck.__init__(self, name)


class DuckDecoy(AbstractDuck):
    def __init__(self, name):
        AbstractDuck.__init__(self, name)

        quack_instance = Quacking()
        self.setQuack(quack_instance)


if __name__ == '__main__':
    AlphaDuck = SantaCruz('AlphaDuck')
    AlphaDuck.swim()
    AlphaDuck.fly()
    AlphaDuck.quack()

    BetaDuck = DuckRedCrestedPochard('BetaDuck')
    BetaDuck.swim()
    BetaDuck.fly()
    BetaDuck.quack()

    GammaDuck = WoodDuck('GammaDuck')   # can't quack and fly
    #GammaDuck.quack()
    #GammaDuck.fly()
    Manok = DuckDecoy('DuckManok')  # can quack
    Manok.quack()
