import queries

def vis_forestillinger():
    input_dato = input("Skriv inn datoen du ønsker å se forestillinger for (dd-mm-yyyy): ")
    stykker = queries.getStykkerByDato(input_dato)
    print(f"\n----Forestillinger som vises på {input_dato}----\n")
    if len(stykker) == 0:
        print("Ingen forestillinger funnet for denne datoen")
        return
    for stykke in stykker:
        stykkeID = queries.getTeaterStykkeID(stykke)
        antallSolgt = queries.getSoldSeats(stykkeID, input_dato)
        print(f"{stykke}".ljust(35) + f"|    Antall seter solgt: {len(antallSolgt)}")

def vis_medskuespillere():
    input_skuespiller = input("Skriv inn navnet på skuespilleren du ønsker å se medskuespillere for: ")
    print(f"\n----Medskuespillere til {input_skuespiller}----\n")
    queries.getMedSkuespillere(input_skuespiller)

def printOversikt():
    print("--------------------------------------------------------")
    print("Hva ønsker du å gjøre?")
    print("1. Registrer ny bruker")
    print("2. Sjekk hvilke forestillingrer som finnes på en dato")
    print("3. Kjøp billett(er) til en forestilling")
    print("4. Vis medskuespillere til en skuespiller")
    print("5. Ordreoversikt")
    print("6. Avslutt programmet")
    print("")

def registrer_bruker():
    print("Registrer ny bruker\n")
    navn = input("Navn: ")
    telefon = input("Telefon: ")
    addresse = input("Addresse: ")
    queries.registrerKunde(navn, telefon, addresse)
    print(f"\n{navn} registrert \n")

