from fastapi import FastAPI, HTTPException
from adaptery.baza_danych_atrapa import UdawanaBazaWarsztatu
from rdzen.mody import Samochod, FabrykaSamochodow
from pydantic import BaseModel
app = FastAPI()
baza = UdawanaBazaWarsztatu()
testowe_auto = Samochod("BMW", "RWD", 180, True, "BIA10994334", None)
baza.dopisz_auto(testowe_auto)

class ZamowienieAuta(BaseModel):
    rejestracja: str
    nazwa: str
    kuty: bool = False

@app.get("/modyfikacje/auta/aktywne")
def pokazAuta():
    auta_aktywne = baza.baza_aut
    wynik = []
    for rejestracja, auto in auta_aktywne.items():
        reprezentacja_auta = {
            "rejestracja": rejestracja,
            "nazwa": auto.nazwa,
            "konie": auto.konie,
            "naped": auto.r_naped,
            "kuty": auto.kuty
        }
        wynik.append(reprezentacja_auta)
    return wynik
@app.post("/modyfikacje/auta/dodawanie")
def dopiszAuto(zamowienie: ZamowienieAuta):
    auto_fabryczne = FabrykaSamochodow.stworz_auto(zamowienie.nazwa, zamowienie.rejestracja, zamowienie.kuty)
    baza.dopisz_auto(auto_fabryczne)
    return {"komunikat": "Auto zjechało z taśmy i trafiło do bazy!"}

@app.delete("/modyfikacje/auta/{rejestracja}")
def usunAuto(rejestracja:str):
    czy_usunieto = baza.usun_auto(rejestracja)
    if not czy_usunieto:
        raise HTTPException(status_code=404, detail="auto o takiej rejestracji nie istnieje w naszej bazie")
    return {"komunikat": f"Auto o rejestracji: {rejestracja} zostalo usuniete!"}
