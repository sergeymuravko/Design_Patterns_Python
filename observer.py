import time
import random


class Listener:
    def __init__(self, subject, name):
        print 'create listeners ' + name
        self.name = name
        subject.register(self)

    def notify(self):
        print "I'm listen, ", self.name, '\n and go read'


class Subject:
    def __init__(self, name, exemplars):
        self.listeners = []
        self.name = name
        self.exemplars = exemplars
        print 'Subject name -> "' + name + '"'
        #self.doNews()

    def doNews(self):
        print 'published,\n exemplar number -> ' + str(count) + ', time -> ' + str(time.clock())
        
        self.notifyListeners()

    def register(self, listener):
        self.listeners.append(listener)
        #print 'register'

    def unregister(self, listener):
        pass

    def notifyListeners(self):
        for listener in self.listeners:
            listener.notify()


if __name__ == '__main__':
    newspaper = Subject('The New York Times', 20)

    subscriber1 = Listener(newspaper, 'Tom')
    subscriber2 = Listener(newspaper, 'Nick')

    count = 1

    while count < newspaper.exemplars:
        t = random.randrange(2, 5)
        time.sleep(t)
        newspaper.doNews()
        count += 1


