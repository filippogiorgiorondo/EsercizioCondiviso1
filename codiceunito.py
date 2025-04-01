# Concerti disponibili
listaConcerti = ["Tiziano Ferro (0)", "Shade(1)", "Mirko Camparus(2)", " Geolier(3)", "Malgioglio(4)", "Gigi D'Alessio(5)"]

# Posti disponibili
postiTiziano = 0
postiShade = 0
postiMirko = 0
postiGeolier = 0
postiMalgioglio = 0
postiGigi = 0

concertiScelti = []

def aggiuntaPosti(concertoScelto):
    match int(concertoScelto):
        case 0:
            if postiTiziano == 10:
                print("Non puoi partecipare al concerto")
            else:    
                postiTiziano += 1
        case 1:
            if postiShade == 10:
                print("Non puoi partecipare al concerto")
            else:    
                postiShade += 1
        case 2:
            if postiMirko == 10:
                print("Non puoi partecipare al concerto")
            else:    
                postiMirko += 1
        case 3:
            if postiGeolier == 10:
                print("Non puoi partecipare al concerto")
            else:
                postiGeolier += 1
        case 4:
            if postiMalgioglio == 10:
                print("Non puoi partecipare al concerto")
            else:
                postiMalgioglio += 1
        case 5:
            if postiGigi == 10:
                print("Non puoi partecipare al concerto")
            else:
                postiGigi += 1
        case _:
            pass
    return postiTiziano, postiShade, postiMirko, postiGeolier, postiMalgioglio, postiGigi
    
def regConcerti():
    while quantiConcerti <=3:
        print(f"I concerti disponibili sono: {listaConcerti}")
        
        quantiConcerti = int(input("Inserisci il numero di concerti da vedere (puoi prenotarne al massimo 3)"))

        match quantiConcerti:
            case 1:
                concertoScelto = int(input("Inserisci il numero del concerto da aggiungere"))
                listaConcerti.append(listaConcerti[concertoScelto])
                aggiuntaPosti(concertoScelto)
                postiTiziano, postiShade, postiMirko, postiGeolier, postiMalgioglio, postiGigi = aggiuntaPosti(concertoScelto)

            case 2:
                for n in range(1,3):
                    concertoScelto = int(input("Inserisci il numero del concerto da aggiungere")) 
                    listaConcerti.append(listaConcerti[concertoScelto])
                    aggiuntaPosti(concertoScelto)
                    postiTiziano, postiShade, postiMirko, postiGeolier, postiMalgioglio, postiGigi = aggiuntaPosti(concertoScelto)

            case 3:
                for n in range(1,3):
                    concertoScelto = int(input("Inserisci il numero del concerto da aggiungere")) 
                    listaConcerti.append(listaConcerti[concertoScelto])
                    aggiuntaPosti(concertoScelto)
                    postiTiziano, postiShade, postiMirko, postiGeolier, postiMalgioglio, postiGigi = aggiuntaPosti(concertoScelto)

    
