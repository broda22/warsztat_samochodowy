from fastapi import FastAPI
app = FastAPI()
@app.get("/modyfikacje/auta/aktywne")
def pokazAuta():
    return [
    {"rejestracja": "BIA19059339", "konie": 240, "naped": "RWD", "kuty": False},
    {"rejestracja": "BIA96398648", "konie": 280, "naped": "AWD", "kuty": True}
    ]