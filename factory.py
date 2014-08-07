__author__ = 'sergey'


class PizzaFactory:
    def __init__(self, pizzaType):
        print "I'm pizza Factory"
        self.pizzaType = pizzaType

    def createPizza(self):
        targetPizza = self.pizzaType#.capitalize()
        #return globals()[targetPizza]()
        self.pizza = globals()[targetPizza]()
        print self.pizza


class AbstractPizza:
    pizza = ""

    def get_pizza(self):

        return self.pizza


class SanFranciscoPizza(AbstractPizza):
    pizza = 'thin crust, lots of cheese, sauce, ham'


class ChicagoPizza(AbstractPizza):
    pizza = 'thin dough, a little cheese, gravy, sausage'


if __name__ == '__main__':
    pizza1 = PizzaFactory('ChicagoPizza')
    print pizza1.createPizza()