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

def printOversikt():
    print("--------------------------------------------------------")
    print("Hva ønsker du å gjøre?")
    print("1. Registrer ny bruker")
    print("2. Sjekk hvilke forestillingrer som finnes på en dato")
    print("3. Kjøp billetter")
    print("4. Avslutt programmet")
    print("")

def main():
    printOversikt()
    
    while True:
        valg = input(
            "\nSkriv inn tallet til ønsket handling: ")
        if valg == "1":
            print("Registrer ny bruker")
        elif valg == "2":
            vis_forestillinger()
            print("")
        elif valg == "3":
            print("Kjøp billetter")
        elif valg == "4":
            print("\nAvslutter programmet\n")
            break
        else:
            printOversikt()
        
main()