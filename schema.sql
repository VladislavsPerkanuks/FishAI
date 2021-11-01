CREATE TABLE IF NOT EXISTS `Lietotajs` (
  `ID` INTEGER PRIMARY KEY ,
  `Lietotaja_vards` TEXT,
  `Parole` TEXT
);

CREATE TABLE IF NOT EXISTS`Zivis` (
  `ID` INTEGER PRIMARY KEY ,
  `Latviesu_nosaukums` TEXT,
  `Zinatniskais_nosaukums` TEXT,
  `Apraksts` TEXT,
  `Bilde` BLOB
);

CREATE TABLE IF NOT EXISTS `Loms` (
  `ID` INTEGER PRIMARY KEY ,
  `Lietotaja_ID` INTEGER,
  `Bilde` BLOB,
  `Zivs_ID` INTEGER,
  `Zvejas_datums` TEXT,
  `Zvejas_vietas_ID` INTEGER,
  FOREIGN KEY (Lietotaja_ID) REFERENCES Lietotajs(ID),
  FOREIGN KEY (Zivs_ID) REFERENCES Zivis(ID),
  FOREIGN KEY (Zvejas_vietas_ID) REFERENCES Zvejas_vieta(ID)
);

CREATE TABLE IF NOT EXISTS`Zvejas_vieta` (
  `ID` INTEGER PRIMARY KEY ,
  `Platuma_gradi` REAL,
  `Garuma_gradi` REAL
);


