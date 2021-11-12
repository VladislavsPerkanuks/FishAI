CREATE TABLE Lietotajs (
    ID              INTEGER PRIMARY KEY,
    Lietotaja_vards TEXT,
    Parole          TEXT
);

CREATE TABLE Prognozes (
	ID INTEGER PRIMARY KEY, 
	Lietotaja_nosaukums TEXT, 
	Nosaukums1 TEXT, 
	Procenti1 REAL, 
	Nosaukums2 TEXT, 
	Procenti2 REAL, 
	Nosaukums3 TEXT, 
	Procenti3 REAL
);

CREATE TABLE Loms (
    ID                  INTEGER PRIMARY KEY,
    prognozes_ID        INTEGER REFERENCES Prognozes (ID),
    Lietotaja_ID        INTEGER,
    Bilde               BLOB,
    Zivs_Nosaukums      TEXT,
    Lietotaja_Nosaukums TEXT,
    Zvejas_datums       TEXT,
    Zvejas_vieta        TEXT,
    svars               REAL,
    izmers              REAL,

    FOREIGN KEY (Lietotaja_ID) REFERENCES Lietotajs (ID),
    FOREIGN KEY (prognozes_ID) REFERENCES Prognozes(ID)
);
