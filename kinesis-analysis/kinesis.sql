 CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    "fleet" VARCHAR(10), 
    "load" double,
    "temperature" double,
    "terrain" double,
    "mileage" double,
	"firstval" double,
	"lastval" double);


CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
    INSERT INTO "DESTINATION_SQL_STREAM"
    SELECT STREAM "FLEET", 
                    AVG("LOAD") OVER W1 AS "load",
                    AVG("TEMPERATURE") OVER W1 AS "temperature",
                    AVG("TERRAIN") OVER W1 AS "terrain",
                    MAX("MILEAGE") OVER W1 AS "mileage",
                  FIRST_VALUE("VELOCITY") OVER W1 AS "firstval",
                  LAST_VALUE("VELOCITY") OVER W1 AS "lastval"
 FROM "SOURCE_SQL_STREAM_001"
    WINDOW W1 AS (
        PARTITION BY "FLEET" 
        RANGE INTERVAL '1' MINUTE PRECEDING);


 CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM_DIFF" (
    "fleet" VARCHAR(10), 
    "load" double,
    "temperature" double,
    "terrain" double,
    "mileage" double,
	"veldiff" double);


 CREATE OR REPLACE PUMP "STREAM_PUMP_DIFF" AS 
	    INSERT INTO "DESTINATION_SQL_STREAM_DIFF"
	    SELECT STREAM "fleet", "load", "temperature", "terrain", "mileage", "lastval" - "firstval" AS "veldiff"
	    FROM "DESTINATION_SQL_STREAM";
	    
 CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM_ACC" (
    "fleet" VARCHAR(10), 
    "load" double,
    "temperature" double,
    "terrain" double,
    "mileage" double,
	"acc" double);
	
 CREATE OR REPLACE PUMP "STREAM_PUMP_ACC" AS 
	    INSERT INTO "DESTINATION_SQL_STREAM_ACC"
	    SELECT STREAM "fleet", "load", "temperature", "terrain", "mileage", "veldiff"/60 AS "acc"
	    FROM "DESTINATION_SQL_STREAM_DIFF";
