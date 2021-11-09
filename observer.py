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
        self._punkte = 0
    def erhoehePunkte(self, anzahlPunkte):
        self._punkte += anzahlPunkte
        print("Meine Punkte sind nun", self._punkte)
        self._notify()
        return self._punkte