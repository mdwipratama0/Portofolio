SELECT city, S.stationid, DT.truck_type, ROUND(MAX(wastecollected)::numeric, 2) AS max_waste_collected
FROM FactTrips AS F
JOIN DimStation AS S
	ON F.stationid = S.stationid
JOIN DimDate AS D
	ON F.dateid = D.dateid
JOIN DimTruck AS DT
	ON F.truckid = DT.truckid
GROUP BY F.tripid, D.date, D.month, city, S.stationid, DT.truck_type;