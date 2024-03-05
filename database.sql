-- Create table for 'Ansatt'
CREATE TABLE Ansatt (
    AnsattID INT PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    Epost VARCHAR(50) NOT NULL,
    AnsattStatus VARCHAR(50) NOT NULL
);

-- Create table for 'Direktør'
CREATE TABLE Direktor (
    DirektorID INT PRIMARY KEY,
    AnsattID INT,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create table for 'Skuespiller'
CREATE TABLE Skuespiller (
    SkuespillerID INT PRIMARY KEY,
    AnsattID INT,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create table for 'Rolle'
CREATE TABLE Rolle (
    RolleID INT PRIMARY KEY,
    RolleNavn VARCHAR(50) NOT NULL
);

-- Create table for 'HarRolle'
CREATE TABLE HarRolle (
    SkuespillerID INT,
    RolleID INT,
    FOREIGN KEY (SkuespillerID) REFERENCES Skuespiller(SkuespillerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (SkuespillerID, RolleID)
);

-- Create table for 'RolleIAkt'
CREATE TABLE RolleIAkt (
    AktNr INT,
    StykkeID INT,
    RolleID INT,
    FOREIGN KEY (AktNr, StykkeID) REFERENCES Akt(AktNr, StykkeID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (AktNr, StykkeID, RolleID)
);

-- Create table for 'Akt'
CREATE TABLE Akt (
    AktNr INT,
    StykkeID INT,
    Navn VARCHAR(50) NOT NULL,
    PRIMARY KEY (AktNr, StykkeID),
    FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create table for 'TeaterStykke'
CREATE TABLE TeaterStykke (
    StykkeID INT PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    SalNr INT NULL, -- NULL if not performed in a theater
    FOREIGN KEY (SalNr) REFERENCES TeaterSal(SalNr) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Create table for 'HarOppgave'
CREATE TABLE HarOppgave (
    StykkeID INT,
    AnsattID INT,
    OppgaveNavn VARCHAR(50),
    FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (StykkeID, AnsattID, OppgaveNavn)
);

-- Create table for 'TeaterOppsettning'
CREATE TABLE TeaterOppsettning (
    Dato DATE,
    StykkeID INT,
    PRIMARY KEY (Dato, StykkeID),
    FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create table for 'TeaterSal'
CREATE TABLE TeaterSal (
    SalNr INT PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
);

-- Create table for 'Sete'
CREATE TABLE Sete (
    SalNr INT,
    SeteNr INT,
    RadNr INT NULL, -- Can be null i Område GALLERI (ØVRE/NEDRE) in Sal HovedScene
    Område VARCHAR(50) NOT NULL,
    PRIMARY KEY (SalNr, SeteNr),
    FOREIGN KEY (SalNr) REFERENCES TeaterSal(SalNr) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create table for 'Billett'
CREATE TABLE Billett (
    BillettNr INT PRIMARY KEY,
    StykkeID INT,
    Dato DATE,
    SalNr INT,
    SeteNr INT,
    BillettType VARCHAR(50) NOT NULL,
    OrdreNr INT,
    FOREIGN KEY (StykkeID, Dato) REFERENCES TeaterOppsettning(StykkeID, Dato) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (SalNr, SeteNr) REFERENCES Sete(SalNr, SeteNr) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (OrdreNr) REFERENCES Ordre(OrdreID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create table for 'PrisTabell'
CREATE TABLE PrisTabell (
    StykkeID INT,
    BillettType VARCHAR(50),
    Pris DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (StykkeID, BillettType),
    FOREIGN KEY (BillettType) REFERENCES Billett(BillettType) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create table for 'Ordre'
CREATE TABLE Ordre (
    OrdreID INT PRIMARY KEY,
    KjøpsTid TIME NOT NULL,
    KjøpsDato DATE NOT NULL,
    Antall INT NOT NULL,
    Pris DECIMAL(10, 2) NOT NULL,
    KundeNr INT,
    FOREIGN KEY (KundeNr) REFERENCES Kunde(KundeNr) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create table for 'Kunde'
CREATE TABLE Kunde (
    KundeNr INT PRIMARY KEY,
    Navn VARCHAR(50) NOT NULL,
    Mobilnummer VARCHAR(20) NOT NULL,
    Adresse VARCHAR(50) NOT NULL
);
