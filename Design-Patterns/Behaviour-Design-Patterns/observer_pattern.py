

class Observer():

    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def unregister_all(self):
        self.observers.clear()

    def update(self, *args, **kwargs):
        for each in self.observers:
            each.update(*args, **kwargs)


class Observable():

    def update(self, *args, **kwargs):
        pass


class UsMarket(Observable):

    def update(self, *args, **kwargs):
        print (f"Update on Us Market {args} \n {kwargs}")


class AsiaMarket(Observable):

    def update(self, *args, **kwargs):
        print (f"Update on Asia Market {args} \n {kwargs}")


market_observer = Observer()
us_market = UsMarket()
asia_market = AsiaMarket()

market_observer.register_observer(us_market)
market_observer.register_observer(asia_market)

market_observer.update("Alert !!", {"warning": "Trump died. Market may go down"})


