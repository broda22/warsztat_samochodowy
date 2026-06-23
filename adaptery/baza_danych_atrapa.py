from port.wymogi import RepozytoriumWarsztatu
from rdzen.mody import Samochod, Modyfikacje


class UdawanaBazaWarsztatu(RepozytoriumWarsztatu):
    def __init__(self):
        self.baza_aut = {}
        self.magazyn_modow = []
    def dopisz_auto(self, auto: Samochod):
        self.baza_aut[auto.rejestracja] = auto
    def pobierz_auto(self, rejestracja: str):
        baza_auto = self.baza_aut
        return baza_auto.get(rejestracja)
    def dopisz_mody(self,   mod: Modyfikacje):
        self.magazyn_modow.append(mod)
    def usun_auto(self, rejestracja: str):
        if rejestracja in self.baza_aut:
            del self.baza_aut[rejestracja]
            return True
        else:
            return False