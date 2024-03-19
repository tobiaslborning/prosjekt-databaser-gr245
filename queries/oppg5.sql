SELECT DISTINCT StykkeNavn, Ansatt.Navn as SkuespillerNavn, RolleNavn
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
ORDER BY StykkeNavn