-- With The Sliding window of the 1 Minute Calculate the Starting Velocity and Ending Velocity.
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
        

-- From Previous In-Memory Stream calculate the Velocity Difference With in the Window Duration.


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
	    
-- From the Velocity Difference Calculated in Previous stream calculate the Accleration of deceleration occured in each window.
	    
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
	    

-- From all the previous streams calculate the features such as Average Load on Truck, Average temperature of tires, Average Terrain condition of road and number of brakes applied.
-- Thos features will help us to identify the tire wear and condition in realtime.
	    
 CREATE OR REPLACE STREAM "FINAL_ANALYSIS_STREAM"(
 "fleet" VARCHAR(10),
 "load" double,
 "temperature" double,
 "terrain" double,
 "brakes" integer);
 
 CREATE OR REPLACE PUMP "FINAL_ANALYSIS_PUMP" AS
    INSERT INTO "FINAL_ANALYSIS_STREAM"
    SELECT STREAM "fleet",                         
        AVG("load") AS "load",
        AVG("temperature") AS "temperature",
        AVG("terrain") AS "terrain",
        COUNT("acc") as "brakes"
        FROM "DESTINATION_SQL_STREAM_ACC" where "acc" < 0
        GROUP BY "fleet",
        STEP("DESTINATION_SQL_STREAM_ACC".ROWTIME BY INTERVAL '2' MINUTE);
