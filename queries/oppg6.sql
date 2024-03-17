SELECT stykke.navn, oppsettning.dato, ifnull(antallSolgt,0) as billetterSolgt
FROM TeaterStykke AS stykke
NATURAL JOIN TeaterOppsettning AS oppsettning
LEFT OUTER JOIN (
    SELECT StykkeID, Dato, COUNT(*) AS antallSolgt
    FROM Billett
    GROUP BY StykkeID, Dato
) AS b 
ON stykke.StykkeID = b.StykkeID AND oppsettning.dato = b.Dato
ORDER BY billetterSolgt DESC