import random

# Lista dei concerti disponibili
listaConcerti = [
    "Tiziano Ferro", 
    "Shade", 
    "Mirko Camparus", 
    "Geolier", 
    "Malgioglio", 
    "Gigi D'Alessio"
]

# Posti disponibili per ogni concerto
postiDisponibili = {concerto: 10 for concerto in listaConcerti}

# Utenti registrati (dizionario con nome utente e password)
utentiRegistrati = {}

def sign_in():
    """Registra un nuovo utente con nome e password"""
    name = input("Inserisci il tuo nome: ")
    
    if name in utentiRegistrati:
        print("Questo nome utente è già registrato. Scegli un altro nome.")
        return None
    
    password = input("Inserisci una password (deve contenere almeno un simbolo @, # o +): ")
    
    if any(s in password for s in ["@", "#", "+"]):
        utentiRegistrati[name] = password
        print("Registrazione completata con successo!")
        return name
    else:
        print("La password non è abbastanza sicura. Usa almeno uno dei simboli @, # o +.")
        return None

def login():
    """Permette a un utente di accedere"""
    name = input("Inserisci il tuo nome: ")
    password = input("Inserisci la tua password: ")
    
    if utentiRegistrati.get(name) == password:
        print("Accesso effettuato con successo!")
        return name
    else:
        print("Nome utente o password errati.")
        return None

def ha_password_segreta():
    """Controlla se l'utente conosce la password segreta per aggiungere concerti"""
    password_segreta = input("Inserisci la password segreta: ")
    return password_segreta == "GHIBLI"

def aggiuntaPosti(concerto):
    """Aggiunge un partecipante a un concerto se ci sono posti disponibili"""
    if postiDisponibili[concerto] > 0:
        postiDisponibili[concerto] -= 1
        print(f"Prenotazione confermata per {concerto}! Posti rimanenti: {postiDisponibili[concerto]}")
        return True
    else:
        print("Posti esauriti per questo concerto.")
        return False

def prenotaConcerto():
    """Permette a un utente di prenotare fino a 3 concerti"""
    concertiPrenotati = []

    print("Concerti disponibili:")
    for i, concerto in enumerate(listaConcerti):
        print(f"{i} - {concerto} ({postiDisponibili[concerto]} posti disponibili)")

    for _ in range(3):
        scelta = input("Inserisci il numero del concerto che vuoi prenotare (o premi Invio per terminare): ")
        
        if scelta == "":
            break

        if scelta.isdigit():
            scelta = int(scelta)
            if 0 <= scelta < len(listaConcerti):
                concerto_scelto = listaConcerti[scelta]
                if aggiuntaPosti(concerto_scelto):
                    concertiPrenotati.append(concerto_scelto)
            else:
                print("Scelta non valida.")
        else:
            print("Inserisci un numero valido.")

    print("I tuoi concerti prenotati:", concertiPrenotati)

def aggiungiConcerto():
    """Permette di aggiungere un concerto se si conosce la password segreta"""
    if ha_password_segreta():
        nuovo_concerto = input("Inserisci il nome del nuovo concerto: ")
        if nuovo_concerto not in listaConcerti:
            listaConcerti.append(nuovo_concerto)
            postiDisponibili[nuovo_concerto] = 10
            print(f"Concerto '{nuovo_concerto}' aggiunto con successo!")
        else:
            print("Questo concerto esiste già.")
    else:
        print("Password segreta errata. Non puoi aggiungere concerti.")

def main():
    """Gestisce il flusso principale del programma"""
    print("Benvenuto nel sistema di prenotazione concerti!")
    
    while True:
        scelta = input("Vuoi registrarti (R), accedere (L) o uscire (E)? ").upper()

        if scelta == "R":
            utente = sign_in()
        elif scelta == "L":
            utente = login()
            if utente:
                while True:
                    azione = input("Vuoi prenotare un concerto (P), aggiungere un concerto (A) o fare logout (L)? ").upper()
                    if azione == "P":
                        prenotaConcerto()
                    elif azione == "A":
                        aggiungiConcerto()
                    elif azione == "L":
                        break
                    else:
                        print("Scelta non valida.")
        elif scelta == "E":
            print("Grazie per aver usato il sistema di prenotazione!")
            break
        else:
            print("Scelta non valida.")

# Avvia il programma
main()
