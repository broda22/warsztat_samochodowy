from mody import Modyfikacje, Samochod, Kierownik
def test_pierwszy_mod():
    audi = Samochod("RWD", 180, False, None)
    turbina = Modyfikacje(1295.4, 300, 60, None, None)
    montaz = Kierownik()
    wynik_pracy = montaz.zamontuj(audi, turbina)
    wyliczona_cena, wyliczony_czas = montaz.podlicz(audi)
    assert wynik_pracy == True
    assert wyliczona_cena == 1295.4
    assert wyliczony_czas == 300