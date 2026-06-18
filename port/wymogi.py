from abc import ABC, abstractmethod

from rdzen.mody import Samochod, Modyfikacje

class RepozytoriumWarsztatu(ABC):
    @abstractmethod
    def dopisz_auto(self, auto: Samochod):
        pass
    @abstractmethod
    def dopisz_mody(self, mody : Modyfikacje):
        pass
    @abstractmethod
    def pobierz_auto(self, rejestracja: str):
        pass
