SELECT tstykke.Navn,  topps.Dato, tsal.Navn,  s.Omrade, s.RadNr, s.SeteNr, b.Pris
FROM Ordre as o
JOIN Billett as b
ON o.OrdreNr = b.OrdreNr
NATURAL JOIN Sete as s
JOIN TeaterOppsettning as topps
ON b.StykkeID = topps.StykkeID AND b.Dato = topps.Dato
NATURAL JOIN TeaterStykke as tstykke
JOIN TeaterSal as tsal
ON s.SalNr = tsal.SalNr
WHERE o.OrdreNr = 2