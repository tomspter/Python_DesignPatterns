from abc import ABCMeta, abstractmethod
from model import Observer, Observable

class WaterHeater(Observable):

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("now temperature:{}".format(self.__temperature))
        self.notifyObservers()

class WashingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and observable.getTemperature() > 50 \
                and observable.getTemperature() < 70:
            print("washing now")

class DrinkingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("drinking now")

if __name__ == '__main__':
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)