def kjop_billetter():
    print("Dersom du ikke er registrert er du nødt til å registrere deg først")
    telefon = input("Skriv inn telefonnummeret registrert på brukeren din: ")
    
    kunde = queries.getKundeByTelefon(telefon)

    if kunde == None:
        print("Ingen bruker med dette telefonnummeret funnet")
        return
    print(f"\nVelkommen {kunde[1]}!\n")

    print("Hvilken forestilling ønsker du å kjøpe billetter til?")
    print("Størst av alt er kjærligheten - 1")
    print("Kongsemnene - 2\n")
    input_stykkeID = input("Skriv inn tallet til ønsket forestilling: ")

    if input_stykkeID not in ["1","2"]:
        print("Ugyldig valg")
        return
    
    datoer = queries.getDatoByStykkeID(input_stykkeID)
    print(f"\n----Datoer for forestillingen----\n")
    for dato in datoer:
        print(dato)
    input_dato = input("\nSkriv inn datoen du ønsker å kjøpe billetter til (dd-mm-yyyy): ")

    if input_dato not in datoer:
        print("Ugyldig dato")
        return

    valgteBillettTyper = dict() # Dict til å holde styr på billetter som skal kjøpes
    print(f"\n----Billettyper----\n")
    billettTyper = queries.getBillettTyperAndPris(input_stykkeID)
    for billettType in billettTyper:
        print(f"{billettType[0]} - {billettType[1]} kr")
    print("")

    while True:
        input_billettType = input("Skriv ønsket billetttype: ")
        antall = input("Skriv inn antall billetter: ")
        if input_billettType not in (x[0] for x in billettTyper):
            print("Ugyldig valg")
            continue
        else:
            if input_billettType not in valgteBillettTyper.keys():
                valgteBillettTyper[input_billettType] = int(antall)
            else:
                valgteBillettTyper[input_billettType] += int(antall)
        print("")
        fortsett = input("Ønsker du å legge til flere billettyper? (J/N): ")
        if fortsett.lower() == "n":
            break

    totalpris = 0
    antallBilletter = 0
    for billettType in valgteBillettTyper.keys():
        billettPris = int(queries.getPrisByBilletType(input_stykkeID, billettType))

        if billettType == "Ordinær" and valgteBillettTyper[billettType] >= 10: # Gruppe 10 Ordinær
            billettPris = billettPris - 30
        if billettType == "Honnør" and valgteBillettTyper[billettType] >= 10: # Gruppe 10 Honnør
            if input_stykkeID == "2":
                billettPris = billettPris - 20
            else:
                billettPris = billettPris - 30

        totalpris += billettPris * int(valgteBillettTyper[billettType])
        antallBilletter += int(valgteBillettTyper[billettType])
    
    print(f"\nTotalpris: {totalpris} kr")
    print(f"Antall billetter: {antallBilletter}\n")

    bekreft = input("Bekreft kjøp av billetter og fortsett til setevalg? (J/N): ")
    if bekreft.lower() == "n":
        return
    
    ordreNr = queries.createOrdre(antallBilletter, totalpris, kunde[0])

    navnOgSal = queries.getStykkeAndSalByID(input_stykkeID)

    print(f"\n----Setevalg for {navnOgSal[0]} på {input_dato} i sal {navnOgSal[1]}----\n")
    print(f"For liste over opptatte seter, tast 1")
    print("")
    valg = input("Skriv inn tallet til ønsket handling: ")
    if valg == "1":
        print(f"\n----Opptatte seter for {navnOgSal[0]} på {input_dato} i sal {navnOgSal[1]}----\n")
        for seteInfo in queries.getSoldSeatsWithInfo(input_stykkeID, input_dato):
            print(f"Rad {seteInfo[2]} Sete {seteInfo[3]} Område {seteInfo[4]}")
    
    for valgtBillettType in valgteBillettTyper.keys():
        for billett in range(0, valgteBillettTyper[valgtBillettType]):
            while(True):
                print(f"\n----Setevalg for billet nummer {billett + 1}, type {valgtBillettType}----\n")
                validOmrader = queries.getOmraderBySal(navnOgSal[1])
                print(f"Gyldige områder: " + ', '.join(validOmrader))
                print("")

                billett_radNr = input("Skriv inn radnummer: ")
                billett_seteNr = input("Skriv inn setenummer: ")
                billett_omrade = input("Skriv inn område: ")
                print("")
                billett_salNr = navnOgSal[1]
                billett_stykkeID = input_stykkeID
                billett_dato = input_dato
                billett_ordreNr = ordreNr
                billett_pris = queries.getPrisByBilletType(input_stykkeID, valgtBillettType)
                billett_seteID = queries.getSeteID(billett_salNr, billett_seteNr, billett_radNr, billett_omrade)
                soldSeats = queries.getSoldSeats(input_stykkeID, input_dato)

                if billett_seteID != None and billett_seteID not in soldSeats:
                    queries.createBillett(billett_stykkeID, billett_dato, billett_seteID, valgtBillettType, billett_ordreNr, billett_pris)
                    print(f"\nBillett {billett + 1} av type {valgtBillettType} kjøpt\n")
                    break
                else:
                    print("\nUgyldig sete")
                    valg = input("Skriv 1 for å avslutte kjøp av billetter, enter for å prøve på nytt\n")
                    if valg == "1":
                        queries.deleteOrdre(ordreNr)
                        return
                    continue
                    
    print(f"\nOrdre {ordreNr} fullført\n")
    print(f"---------Dine billetter---------\n")
    for billett in queries.getBilletterInOrdre(ordreNr):
        print(f"{billett[0]} - {billett[1]} - {billett[2]} - {billett[3]} - Rad Nr {billett[4]} - Sete Nr {billett[5]} - {billett[6]} kr")
        
    print(f"\nTotalpris: {totalpris} kr")

def hent_ordre():
    telefon = input("Skriv inn telefonnummeret registrert på brukeren din: ")
    ordre = queries.getKundeOrdre(telefon)
    if ordre == None:
        print("Ingen ordre med dette nummeret funnet")
        return
    for ordreNr in ordre:
        print(f"\n----OrdreNr: {ordreNr}----\n")
        for billett in queries.getBilletterInOrdre(ordreNr):
            print(f"{billett[0]} - {billett[1]} - {billett[2]} - {billett[3]} - Rad Nr {billett[4]} - Sete Nr {billett[5]} - {billett[6]} kr")
        print(f"\nTotalpris: {queries.getOrdrePris(ordreNr)} kr\n")

def main():
    printOversikt()
    
    while True:
        valg = input(
            "\nSkriv inn tallet til ønsket handling: ")
        if valg == "1":
            registrer_bruker()
            print("")
        elif valg == "2":
            vis_forestillinger()
            print("")
        elif valg == "3":
            kjop_billetter()
            print("")
        elif valg == "4":
            vis_medskuespillere()
            print("")
        elif valg == "5":
            hent_ordre()
            print("")
        elif valg == "6":
            print("\nAvslutter programmet\n")
            break
        else:
            printOversikt()
        
main()