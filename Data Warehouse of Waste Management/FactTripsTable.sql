CREATE TABLE FactTrips(
    tripid INTEGER PRIMARY KEY NOT NULL,
    dateid INTEGER NOT NULL,
    stationid INTEGER NOT NULL,
    truckid INTEGER NOT NULL,
    wastecollected NUMERIC(5,2)
);

ALTER TABLE FactTrips
    ADD FOREIGN KEY (dateid)
    REFERENCES DimDate(dateid)
    NOT VALID;

ALTER TABLE FactTrips
    ADD FOREIGN KEY (stationid)
    REFERENCES DimStation(stationid)
    NOT VALID;

ALTER TABLE FactTrips
    ADD FOREIGN KEY (truckid)
    REFERENCES DimTruck(truckid)
    NOT VALID;

