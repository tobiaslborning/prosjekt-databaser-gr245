-- Create table for 'Ansatt'
CREATE TABLE Ansatt (
    AnsattID INT PRIMARY KEY,
    Navn VARCHAR(255),
    Epost VARCHAR(255),
);

-- Create table for 'Direktør'
CREATE TABLE Direktør (
    DirektørID INT PRIMARY KEY,
    AnsattID INT,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID)
);

-- Create table for 'Skuespiller'
CREATE TABLE Skuespiller (
    SkuespillerID INT PRIMARY KEY,
    AnsattID INT,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID)
);

-- Create table for 'Rolle'
CREATE TABLE Rolle (
    RolleID INT PRIMARY KEY,
    RolleNavn VARCHAR(255)
);

-- Create table for 'HarRolle'
CREATE TABLE HarRolle (
    SkuespillerID INT,
    RolleID INT,
    FOREIGN KEY (SkuespillerID) REFERENCES Skuespiller(SkuespillerID),
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID),
    PRIMARY KEY (SkuespillerID, RolleID)
);

-- Create table for 'RolleIAkt'
CREATE TABLE RolleIAkt (
    AktNr INT,
    StykkeID INT,
    RolleID INT,
    FOREIGN KEY (AktNr, StykkeID) REFERENCES Akt(AktNr, StykkeID),
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID),
    PRIMARY KEY (AktNr, StykkeID, RolleID)
);

-- Create table for 'Akt'
CREATE TABLE Akt (
    AktNr INT,
    StykkeID INT,
    Navn VARCHAR(255),
    PRIMARY KEY (AktNr, StykkeID),
    FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID)
);

-- Create table for 'TeaterStykke'
CREATE TABLE TeaterStykke (
    StykkeID INT PRIMARY KEY,
    Navn VARCHAR(255),
    SalNr INT,
    FOREIGN KEY (SalNr) REFERENCES TeaterSal(SalNr)
);

-- Create table for 'HarOppgave'
CREATE TABLE HarOppgave (
    StykkeID INT,
    AnsattID INT,
    OppgaveNavn VARCHAR(255),
    FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID),
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID),
    PRIMARY KEY (StykkeID, AnsattID)
);

-- Create table for 'TeaterOppsettning'
CREATE TABLE TeaterOppsettning (
    Dato DATE,
    StykkeID INT,
    PRIMARY KEY (Dato, StykkeID),
    FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID)
);

-- Create table for 'TeaterSal'
CREATE TABLE TeaterSal (
    SalNr INT PRIMARY KEY,
    Navn VARCHAR(255),
    Kapasitet INT
);

-- Create table for 'Sete'
CREATE TABLE Sete (
    SalNr INT,
    SeteNr INT,
    RadNr INT,
    Område VARCHAR(255),
    PRIMARY KEY (SalNr, SeteNr),
    FOREIGN KEY (SalNr) REFERENCES TeaterSal(SalNr)
);

-- Create table for 'Billett'
CREATE TABLE Billett (
    BillettNr INT PRIMARY KEY,
    StykkeID INT,
    Dato DATE,
    SalNr INT,
    SeteNr INT,
    BillettType VARCHAR(255),
    Pris DECIMAL(10, 2),
    OrdreNr INT,
    FOREIGN KEY (StykkeID, Dato) REFERENCES TeaterOppsettning(StykkeID, Dato),
    FOREIGN KEY (SalNr, SeteNr) REFERENCES Sete(SalNr, SeteNr),
    FOREIGN KEY (OrdreNr) REFERENCES Ordre(OrdreID)
);

-- Create table for 'PrisTabell'
CREATE TABLE PrisTabell (
    StykkeID INT,
    BillettType VARCHAR(255),
    Pris DECIMAL(10, 2),
    PRIMARY KEY (StykkeID, BillettType),
    FOREIGN KEY (BillettType) REFERENCES Billett(BillettType)
);

-- Create table for 'Ordre'
CREATE TABLE Ordre (
    OrdreID INT PRIMARY KEY,
    KjøpsTid TIME,
    KjøpsDato DATE,
    Antall INT,
    Pris DECIMAL(10, 2),
    KundeNr INT,
    FOREIGN KEY (KundeNr) REFERENCES Kunde(KundeNr)
);

-- Create table for 'Kunde'
CREATE TABLE Kunde (
    KundeNr INT PRIMARY KEY,
    Navn VARCHAR(255),
    Mobilnummer VARCHAR(20),
    Adresse VARCHAR(255)
);
