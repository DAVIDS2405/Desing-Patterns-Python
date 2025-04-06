from abc import ABC, abstractmethod


class BeerBrewing(ABC):
    def ferment(self):
        print("Ferment the beer")

    def bottle(self):
        print("Bottle the beer")

    @abstractmethod
    def select_ingredients(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass

    def prepare(self):
        self.select_ingredients()
        self.ferment()
        self.add_extras()
        self.bottle()


class LagerBeer(BeerBrewing):
    def select_ingredients(self):
        print("Select ingredients for Lager beer")

    def add_extras(self):
        print("Add extras for Lager beer")


class StoutBeer(BeerBrewing):
    def select_ingredients(self):
        print("Select ingredients for Stout beer")

    def add_extras(self):
        print("Add extras for Stout beer")


class SourBeer(BeerBrewing):
    def select_ingredients(self):
        print("Select ingredients for Sour beer")

    def add_extras(self):
        print("Add extras for Sour beer")

    def ferment(self):
        print("Ferment the beer with wild yeast")


lager = LagerBeer()
lager.prepare()
print("---------")
stout = StoutBeer()
stout.prepare()
print("---------")
sour = SourBeer()
sour.prepare()
