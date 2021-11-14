class ObserverSubject:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self)


class Player(ObserverSubject):
    def __init__(self):
        ObserverSubject.__init__(self)
        self._points = 0

    def raisePoints(self, amountPoints):
        self._points += amountPoints
        self._notify()
        return self._points
