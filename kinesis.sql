CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    "fleet" VARCHAR(10), 
	"firstval" double,
	"lastval" double);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
    INSERT INTO "DESTINATION_SQL_STREAM"
    SELECT STREAM "fleet",   
                  FIRST_VALUE("mileage") OVER W1 AS "firstval",
                  LAST_VALUE("mileage") OVER W1 AS "lastval"
 FROM "SOURCE_SQL_STREAM_001"
    WINDOW W1 AS (
        PARTITION BY "fleet" 
        RANGE INTERVAL '1' MINUTE PRECEDING);
        
 CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM_DIFF" (
    "fleet" VARCHAR(10), 
	"distdiff" double);
 CREATE OR REPLACE PUMP "STREAM_PUMP_DIFF" AS 
    INSERT INTO "DESTINATION_SQL_STREAM_DIFF"
    SELECT STREAM "fleet", "lastval" - "firstval" AS "distdiff"
    FROM "DESTINATION_SQL_STREAM"
