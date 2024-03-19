SELECT AktTilSkuespiller.Navn, SkuespillereInAkt.Navn, AktTilSkuespiller.AktNr, AktTilSkuespiller.StykkeNavn
FROM
(SELECT DISTINCT AktRoller.AktNr, AktRoller.StykkeID, AktRoller.StykkeNavn, Ansatt.Navn
                    FROM (
                        SELECT ts.navn as StykkeNavn, ts.StykkeID, a.AktNr, a.Navn as AktNavn, Rolle.RolleNavn, Rolle.RolleID 
                        FROM Akt as a
                        JOIN RolleIAkt as ria
                        ON a.AktNr = ria.AktNr AND a.StykkeID = ria.StykkeID
                        NATURAL JOIN Rolle
                        JOIN TeaterStykke as ts
                        ON ts.StykkeID = a.StykkeID
                        ) as AktRoller
                    JOIN HarRolle as hr
                    ON AktRoller.RolleID = hr.RolleID
                    NATURAL JOIN Skuespiller
                    NATURAL JOIN Ansatt
                    WHERE Ansatt.Navn = "Arturo Scotti"
) as AktTilSkuespiller
JOIN
(SELECT DISTINCT Navn, Aktnr, StykkeID
                    FROM (
                        SELECT ts.navn as StykkeNavn, ts.StykkeID, a.AktNr, a.Navn as AktNavn, Rolle.RolleNavn, Rolle.RolleID 
                        FROM Akt as a
                        JOIN RolleIAkt as ria
                        ON a.AktNr = ria.AktNr AND a.StykkeID = ria.StykkeID
                        NATURAL JOIN Rolle
                        JOIN TeaterStykke as ts
                        ON ts.StykkeID = a.StykkeID
                        ) as AktRoller
                    JOIN HarRolle as hr
                    ON AktRoller.RolleID = hr.RolleID
                    NATURAL JOIN Skuespiller
                    NATURAL JOIN Ansatt
) as SkuespillereInAkt
ON AktTilSkuespiller.AktNr = SkuespillereInAkt.AktNr AND AktTilSkuespiller.StykkeID = SkuespillereInAkt.StykkeID
WHERE SkuespillereInAkt.Navn != AktTilSkuespiller.Navn -- Fjern spiller med seg selv.