
CREATE TABLE Ansatt (
    AnsattID INT PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    Epost VARCHAR(50) NOT NULL,
    AnsattStatus VARCHAR(50) NOT NULL -- Må være {fast,midlertidig,innleid,frivillig eller statist} håndteres i applikasjon
);


CREATE TABLE Direktor (
    DirektorID INT PRIMARY KEY,
    AnsattID INT,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Skuespiller (
    SkuespillerID INT PRIMARY KEY,
    AnsattID INT,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Rolle (
    RolleID INT PRIMARY KEY,
    RolleNavn VARCHAR(50) NOT NULL
);

CREATE TABLE HarRolle (
    SkuespillerID INT,
    RolleID INT,
    FOREIGN KEY (SkuespillerID) REFERENCES Skuespiller(SkuespillerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (SkuespillerID, RolleID)
);

CREATE TABLE RolleIAkt (
    AktNr INT,
    StykkeID INT,
    RolleID INT,
    FOREIGN KEY (AktNr, StykkeID) REFERENCES Akt(AktNr, StykkeID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (AktNr, StykkeID, RolleID)
);

CREATE TABLE Akt (
    AktNr INT,
    StykkeID INT,
    Navn VARCHAR(50) NOT NULL,
    PRIMARY KEY (AktNr, StykkeID),
    FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE TeaterStykke (
    StykkeID INT PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    SalNr INT NULL, -- NULL if not performed in a theater
    FOREIGN KEY (SalNr) REFERENCES TeaterSal(SalNr) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE HarOppgave (
    StykkeID INT,
    AnsattID INT,
    OppgaveNavn VARCHAR(50),
    FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (StykkeID, AnsattID, OppgaveNavn)
);

CREATE TABLE TeaterOppsettning (
    Dato DATE,
    StykkeID INT,
    PRIMARY KEY (Dato, StykkeID),
    FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE TeaterSal (
    SalNr INT PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL
);

CREATE TABLE Sete (
    SalNr INT,
    SeteNr INT,
    RadNr INT NULL, -- Can be null i Område GALLERI (ØVRE/NEDRE) in Sal HovedScene
    Område VARCHAR(50) NOT NULL,
    PRIMARY KEY (SalNr, SeteNr),
    FOREIGN KEY (SalNr) REFERENCES TeaterSal(SalNr) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Billett (
    BillettNr INT PRIMARY KEY,
    StykkeID INT,
    Dato DATE,
    SalNr INT,
    SeteNr INT,
    BillettType VARCHAR(50) NOT NULL, -- Har ett sett med lovlige verdier for StykkeID, disse ligger i PrisTabell, hånderes i applikasjon
    OrdreNr INT,
    Pris INT NOT NULL, --  Kalkulert i applikasjon fra PrisTabell ved å bruke StykkeID og BillettType fra input i applikasjon
    FOREIGN KEY (StykkeID, Dato) REFERENCES TeaterOppsettning(StykkeID, Dato) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (SalNr, SeteNr) REFERENCES Sete(SalNr, SeteNr) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (OrdreNr) REFERENCES Ordre(OrdreID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE PrisTabell (
    StykkeID INT,
    BillettType VARCHAR(50),
    Pris INT NOT NULL,
    PRIMARY KEY (StykkeID, BillettType),
    FOREIGN KEY (BillettType) REFERENCES Billett(BillettType) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Ordre (
    OrdreID INT PRIMARY KEY,
    KjopsTid TIME NOT NULL,
    KjopsDato DATE NOT NULL,
    Antall INT NOT NULL,
    Pris INT NOT NULL, 
    KundeNr INT,
    FOREIGN KEY (KundeNr) REFERENCES Kunde(KundeNr) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Kunde (
    KundeNr INT PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    Mobilnummer VARCHAR(20) NOT NULL,
    Adresse VARCHAR(50) NOT NULL
);
