# ######################################################
# ### Ratespiel ########################################
# ### Spieler muss Zufallszahl zw. 1 und 100 erraten ###
# ### score = Anzahl benötigte Versuche ################
# ######################################################

# ### MODULE
# Zufallszahlen
import random as rd


# ### FUNKTIONEN
# Zufallszahl zwischen 1 und 100 generieren
def zufallszahl():
    return rd.randint(1, 100)


# Eingabe und Prüfung abfragen und prüfen, ob
def eingabe_und_pruefung_zahl() -> int:
    while True:
        try:
            eingabe = input("\nRate die gesuchte Zahl: ")
            if eingabe.isdigit() and 1 <= int(eingabe) <= 100:
                eingabe = int(eingabe)
                return eingabe
            else:
                raise ValueError
        except ValueError:
            print("Die Eingabe muss eine Ganzzahl zw. 1 und 100 sein. Gib eine neue Zahl ein.")


# Eingabe mit generierter Zahl vergleichen
def vergleich(eingegebener_wert: int, zahl: int) -> str:
    if eingegebener_wert == zahl:
        return "korrekt"
    elif eingegebener_wert > zahl:
        return "kleiner"
    elif eingegebener_wert < zahl:
        return "größer"


# Spiel ausführen
def run_game():
    print("\nErrate die Zufallszahl zwischen 1 und 100."
          "\n(Fehlerhafte Eingaben zählen nicht als Versuch)")
    erzeugte_zahl = zufallszahl()
    score = 0
    while True:
        eingabewert = eingabe_und_pruefung_zahl()
        ergebnis_vergleich = vergleich(eingabewert, erzeugte_zahl)
        score += 1
        if ergebnis_vergleich == "korrekt":
            text = f"*** Die geratene Zahl ist korrekt. Benötigte Versuche: {score}. ***"
            print(f"\n{len(text)*"*"}"
                  f"\n{text}"
                  f"\n{len(text)*"*"}")
            break
        else:
            print(f"\nDie gesuchte Zahl ist {ergebnis_vergleich} als der eingegebene Wert. Probier es erneut.")
            print(f"Bisherige Anzahl Versuche: {score}")
    return score


# Score in Datei schreiben
def score_schreiben(punkte):
    dateiname = "Scores.txt"
    spieler_name = input("\nGib ein welcher Name in der Score-Liste angezeigt werden soll: ")
    with open(dateiname, 'a') as w:
        w.write(f"\n{spieler_name}: {punkte} Versuche")


def loop_game_and_write_score():
    weiterspielen = "ja"
    while weiterspielen == "ja":
        punktzahl = run_game()
        score_schreiben(punktzahl)
        while True:
            weiterspielen = input("Möchtest du eine neue Runde starten? (Ja/Nein): ").lower()
            if weiterspielen == "ja" or "nein":
                break
            else:
                print("""Bitte gib "Ja" oder "Nein" ein.""")


# ### PROGRAMM
if __name__ == "__main__":
    loop_game_and_write_score()
